"""
Dependency Inversion Principle (DIP) - ANTI-PATTERN (VIOLATION)
High-level OrderProcessor directly instantiates low-level concrete dependencies
(MySQLDatabase & TwilioSMSGateway).
Tightly coupled: Impossible to unit test without spinning up live MySQL and Twilio!
"""

class MySQLDatabase:
    def insert_order(self, order_id: str, amount: float) -> None:
        print(f"[MySQL] INSERT INTO orders VALUES ('{order_id}', {amount});")


class TwilioSMSGateway:
    def send_sms(self, phone: str, text: str) -> None:
        print(f"[Twilio] Sending SMS via live REST API to {phone}: {text}")


class OrderProcessor:
    def __init__(self) -> None:
        # VIOLATION: Hardcoded concrete dependencies!
        self.db = MySQLDatabase()
        self.sms = TwilioSMSGateway()

    def checkout(self, order_id: str, customer_phone: str, amount: float) -> None:
        self.db.insert_order(order_id, amount)
        self.sms.send_sms(customer_phone, f"Order {order_id} confirmed for ${amount:.2f}")


if __name__ == "__main__":
    processor = OrderProcessor()
    processor.checkout("ORD-999", "+1-555-0199", 89.99)
