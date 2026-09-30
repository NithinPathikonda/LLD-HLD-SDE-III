"""
In-Memory Thread-Safe LRU & LFU Cache - SDE-III Machine Coding Solution
Algorithms:
1. LRU Cache: Doubly Linked List + Hash Map (Strict O(1) Get and Put).
2. LFU Cache: Hash Map + Frequency Doubly Linked Lists + min_frequency pointer (Strict O(1) Get and Put).
3. Thread-Safe Wrapper using threading.RLock.
"""

from __future__ import annotations
from dataclasses import dataclass
import threading
from typing import Dict, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


# ==============================================================================
# 1. DOUBLY LINKED LIST PRIMITIVES FOR O(1) EVICTION
# ==============================================================================

class Node(Generic[K, V]):
    def __init__(self, key: K, value: V, freq: int = 1) -> None:
        self.key: K = key
        self.value: V = value
        self.freq: int = freq
        self.prev: Optional[Node[K, V]] = None
        self.next: Optional[Node[K, V]] = None


class DoublyLinkedList(Generic[K, V]):
    def __init__(self) -> None:
        self.head: Node[K, V] = Node(None, None)  # Dummy head
        self.tail: Node[K, V] = Node(None, None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node[K, V]) -> None:
        node.next = self.head.next
        node.prev = self.head
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node[K, V]) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -= 1

    def remove_tail(self) -> Optional[Node[K, V]]:
        if self.size == 0 or not self.tail.prev or self.tail.prev is self.head:
            return None
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node


# ==============================================================================
# 2. LRU CACHE (STRICT O(1))
# ==============================================================================

class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        self._cache: Dict[K, Node[K, V]] = {}
        self._list: DoublyLinkedList[K, V] = DoublyLinkedList()
        self._lock = threading.RLock()

    def get(self, key: K) -> Optional[V]:
        with self._lock:
            node = self._cache.get(key)
            if not node:
                return None
            # Move accessed node to head (most recently used)
            self._list.remove_node(node)
            self._list.add_to_head(node)
            return node.value

    def put(self, key: K, value: V) -> None:
        with self._lock:
            if key in self._cache:
                node = self._cache[key]
                node.value = value
                self._list.remove_node(node)
                self._list.add_to_head(node)
                return

            if len(self._cache) >= self.capacity:
                evicted = self._list.remove_tail()
                if evicted and evicted.key is not None:
                    del self._cache[evicted.key]

            new_node = Node(key, value)
            self._cache[key] = new_node
            self._list.add_to_head(new_node)


# ==============================================================================
# 3. LFU CACHE (STRICT O(1))
# ==============================================================================

class LFUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        self._key_map: Dict[K, Node[K, V]] = {}
        self._freq_map: Dict[int, DoublyLinkedList[K, V]] = {}
        self._min_freq = 0
        self._lock = threading.RLock()

    def _update_freq(self, node: Node[K, V]) -> None:
        old_freq = node.freq
        freq_list = self._freq_map[old_freq]
        freq_list.remove_node(node)

        if freq_list.size == 0:
            del self._freq_map[old_freq]
            if self._min_freq == old_freq:
                self._min_freq += 1

        node.freq += 1
        new_list = self._freq_map.setdefault(node.freq, DoublyLinkedList())
        new_list.add_to_head(node)

    def get(self, key: K) -> Optional[V]:
        with self._lock:
            node = self._key_map.get(key)
            if not node:
                return None
            self._update_freq(node)
            return node.value

    def put(self, key: K, value: V) -> None:
        with self._lock:
            if key in self._key_map:
                node = self._key_map[key]
                node.value = value
                self._update_freq(node)
                return

            if len(self._key_map) >= self.capacity:
                min_list = self._freq_map[self._min_freq]
                evicted = min_list.remove_tail()
                if evicted and evicted.key is not None:
                    del self._key_map[evicted.key]
                if min_list.size == 0:
                    del self._freq_map[self._min_freq]

            new_node = Node(key, value, freq=1)
            self._key_map[key] = new_node
            self._min_freq = 1
            self._freq_map.setdefault(1, DoublyLinkedList()).add_to_head(new_node)


# ==============================================================================
# VERIFICATION RUNNER
# ==============================================================================

if __name__ == "__main__":
    print("=== Testing Strict O(1) LRU Cache ===")
    lru = LRUCache[str, int](capacity=2)
    lru.put("A", 1)
    lru.put("B", 2)
    assert lru.get("A") == 1  # A accessed, order: A (head), B (tail)
    lru.put("C", 3)           # Evicts B
    assert lru.get("B") is None
    assert lru.get("C") == 3
    print("LRU Cache passed!")

    print("\n=== Testing Strict O(1) LFU Cache ===")
    lfu = LFUCache[str, int](capacity=2)
    lfu.put("A", 10)
    lfu.put("B", 20)
    assert lfu.get("A") == 10  # freq(A) = 2, freq(B) = 1
    lfu.put("C", 30)           # Evicts B because min_freq is 1
    assert lfu.get("B") is None
    assert lfu.get("A") == 10
    assert lfu.get("C") == 30
    print("LFU Cache passed!")
