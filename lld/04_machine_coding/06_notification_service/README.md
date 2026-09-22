# Machine Coding: Multi-Channel Notification Service
**Difficulty**: `Medium` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Send notifications via SMS, Email, and Push.
- Support user notification preferences and opt-outs.
- Support message templates with variable interpolation.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Decorator pattern for retries with exponential backoff and rate limiting.
- Pluggable provider strategies (Twilio, SendGrid, FCM).

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
