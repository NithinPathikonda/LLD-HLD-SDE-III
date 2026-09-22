# SDE-III High-Level System Design (HLD) 45-Minute Blueprint

In SDE-III / Staff System Design interviews, the bar is not just drawing boxes and arrows. Interviewers evaluate:
1. **Scope Leadership**: Driving the conversation, prioritizing business-critical tradeoffs.
2. **Back-of-the-Envelope Estimation**: Translating traffic/storage numbers into hardware constraints.
3. **Data Architecture**: Relational vs NoSQL, sharding schemes, index design, replication lag mitigation.
4. **Resiliency & Fault Tolerance**: Circuit breakers, dead letter queues, rate limiters, split-brain avoidance.
5. **Observability**: Metrics, distributed tracing, alerting, SLOs/SLAs.

---

## 45-Minute Time Allocation

| Time | Phase | Focus |
| :--- | :--- | :--- |
| **00 - 05 min** | **1. Scope & Requirements** | Functional & Non-Functional Requirements, Constraints, Out-of-scope |
| **05 - 10 min** | **2. Scale & Estimations** | DAU, QPS (Read/Write), Bandwidth, Storage over 5 years, Cache sizing |
| **10 - 15 min** | **3. API & Data Model** | REST/gRPC contracts, Schema design, Primary & Sharding keys |
| **15 - 30 min** | **4. High-Level Architecture** | Core components, Data flow, Caching, Asynchronous workers |
| **30 - 45 min** | **5. Deep-Dive & SDE-III Edge Cases**| Bottlenecks, Failures, Concurrency, Hot partitions, Replication lag |

---

## Step-by-Step Template

### 1. Requirements Gathering & Scoping
* **Functional Requirements (FR)**:
  - Top 3–4 essential user journeys (e.g., *1. Post a tweet, 2. View user timeline, 3. Search tweets*).
* **Non-Functional Requirements (NFR)**:
  - **Availability vs Consistency (CAP)**: Highly available (99.99%) with eventual consistency, or strong read-after-write consistency?
  - **Latency**: P99 read < 50ms, P99 write < 200ms.
  - **Durability**: Zero data loss for transactional data.
* **Out of Scope**:
  - Analytics pipeline, AI recommendations (unless specifically requested).

---

### 2. Back-of-the-Envelope Calculations
* **Traffic**:
  - Daily Active Users (DAU) = $N$
  - Read QPS = $\frac{\text{Reads/day}}{86,400}$ (Peak = $2\times$ to $3\times$ Average QPS)
  - Write QPS = $\frac{\text{Writes/day}}{86,400}$
* **Storage**:
  - Write size per item = $S$ bytes
  - Daily storage = $\text{Write QPS} \times 86,400 \times S$
  - 5-Year Storage = $\text{Daily Storage} \times 365 \times 5$
* **Memory & Caching (80/20 Rule)**:
  - Cache 20% of daily read traffic.
  - Cache RAM required = $0.20 \times \text{Daily Reads} \times \text{Payload Size}$.

---

### 3. API Design & Data Modeling
* **API Endpoints**:
  - `POST /api/v1/resource` -> `{ status: 201, id: "..." }`
  - `GET /api/v1/resource/{id}` -> `{ ... }`
* **Data Store Selection**:
  - **Relational (PostgreSQL/MySQL)**: Complex relationships, ACID transactions, strict schema.
  - **NoSQL Document / KV (DynamoDB / Cassandra / Redis)**: Massive horizontal scale, high write throughput, predictable key-based lookups.
* **Schema Definition**:
  - Entities, Foreign keys, Indexing strategy, Partitioning Key (`PK`) & Sort Key (`SK`).

---

### 4. High-Level Component Diagram
* Client (Mobile/Web) -> CDN / DNS -> API Gateway (Rate Limiter, Auth, SSL Termination)
* Application Microservices (Stateless)
* Caching Layer (Redis / Memcached cluster with LRU)
* Database (Primary-Replica or Multi-Master with Sharding)
* Async Message Queue (Kafka / RabbitMQ / AWS SQS) -> Consumer Workers -> Object Storage (S3)

---

### 5. SDE-III Deep-Dive & Trade-offs
* **Partitioning & Sharding Strategy**:
  - Hash-based partitioning vs Range-based.
  - How to handle the **Celebrity / Hot Key Problem** (e.g., Elon Musk with 150M followers)?
* **Cache Invalidation & Consistency**:
  - Cache-Aside vs Write-Through vs Write-Behind.
  - Thundering Herd problem prevention (Distributed Mutex / Cache warming).
* **Fault Tolerance & Disaster Recovery**:
  - Leader election & Consensus (Raft / Paxos / ZooKeeper).
  - Cross-region replication (Active-Active vs Active-Passive).
  - Circuit Breakers (Hystrix / Resilience4j pattern) and Graceful Degradation.
