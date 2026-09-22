# SDE-III LLD & HLD Mastery: Personalized Mentor & Tracker

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Track Progress](https://img.shields.io/badge/Interactive%20Tracker-index.html-brightgreen)](./index.html)
[![Target Role](https://img.shields.io/badge/Level-SDE--III%20%2F%20Staff%20Engineer-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A personalized, production-grade repository designed to take you from foundational system concepts to **SDE-III / Staff Software Engineer** mastery in both **Low-Level Design (Python)** and **High-Level Distributed Systems Design**.

---

## 📑 Table of Contents
1. [What Separates SDE-II from SDE-III?](#-what-separates-sde-ii-from-sde-iii)
2. [Interactive Progress Dashboard (`index.html`)](#-interactive-progress-dashboard-indexhtml)
3. [Low-Level Design (LLD) Curriculum](#-low-level-design-lld-python)
   - [SOLID Principles](#1-solid-principles-in-python)
   - [Core Design Patterns](#2-gof-design-patterns)
   - [Concurrency & Thread Safety](#3-concurrency--multithreading)
   - [15 Machine Coding Problem Bank](#4-15-curated-sde-iii-machine-coding-problems)
4. [High-Level Design (HLD) Curriculum](#-high-level-system-design-hld)
   - [Distributed Systems Fundamentals](#1-distributed-fundamentals)
   - [Core Building Blocks](#2-core-building-blocks)
   - [10 End-to-End System Design Case Studies](#3-10-end-to-end-system-design-case-studies)
5. [SDE-III Python Engineering Standards](#-sde-iii-python-engineering-standards)
6. [Interactive Mentorship Workflow](#-interactive-mentorship-workflow)

---

## 🎯 What Separates SDE-II from SDE-III?

| Evaluation Dimension | SDE-II Expectation | SDE-III / Staff Engineer Bar |
| :--- | :--- | :--- |
| **LLD Architecture** | Can write code that runs and implements basic OOP. | Writes modular, loosely coupled code (SOLID) extensible via design patterns (Strategy, Factory, State) without modifying existing classes. |
| **Concurrency & Thread Safety** | Mentions locks or basic threads without depth. | Identifies race conditions, starvation, deadlocks; designs thread-safe domain entities with fine-grained locking (`RLock`, `Condition`) or lock-free concurrency. |
| **Typing & Clean Code** | Standard dynamic code. | Strict type hinting (`typing`, `Protocol`, `ABC`), custom domain exceptions, immutable value objects (`@dataclass(frozen=True)`). |
| **HLD Scope Leadership** | Follows standard tutorial diagrams (Web server -> DB). | Proactively drives trade-offs (CAP, consistency models, partition keys, hot keys, replication lag, blast radius, failure modes, cost). |
| **Resilience & Production** | Assumes the network and components never fail. | Designs circuit breakers, rate limiters, dead-letter queues, idempotent retry policies, and observability (metrics/distributed tracing). |

---

## 🚀 Interactive Progress Dashboard (`index.html`)

The repository includes a single-page, zero-dependency, dark-mode tracking web app built with modern CSS glassmorphism and local storage persistence.

```bash
# Launch directly in your browser on macOS
open index.html
```

### Dashboard Highlights:
- 📈 **Real-Time SDE-III Readiness Metric**: Automatically computes your overall mastery index across all LLD & HLD modules.
- 🔍 **Instant Search & Filter**: Real-time filtering across LLD Machine Coding, Design Patterns, HLD Case Studies, and Fundamentals.
- ⭐ **Confidence & Status Tracker**: Track status (*Not Started*, *In Progress*, *Solved*, *Needs Revision*) and rate confidence from 1 to 5 stars.
- 📝 **Architectural Notes & Rubric Drawer**: Save design trade-offs, edge cases, and personal learnings per problem (stored in `localStorage`).
- 💾 **Data Backup**: Export and Import your tracking progress via JSON anytime.

---

## 📐 Low-Level Design (LLD) [Python]

### 1. SOLID Principles in Python
- [Single Responsibility Principle (SRP)](./lld/01_solid_principles/01_single_responsibility/README.md)
- [Open/Closed Principle (OCP)](./lld/01_solid_principles/02_open_closed/README.md)
- [Liskov Substitution Principle (LSP)](./lld/01_solid_principles/03_liskov_substitution/README.md)
- [Interface Segregation Principle (ISP)](./lld/01_solid_principles/04_interface_segregation/README.md)
- [Dependency Inversion Principle (DIP)](./lld/01_solid_principles/05_dependency_inversion/README.md)

### 2. GoF Design Patterns
- [Strategy Pattern](./lld/02_design_patterns/01_strategy/README.md)
- [Factory & Abstract Factory](./lld/02_design_patterns/02_factory/README.md)
- [Observer / Event Bus](./lld/02_design_patterns/03_observer/README.md)
- [Decorator Pattern](./lld/02_design_patterns/04_decorator/README.md)
- [State Pattern & FSM](./lld/02_design_patterns/05_state/README.md)
- [Chain of Responsibility](./lld/02_design_patterns/06_chain_of_responsibility/README.md)
- [Builder Pattern](./lld/02_design_patterns/07_builder/README.md)
- [Adapter & Facade Pattern](./lld/02_design_patterns/08_adapter_facade/README.md)

### 3. Concurrency & Multithreading
- [Locks, Deadlocks & Thread-Safety](./lld/03_concurrency/01_locks_and_deadlocks/README.md)
- [Producer-Consumer with Condition Variables](./lld/03_concurrency/02_producer_consumer/README.md)
- [Custom Thread Pool & Worker Queues](./lld/03_concurrency/03_thread_pool/README.md)

### 4. 15 Curated SDE-III Machine Coding Problems

Each problem includes requirements, edge cases, SDE-III rubrics, and a typed Python starter file:

| # | Problem | Difficulty | Key Patterns / Focus | Folder | Starter Code |
|---|---|---|---|---|---|
| **01** | Multilevel Parking Lot | `Hard` | Strategy (Fee & Allocation), Concurrency | [README](./lld/04_machine_coding/01_parking_lot/README.md) | [solution.py](./lld/04_machine_coding/01_parking_lot/solution.py) |
| **02** | Splitwise / Expense Sharing | `Hard` | Strategy, Debt Simplification Graph | [README](./lld/04_machine_coding/02_splitwise/README.md) | [solution.py](./lld/04_machine_coding/02_splitwise/solution.py) |
| **03** | Distributed Rate Limiter | `SDE-III Bar Raiser` | Token Bucket, Sliding Window, Thread Safety | [README](./lld/04_machine_coding/03_rate_limiter/README.md) | [solution.py](./lld/04_machine_coding/03_rate_limiter/solution.py) |
| **04** | In-Memory LRU & LFU Cache | `Hard` | Doubly Linked List, $O(1)$ Operations, RLock | [README](./lld/04_machine_coding/04_lru_lfu_cache/README.md) | [solution.py](./lld/04_machine_coding/04_lru_lfu_cache/solution.py) |
| **05** | Elevator Control System | `Hard` | State Pattern, LOOK/SCAN Dispatcher | [README](./lld/04_machine_coding/05_elevator_system/README.md) | [solution.py](./lld/04_machine_coding/05_elevator_system/solution.py) |
| **06** | Notification Service | `Medium` | Observer, Decorator (RateLimit, Retry) | [README](./lld/04_machine_coding/06_notification_service/README.md) | [solution.py](./lld/04_machine_coding/06_notification_service/solution.py) |
| **07** | BookMyShow (Seat Booking) | `SDE-III Bar Raiser` | Pessimistic/Optimistic Seat Locks, TTL Expiry | [README](./lld/04_machine_coding/07_bookmyshow/README.md) | [solution.py](./lld/04_machine_coding/07_bookmyshow/solution.py) |
| **08** | Cricbuzz / Live Score Tracker | `Hard` | Observer, Ball-by-ball State Machine | [README](./lld/04_machine_coding/08_cricbuzz/README.md) | [solution.py](./lld/04_machine_coding/08_cricbuzz/solution.py) |
| **09** | Task Scheduler / Cron Engine | `SDE-III Bar Raiser` | PriorityQueue, Worker Pool, Condition Variables | [README](./lld/04_machine_coding/09_task_scheduler/README.md) | [solution.py](./lld/04_machine_coding/09_task_scheduler/solution.py) |
| **10** | Logging Framework (Log4j-lite)| `Medium` | Chain of Responsibility, Async Sink Queue | [README](./lld/04_machine_coding/10_logging_framework/README.md) | [solution.py](./lld/04_machine_coding/10_logging_framework/solution.py) |
| **11** | Chess Game Engine | `Hard` | Command Pattern, Move Undo/Redo Stack | [README](./lld/04_machine_coding/11_chess/README.md) | [solution.py](./lld/04_machine_coding/11_chess/solution.py) |
| **12** | Vending Machine | `Medium` | State Pattern, Coin Denomination Greedy | [README](./lld/04_machine_coding/12_vending_machine/README.md) | [solution.py](./lld/04_machine_coding/12_vending_machine/solution.py) |
| **13** | Online Auction / Bidding | `Hard` | Observer, Concurrency Lock, Timer Snipe | [README](./lld/04_machine_coding/13_auction_system/README.md) | [solution.py](./lld/04_machine_coding/13_auction_system/solution.py) |
| **14** | Snake and Ladder Game | `Medium` | Strategy (Dice), Circular Queue | [README](./lld/04_machine_coding/14_snake_ladder/README.md) | [solution.py](./lld/04_machine_coding/14_snake_ladder/solution.py) |
| **15** | Pub-Sub Messaging Broker | `SDE-III Bar Raiser` | Consumer Groups, Topic Offsets, Async Workers | [README](./lld/04_machine_coding/15_pub_sub/README.md) | [solution.py](./lld/04_machine_coding/15_pub_sub/solution.py) |

---

## 🏛️ High-Level System Design (HLD)

### 1. Distributed Fundamentals
- [CAP & PACELC Trade-Offs](./hld/01_fundamentals/01_cap_and_pacelc/README.md)
- [Database Sharding & Partitioning Strategies](./hld/01_fundamentals/02_sharding_and_partitioning/README.md)
- [Caching Strategies & Thundering Herd Mitigation](./hld/01_fundamentals/03_caching_and_thundering_herd/README.md)
- [Replication & Consistency Models](./hld/01_fundamentals/04_replication_and_consistency/README.md)

### 2. Core Building Blocks
- [Distributed Rate Limiter](./hld/02_building_blocks/01_distributed_rate_limiter/README.md)
- [Distributed Cache Architecture](./hld/02_building_blocks/02_distributed_cache/README.md)
- [Distributed Locks (Redlock vs ZooKeeper)](./hld/02_building_blocks/03_distributed_lock/README.md)
- [Distributed 64-bit Unique ID Generator (Snowflake)](./hld/02_building_blocks/04_unique_id_generator/README.md)
- [Distributed Message Queue Architecture](./hld/02_building_blocks/05_message_queue/README.md)

### 3. 10 End-to-End System Design Case Studies

Each case study contains an architectural blueprint (`design.md`) with capacity calculations, API contracts, schemas, Mermaid component diagrams, and SDE-III trade-off deep dives:

| # | System Design System | Scale & Throughput | Key SDE-III Architecture Focus | Architecture Blueprint |
|---|---|---|---|---|
| **01** | URL Shortener (TinyURL) | 100M writes/mo, 10B reads/mo | Base62 vs KGS, 301 vs 302 redirect, Cache-Aside | [design.md](./hld/03_case_studies/01_tinyurl/design.md) |
| **02** | Ride-Sharing (Uber / Lyft) | 5M drivers emitting GPS / 4s | Uber H3 Hexagonal indexing, Kafka ingestion, matching lock | [design.md](./hld/03_case_studies/02_uber/design.md) |
| **03** | Real-Time Chat (WhatsApp) | 100B msgs/day, 2B DAU | WebSocket session registry, Cassandra queues, group fanout | [design.md](./hld/03_case_studies/03_whatsapp/design.md) |
| **04** | Video Streaming (YouTube) | 500 hrs uploaded/min | Asynchronous DAG transcoding, HLS adaptive bitrate, Multi-tier CDN | [design.md](./hld/03_case_studies/04_youtube_netflix/design.md) |
| **05** | Distributed Commit Log (Kafka) | Millions events/sec | Page cache sequential append, `sendfile` zero-copy, ISR replication | [design.md](./hld/03_case_studies/05_kafka/design.md) |
| **06** | Payment Gateway (Stripe) | 100% financial correctness | Idempotency keys, Double-entry ledger, Saga orchestrator | [design.md](./hld/03_case_studies/06_payment_gateway/design.md) |
| **07** | Flash Sale (Amazon/Flipkart) | 500k QPS, 1000 items | Atomic Redis Lua decrement, virtual waiting room, async orders | [design.md](./hld/03_case_studies/07_flash_sale/design.md) |
| **08** | Collaborative Docs (Google Docs) | Multi-editor real-time sync | Operational Transformation vs CRDT, vector clocks, snapshots | [design.md](./hld/03_case_studies/08_google_docs/design.md) |
| **09** | Distributed Web Crawler | 1B pages/month | URL Frontier politeness queues, Bloom filter & SimHash deduplication | [design.md](./hld/03_case_studies/09_web_crawler/design.md) |
| **10** | Distributed Metrics (Datadog) | 10M metrics/sec | Time-Series DB, Gorilla delta-of-delta compression, rollups | [design.md](./hld/03_case_studies/10_monitoring_datadog/design.md) |

---

## 🐍 SDE-III Python Engineering Standards

When solving machine coding problems in this repo, adopt the blueprint in [`templates/lld_template.py`](./templates/lld_template.py):

1. **Strict Type Annotations**: Use `typing.List`, `typing.Dict`, `typing.Optional`, and `typing.Protocol` or `abc.ABC`.
2. **Value Objects**: Use `@dataclass(frozen=True)` for immutable entities (e.g., `EntityId`, `Money`, `Coordinates`).
3. **Open-Closed Principle (OCP)**: Never write monolithic `if/elif/else` branching on types. Use Strategy / Factory patterns.
4. **Concurrency & Thread Safety**: Protect mutable shared state with `threading.RLock()` or atomic queues.
5. **Custom Exceptions**: Never raise generic `Exception`. Always declare domain-specific errors (e.g., `ResourceNotFoundException`, `InvalidOperationException`).

---

## 💡 Interactive Mentorship Workflow

When practicing with your AI mentor in chat:
1. **Pick a Topic / Problem**: Say *"Let's do Parking Lot LLD"* or *"Let's design Uber HLD"*.
2. **Interactive Mock Interview**:
   - I act as an **SDE-III Bar Raiser Interviewer**.
   - Clarify Functional & Non-Functional requirements.
   - Propose data models and class relationships.
   - Review your Python machine coding implementation line-by-line for production readiness.
   - Challenge you on edge cases, concurrent race conditions, and scalability bottlenecks.
3. **Log Your Progress**:
   - Open [`index.html`](./index.html), mark the problem status, rate your confidence (1–5 stars), and record your key learnings in the Notes drawer.
