# SDE-III LLD Machine Coding Problem Bank (Python)

These 15 machine coding problems represent 95%+ of all LLD interview scenarios at top-tier companies (Uber, Google, Amazon, Atlassian, Swiggy, Flipkart, PhonePe, Microsoft).

---

### Machine Coding Problems Matrix

| # | Problem | Core Patterns / Techniques | Key SDE-III Challenge |
|---|---|---|---|
| **01** | [Parking Lot](./01_parking_lot/) | Strategy (Fee, Spot allocation), Factory | Multi-floor concurrency, vehicle-spot size compatibility |
| **02** | [Splitwise / Expense Sharing](./02_splitwise/) | Strategy (Equal, Exact, % split), Graph | Debt simplification algorithm, currency handling |
| **03** | [Distributed Rate Limiter](./03_rate_limiter/) | Token Bucket, Leaky Bucket, Sliding Window Log | High throughput, atomic increment, window eviction |
| **04** | [In-Memory Cache (LRU / LFU)](./04_cache/) | Doubly Linked List + HashMap, Min-Heap | $O(1)$ operations, thread-safe eviction policies |
| **05** | [Elevator Control System](./05_elevator/) | State Pattern, Strategy (LOOK/SCAN dispatch) | Multiple elevators, direction scheduling, overload safety |
| **06** | [Notification Service](./06_notification_service/) | Observer, Strategy, Decorator (Rate-limiting, Retry) | Channel abstraction (Email/SMS/Push), batching, idempotency |
| **07** | [BookMyShow / Movie Booking](./07_bookmyshow/) | Concurrency Lock, State Pattern | Race condition on seat locks with 10-min reservation timeout |
| **08** | [Cricbuzz / Live Score Tracker](./08_cricbuzz/) | Observer Pattern, Strategy | Real-time event streaming, ball-by-ball state machine |
| **09** | [Task Scheduler / Cron Engine](./09_task_scheduler/) | PriorityQueue, Worker Pool, Producer-Consumer | Delayed tasks, recurring cron execution, graceful shutdown |
| **10** | [Logging Framework (Log4j-lite)](./10_logging_framework/) | Chain of Responsibility, Singleton, Sink Strategy | Async buffer queue, log levels, file/console flush |
| **11** | [Chess / Board Game](./11_chess/) | Command Pattern, Factory, State | Move validation, checkmate detection, undo/redo stack |
| **12** | [Vending Machine](./12_vending_machine/) | State Pattern | State transitions (Idle -> HasMoney -> Dispensing -> SoldOut) |
| **13** | [Online Auction / Bidding System](./13_auction_system/) | Observer Pattern, Optimistic Locking | Concurrent bids, timer expiration, auto-bid bot |
| **14** | [Snake and Ladder](./14_snake_ladder/) | Factory, Modular arithmetic, Dice Strategy | Configurable board, multiple players, crooked dice |
| **15** | [Pub-Sub Messaging Queue](./15_pub_sub/) | Observer, Publisher-Subscriber, Topic Router | Thread-safe consumer groups, message offset tracking |
