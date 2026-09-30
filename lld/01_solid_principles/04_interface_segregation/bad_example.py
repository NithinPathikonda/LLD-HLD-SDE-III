"""
Interface Segregation Principle (ISP) - ANTI-PATTERN (VIOLATION)
Fat interface forces clients to depend on methods they do not use.
"""

from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def print_doc(self, doc: str) -> None:
        pass

    @abstractmethod
    def scan_doc(self, doc: str) -> None:
        pass

    @abstractmethod
    def fax_doc(self, doc: str) -> None:
        pass


class SimplePrinter(Machine):
    def print_doc(self, doc: str) -> None:
        print(f"Printing: {doc}")

    def scan_doc(self, doc: str) -> None:
        # VIOLATION: SimplePrinter cannot scan
        raise NotImplementedError("Scan not supported!")

    def fax_doc(self, doc: str) -> None:
        # VIOLATION: SimplePrinter cannot fax
        raise NotImplementedError("Fax not supported!")


if __name__ == "__main__":
    printer = SimplePrinter()
    printer.print_doc("Resume.pdf")
    try:
        printer.scan_doc("Document.pdf")
    except NotImplementedError as e:
        print(f"[FAT INTERFACE ISSUE]: {e}")
