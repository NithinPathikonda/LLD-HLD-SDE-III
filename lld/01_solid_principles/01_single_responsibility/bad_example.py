"""
Single Responsibility Principle (SRP) - ANTI-PATTERN (VIOLATION)
The 'God Class' UserManager handles:
1. User domain representation
2. Password hashing & cryptographic operations
3. Database persistence (SQL generation)
4. Email notification dispatch
"""

class UserManager:
    def __init__(self, username: str, email: str, raw_password: str) -> None:
        self.username = username
        self.email = email
        self.raw_password = raw_password

    def hash_password(self) -> str:
        # Cryptography reason to change
        return f"hashed_{self.raw_password}_salt_123"

    def save_to_database(self) -> None:
        # Database / SQL schema reason to change
        hashed = self.hash_password()
        sql = f"INSERT INTO users (username, email, password) VALUES ('{self.username}', '{self.email}', '{hashed}')"
        print(f"[DB] Executing SQL: {sql}")

    def send_welcome_email(self) -> None:
        # Email formatting / SMTP protocol reason to change
        print(f"[EMAIL] Connecting to smtp.mail.com:587...")
        print(f"[EMAIL] To: {self.email} -> Welcome to the platform, {self.username}!")


if __name__ == "__main__":
    print("--- Running SRP Violation ---")
    user_mgr = UserManager("john_doe", "john@example.com", "secretPassword")
    user_mgr.save_to_database()
    user_mgr.send_welcome_email()
