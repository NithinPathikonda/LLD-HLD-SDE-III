# Database Internals: Storage Engines, Indexes & ACID Isolation

> **Must-Know Fundamentals**: How databases actually store, index, and lock data on disk and in memory.

---

## 1. Storage Engines: B-Tree vs LSM-Tree

| Dimension | B-Tree (PostgreSQL, MySQL InnoDB) | LSM-Tree (Log-Structured Merge Tree: Cassandra, RocksDB) |
| :--- | :--- | :--- |
| **Write Mechanism** | Updates pages in-place on disk (requires random disk writes). | Appends sequentially to In-Memory MemTable + Write-Ahead Log (WAL). Flushes to disk as immutable SSTables. |
| **Write Performance** | Slower writes (random disk I/O, page splits). | 🚀 **Extremely fast writes** (100% sequential I/O). |
| **Read Performance** | 🚀 **Predictable & Fast reads** ($O(\log N)$ tree lookup). | Slower reads (must check MemTable + Bloom filters + multiple SSTables). |
| **Compaction** | Minor vacuuming/fragmentation cleanup. | Background compaction merges SSTables, causing CPU/I/O spikes. |
| **Ideal Workload** | Read-heavy workloads, OLTP relational databases. | Write-intensive workloads (Metrics, Event logs, Messaging queues). |

---

## 2. Database Indexes & Query Optimization

### Clustered vs Non-Clustered Index
- **Clustered Index**: Determines the physical order of data on disk. A table can only have **one** clustered index (usually the Primary Key).
- **Non-Clustered Index (Secondary Index)**: A separate B-tree structure holding indexed columns and a pointer (bookmark/PK) back to the actual row.
- **Index Covering Query**: When an index contains all columns requested by a `SELECT` statement, avoiding the secondary lookup (table scan / bookmark lookup) entirely.

### Composite Index: The Leftmost Prefix Rule
- If an index is on `(user_id, status, created_at)`:
  - `WHERE user_id = 5` -> ✅ Uses Index
  - `WHERE user_id = 5 AND status = 'ACTIVE'` -> ✅ Uses Index
  - `WHERE status = 'ACTIVE'` -> ❌ **Full Table Scan** (Leftmost column missing)

---

## 3. ACID Isolation Levels & Concurrency Anomalies

SQL standards define 4 isolation levels to manage concurrent transactions:

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Write Skew |
| :--- | :---: | :---: | :---: | :---: |
| **Read Uncommitted** | ⚠️ Allowed | ⚠️ Allowed | ⚠️ Allowed | ⚠️ Allowed |
| **Read Committed** (Default Postgres/Oracle) | 🛡️ Prevented | ⚠️ Allowed | ⚠️ Allowed | ⚠️ Allowed |
| **Repeatable Read** (Default MySQL InnoDB) | 🛡️ Prevented | 🛡️ Prevented | ⚠️ Allowed | ⚠️ Allowed |
| **Serializable** | 🛡️ Prevented | 🛡️ Prevented | 🛡️ Prevented | 🛡️ Prevented |

### Understanding the Anomalies:
1. **Dirty Read**: Transaction A reads uncommitted modifications made by Transaction B (which might later roll back).
2. **Non-Repeatable Read**: Transaction A reads row $X$. Transaction B updates row $X$ and commits. Transaction A re-reads row $X$ and sees different data.
3. **Phantom Read**: Transaction A queries rows matching a condition (`WHERE age > 30`). Transaction B inserts a new matching row and commits. Transaction A re-queries and sees a "phantom" row.
4. **Write Skew**: Two concurrent transactions read overlapping data, satisfy constraints independently, but their combined concurrent writes violate the business invariant (e.g., at least one doctor must remain on call). Prevented by **Serializable** or explicit `SELECT ... FOR UPDATE`.
