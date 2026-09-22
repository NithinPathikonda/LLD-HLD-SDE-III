# System Design Architecture: Design Ride-Sharing Platform (Uber / Lyft)

## 1. Requirements & Scope
- **Functional Requirements**: Core user workflows and contracts.
- **Non-Functional Requirements**: High availability, P99 latency goals, consistency trade-offs.

---

## 2. Scale & Back-of-the-Envelope Estimation
- **DAU**: 50 Million daily active riders, 5 Million active drivers
- **WRITES**: 5 Million drivers emit GPS coordinates every 4 seconds = 1.25 Million writes/sec location ingestion
- **READS**: Riders querying nearby drivers every 5 seconds = ~200,000 queries/sec
- **STORAGE**: Driver location ping = 64 bytes. 1.25M * 64B = 80 MB/s ingestion bandwidth
- **CACHE**: Active driver locations kept entirely in RAM (Redis / Custom In-Memory Geospatial Ring)

---

## 3. API Contracts & Data Schema
### API Endpoints
- `POST /api/v1/driver/location -> { driver_id: string, lat: float, lon: float, status: 'AVAILABLE'|'BUSY' }`
- `POST /api/v1/ride/request -> { rider_id: string, pickup_lat: float, pickup_lon: float, drop_lat: float, drop_lon: float } -> { ride_id: string, status: 'MATCHING' }`
- `GET /api/v1/drivers/nearby?lat=...&lon=...&radius=3km -> { drivers: [...] }`

### Data Schema
```sql
Table: driver_locations (In-Memory / Redis Geospatial)
- driver_id: UUID PK
- h3_index: VARCHAR(15) INDEX (Uber H3 Hexagonal Cell)
- lat: DOUBLE, lon: DOUBLE
- updated_at: TIMESTAMP

Table: trips
- trip_id: UUID PK
- rider_id: UUID FK
- driver_id: UUID FK
- status: ENUM ('REQUESTED', 'ACCEPTED', 'IN_TRANSIT', 'COMPLETED', 'CANCELLED')
- pickup_location: POINT, drop_location: POINT
- fare_amount: DECIMAL(10, 2)
```

---

## 4. High-Level System Architecture
```mermaid
graph TD
    Driver[Driver App] -->|WebSocket GPS Ping| Gateway[Location Gateway]
    Gateway --> Kafka[Kafka Location Queue]
    Kafka --> GeoService[Geospatial Service (H3 Ring)]
    GeoService --> GeoRedis[(In-Memory Geospatial Cache)]

    Rider[Rider App] -->|HTTP Request Ride| DispatchService[Dispatch & Matching Engine]
    DispatchService --> GeoRedis
    DispatchService --> TripDB[(Trips Database)]
```

---

## 5. SDE-III Deep Dives & Bottlenecks
### **Geospatial Indexing Choice**: Uber H3 (Hexagonal Hierarchical Spatial Index) vs Google S2 vs QuadTree. Hexagons have equal distance to all 6 adjacent neighbors (unlike squares in S2/QuadTree), making radius searches smooth.

### **Decoupled Location Ingestion**: Ingesting 1.25M writes/s directly into DB will crash it. Use Kafka partitioned by `h3_cell_id` with memory-mapped buffer workers updating in-memory Geospatial Cache.

### **Driver-Rider Matching Lock**: When dispatching a trip to the nearest driver, use a short-lived Redis lock on `driver_id` with a 15-second acceptance window to avoid race condition of offering same driver to multiple riders.

---

## 6. Interview Checklist
- [ ] Explained tradeoffs between SQL vs NoSQL for this specific data access pattern
- [ ] Addressed single points of failure (SPOF) with redundancy
- [ ] Solved caching stampede / hot partition challenges
- [ ] Defined metric observability and disaster recovery plan
