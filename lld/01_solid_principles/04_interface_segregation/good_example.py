"""
Interface Segregation Principle (ISP) - SDE-III REFACTORED
Clients should not be forced to depend upon interfaces that they do not use.
Fine-grained, decoupled protocols.
"""

from typing import Protocol


class Printer(Protocol):
    def print_doc(self, doc: str) -> None:
        ...


class Scanner(Protocol):
    def scan_doc(self, doc: str) -> str:
        ...


class FaxMachine(Protocol):
    def fax_doc(self, doc: str, number: str) -> None:
        ...


# Simple device only implements Printer
class EconomyPrinter:
    def print_doc(self, doc: str) -> None:
        print(f"[EconomyPrinter] Printing: {doc}")


# Enterprise all-in-one device implements both Printer and Scanner
class AllInOneOfficeHub:
    def print_doc(self, doc: str) -> None:
        print(f"[AllInOneHub] High-speed laser printing: {doc}")

    def scan_doc(self, doc: str) -> str:
        print(f"[AllInOneHub] Scanning high-resolution digital image: {doc}")
        return f"scanned_data_of_{doc}"


def print_batch(printer: Printer, docs: list[str]) -> None:
    for doc in docs:
        printer.print_doc(doc)


if __name__ == "__main__":
    economy = EconomyPrinter()
    enterprise = AllInOneOfficeHub()

    # Both work seamlessly where only a Printer is needed!
    print_batch(economy, ["Invoice1.pdf"])
    print_batch(enterprise, ["Contract.pdf"])
