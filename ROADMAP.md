# 12-Week SDE-3 Mastery Roadmap (Tailored for 2 YoE Engineers)

> **Profile**: Software Engineer with ~2 years of experience (SDE-1 / early SDE-2).
> **Goal**: Solidify fundamental engineering mental models, eliminate superficial knowledge, and bridge the gap to **SDE-III / Staff Software Engineer** in both Low-Level Design (Python) and High-Level Distributed Systems.

---

## 🧭 The 2 YoE Trap (and How to Beat It)

At 2 years of experience, most engineers fall into one of two traps:
1. **In LLD**: Writing functional procedural code inside classes (God objects, tight coupling, hardcoded conditionals) without understanding *why* design patterns exist or how to write extensible, thread-safe software.
2. **In HLD**: Memorizing architecture diagrams (e.g., "Web server -> Redis -> Postgres") without knowing the underlying mechanics (e.g., *Why did we pick LSM-tree over B-Tree? What happens during network split-brain? Why does Redlock fail without fencing tokens?*).

This roadmap builds your knowledge from **first principles** up to Staff-level trade-offs.

---

## 🗓️ Phase 1: Object-Oriented & Python Deep Fundamentals (Weeks 1 – 2)

**Focus**: Clean Python OOP, modern typing, and the 5 SOLID principles.

- **Day 1–3: Python OOP & Typing Mastery**
  - Read & practice [`lld/00_oop_foundations/`](./lld/00_oop_foundations/README.md).
  - Understand `typing.Protocol` (duck-typing contracts) vs `abc.ABC` (nominal typing).
  - Understand Value Objects vs Entities: `@dataclass(frozen=True)` with custom `__hash__` and `__eq__`.
  - Composition over Inheritance: Why deep class hierarchies create fragile code.
- **Day 4–7: S.O.L.I.D. Deep Dive**
  - Read & implement each principle in [`lld/01_solid_principles/`](./lld/01_solid_principles/README.md).
  - Single Responsibility: Separating business logic, persistence, and external APIs.
  - Open/Closed: Eliminating `if/elif/else` type checks via Strategy pattern.
  - Liskov Substitution: Never raising `NotImplementedError` in a subclass.
- **Week 2: Concurrency & Thread-Safety in Python**
  - Study [`lld/03_concurrency/`](./lld/03_concurrency/01_locks_and_deadlocks/README.md).
  - The Python GIL (Global Interpreter Lock): When does threading help (I/O) vs multiprocessing (CPU)?
  - Mutex (`threading.Lock`) vs Reentrant Lock (`threading.RLock`).
  - Condition Variables (`threading.Condition`) and the Producer-Consumer pattern.

---

## 🗓️ Phase 2: Design Patterns for Machine Coding (Weeks 3 – 4)

**Focus**: The 8 design patterns that appear in 95% of machine coding rounds.

- **Week 3: Behavioral Patterns**
  - **Strategy Pattern**: Dynamic pricing, fee calculators, discount engines.
  - **Observer Pattern**: Event buses, real-time push score engines (Cricbuzz).
  - **State Pattern**: Finite state machines for orders, vending machines, elevators.
  - **Chain of Responsibility**: Middleware, logging filters, request validators.
- **Week 4: Creational & Structural Patterns**
  - **Factory & Self-Registering Factory**: Pluggable object creation with Python decorators.
  - **Decorator Pattern**: Reusable caching, retry logic with backoff, and metrics middleware.
  - **Builder Pattern**: Complex immutable object construction (queries, configs).
  - **Adapter / Facade**: Integrating external legacy APIs cleanly.

---

## 🗓️ Phase 3: LLD Machine Coding Intensive (Weeks 5 – 7)

**Focus**: Timed 60–90 minute problem solving from scratch.

- **Week 5: Resource Management & Allocation Systems**
  - 🚗 [Multilevel Parking Lot](./lld/04_machine_coding/01_parking_lot/README.md)
  - 🛗 [Elevator Dispatch System](./lld/04_machine_coding/05_elevator_system/README.md)
  - 🍫 [Vending Machine System](./lld/04_machine_coding/12_vending_machine/README.md)
- **Week 6: High-Concurrency & Rate-Limiting Systems**
  - ⚡ [Distributed Rate Limiter (Token / Sliding Window)](./lld/04_machine_coding/03_rate_limiter/README.md)
  - 💾 [In-Memory LRU & LFU Cache](./lld/04_machine_coding/04_lru_lfu_cache/README.md)
  - ⏱️ [Distributed Task Scheduler / Cron Engine](./lld/04_machine_coding/09_task_scheduler/README.md)
- **Week 7: Financial & Game Engines**
  - 💸 [Splitwise / Expense Sharing App](./lld/04_machine_coding/02_splitwise/README.md)
  - 🎟️ [BookMyShow Seat Reservation with Locks](./lld/04_machine_coding/07_bookmyshow/README.md)
  - ♟️ [Chess Game Engine with Undo/Redo](./lld/04_machine_coding/11_chess/README.md)

---

## 🗓️ Phase 4: Distributed Systems Fundamentals (Weeks 8 – 9)

**Focus**: The underlying plumbing of high-scale systems.

- **Week 8: Networking, Databases & Storage Internals**
  - **Protocols**: TCP vs UDP, HTTP/1.1 vs HTTP/2 vs HTTP/3, WebSockets vs gRPC vs SSE.
  - **Storage Engines**: B-Tree (PostgreSQL/MySQL) vs LSM-Tree (Cassandra, RocksDB).
  - **Database Indexes**: Clustered vs Non-clustered, composite index leftmost prefix rule.
  - **ACID & Isolation Levels**: Dirty reads, phantom reads, Repeatable Read vs Serializable.
- **Week 9: Distributed Trade-offs & Consistency**
  - **CAP & PACELC**: Why network partitions are inevitable; latency vs consistency trade-offs.
  - **Sharding & Partitioning**: Hash-based vs range-based; handling hot keys.
  - **Caching Mechanics**: Cache-Aside, Write-Through, Write-Behind, Thundering herd & XFetch.
  - **Distributed Locks**: Redlock algorithm, Martin Kleppmann's critique, and fencing tokens.

---

## 🗓️ Phase 5: End-to-End High-Level Design (Weeks 10 – 12)

**Focus**: 45-Minute SDE-III system design interview execution using [`templates/hld_framework.md`](./templates/hld_framework.md).

- **Week 10: High-Throughput & Real-Time Ingestion**
  - 🔗 [Design TinyURL (Read-Heavy Cache-Aside)](./hld/03_case_studies/01_tinyurl/design.md)
  - 🚕 [Design Uber (Geospatial Indexing H3 / QuadTree)](./hld/03_case_studies/02_uber/design.md)
  - 💬 [Design WhatsApp (WebSockets & Cassandra queues)](./hld/03_case_studies/03_whatsapp/design.md)
- **Week 11: Streaming & Append-Only Logs**
  - 🎥 [Design YouTube / Netflix (Chunked Transcoding & CDN)](./hld/03_case_studies/04_youtube_netflix/design.md)
  - 🪵 [Design Kafka-lite (Page Cache & Zero-Copy Reads)](./hld/03_case_studies/05_kafka/design.md)
  - 🕷️ [Design Web Crawler (URL Frontier & Politeness)](./hld/03_case_studies/09_web_crawler/design.md)
- **Week 12: Mission-Critical Financial Systems & SDE-III Bar Raiser**
  - 💳 [Design Stripe-lite Payment Gateway (Idempotency & Double-Entry Ledger)](./hld/03_case_studies/06_payment_gateway/design.md)
  - 🛍️ [Design Flash Sale System (Atomic Redis Lua Decrement)](./hld/03_case_studies/07_flash_sale/design.md)
  - 📝 [Design Google Docs (Operational Transformation vs CRDT)](./hld/03_case_studies/08_google_docs/design.md)

---

## 📊 Daily Study Routine (1.5 – 2 Hours / Day)

| Time | Activity | Output |
| :--- | :--- | :--- |
| **00 – 15 min** | Review previous day's concept on [index.html](./index.html) | Spaced repetition check |
| **15 – 75 min** | Active coding / design drafting | Write Python code or draw architecture |
| **75 – 90 min** | Code Review & Notes Logging | Record mistakes, edge cases, and rate confidence |
