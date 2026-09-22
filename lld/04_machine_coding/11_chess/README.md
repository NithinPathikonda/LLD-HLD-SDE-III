# Machine Coding: Chess Game Engine
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Standard 8x8 chessboard with standard pieces.
- Validate legal moves for Pawn, Knight, Bishop, Rook, Queen, King.
- Detect check, checkmate, castling, and stalemate.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Command Pattern for move execution with full Undo/Redo history stack.
- Polymorphic Piece classes with clear boundary validation.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
