# System Design Architecture: Design Collaborative Document Editor (Google Docs)

## 1. Requirements & Scope
- **Functional Requirements**: Core user workflows and contracts.
- **Non-Functional Requirements**: High availability, P99 latency goals, consistency trade-offs.

---

## 2. Scale & Back-of-the-Envelope Estimation
- **SCALE**: 50 active concurrent editors on the same document, typing 10 keystrokes/sec each
- **LATENCY**: Real-time sync latency < 50ms across global participants
- **OFFLINE**: Support offline editing with seamless reconciliation on reconnect

---

## 3. API Contracts & Data Schema
### API Endpoints
- `WebSocket ws://docs.domain.com/session/{doc_id} -> Stream binary operations`
- `Operation Contract: { op_id: string, author_id: string, revision: int, type: 'INSERT'|'DELETE', position: int, char: string }`

### Data Schema
```sql
Document Snapshot Store:
- doc_id: UUID PK
- base_snapshot: TEXT
- revision_number: BIGINT

Operation Log:
- doc_id: UUID (Partition Key)
- revision: BIGINT (Clustering Key)
- operation: JSON
- timestamp: TIMESTAMP
```

---

## 4. High-Level System Architecture
```mermaid
graph TD
    UserA[Alice (WebSocket)] --> DocServer[Collaboration Gateway]
    UserB[Bob (WebSocket)] --> DocServer
    DocServer --> OT_Engine[OT Transform Engine & Sequencer]
    OT_Engine --> MemoryBuffer[In-Memory Doc Revision State]
    MemoryBuffer --> OpLog[(Operation Log - Redis/Cassandra)]
    MemoryBuffer --> SnapshotStore[(Doc Snapshots - S3 / PostgreSQL)]
```

---

## 5. SDE-III Deep Dives & Bottlenecks
### **Operational Transformation (OT) vs CRDT**: Google Docs historically uses Operational Transformation (server is central sequencer). CRDTs (Conflict-free Replicated Data Types, e.g. Yjs / Automerge) are peer-to-peer and require no central lock, but have higher memory overhead.

### **Transform Function**: If Alice inserts 'X' at pos 3 while Bob inserts 'Y' at pos 2, server transforms Alice's operation from pos 3 to pos 4 (`T(opA, opB) -> opA'`) so characters don't overwrite each other.

### **Snapshot Compaction**: Storing millions of individual character operations causes slow document opening. Periodically compact past operations into full document snapshots every 500 revisions.

---

## 6. Interview Checklist
- [ ] Explained tradeoffs between SQL vs NoSQL for this specific data access pattern
- [ ] Addressed single points of failure (SPOF) with redundancy
- [ ] Solved caching stampede / hot partition challenges
- [ ] Defined metric observability and disaster recovery plan
