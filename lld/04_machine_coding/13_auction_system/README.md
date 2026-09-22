# Machine Coding: Online Auction / Bidding System
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Users can create auctions with reserve price and duration.
- Users place bids; each bid must be higher than current highest.
- Close auction and declare winner when timer expires.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Thread-safe concurrent bids handling without race conditions.
- Sniper protection: Bids in the last 30 seconds extend auction by 1 minute.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
