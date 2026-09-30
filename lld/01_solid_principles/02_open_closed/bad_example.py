"""
Open/Closed Principle (OCP) - ANTI-PATTERN (VIOLATION)
Violating OCP by using if/elif/else chains checking payment types.
Adding a new payment method (e.g. Crypto) requires modifying existing class code!
"""

class PaymentProcessor:
    def process_payment(self, payment_type: str, amount: float) -> None:
        if payment_type == "CREDIT_CARD":
            print(f"[CARD] Charging ${amount:.2f} via Payment Gateway API.")
        elif payment_type == "UPI":
            print(f"[UPI] Initiating UPI intent for ${amount:.2f}.")
        elif payment_type == "PAYPAL":
            print(f"[PAYPAL] Redirecting to PayPal OAuth for ${amount:.2f}.")
        else:
            raise ValueError(f"Unsupported payment type: {payment_type}")


if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.process_payment("CREDIT_CARD", 100.0)
    processor.process_payment("UPI", 50.0)
