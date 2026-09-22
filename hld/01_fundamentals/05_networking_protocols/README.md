# Networking Protocols & Communication Patterns

> **Must-Know Fundamentals**: The transport and application layer protocols that power modern distributed systems.

---

## 1. Transport Layer: TCP vs UDP

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Connection** | Connection-oriented (3-Way Handshake: SYN -> SYN-ACK -> ACK) | Connectionless (Fire and forget) |
| **Reliability** | Guaranteed in-order delivery, retransmissions on packet loss | No guarantee of delivery or ordering |
| **Flow & Congestion**| Built-in flow control (sliding window) & congestion control | None |
| **Overhead** | 20-byte header, handshake latency | 8-byte header, minimal latency |
| **Use Cases** | HTTP/REST, WebSockets, gRPC, Database connections | Video streaming (RTP), VoIP, Online multiplayer gaming, DNS |

---

## 2. Web Communication Protocols: HTTP/1.1 vs HTTP/2 vs HTTP/3

- **HTTP/1.1**:
  - One request/response per TCP connection at a time.
  - Suffers from **Head-of-Line (HoL) Blocking** at the HTTP application layer.
  - Keep-Alive reuses connections, but browsers still open up to 6 parallel TCP connections per domain.
- **HTTP/2**:
  - **Multiplexing**: Multiple bidirectional streams over a single TCP connection.
  - Header compression (HPACK).
  - Server push.
  - *Pitfall*: If a single packet drops on the TCP connection, all streams stall (**TCP-level HoL blocking**).
- **HTTP/3 (QUIC)**:
  - Runs on **UDP** instead of TCP.
  - Implements its own congestion control and encryption (TLS 1.3 baked into transport).
  - Eliminates TCP Head-of-Line blocking: A dropped packet on stream A does not stall stream B.
  - Zero-RTT (0-RTT) connection resumption for roaming mobile clients.

---

## 3. Real-Time Communication Patterns

| Pattern | How It Works | Direction | Overhead | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Short Polling** | Client sends repeated HTTP requests on a timer (e.g. every 3s). | Client -> Server | High (HTTP headers sent every request) | Rarely recommended in production |
| **Long Polling** | Client sends request; server holds connection open until new data is available. | Client <-> Server | Medium | Legacy fallback, notification alerts |
| **Server-Sent Events (SSE)** | Persistent HTTP connection where server pushes text events to client. | Server -> Client (Unidirectional) | Low (Reuses standard HTTP/2) | Stock tickers, live sports scores, LLM streaming responses |
| **WebSockets** | Full-duplex bidirectional TCP connection initiated via HTTP Upgrade handshake. | Bi-directional | Very Low (2-byte framing overhead) | Real-time chat (WhatsApp), collaborative editors (Google Docs) |
| **gRPC** | High-performance RPC over HTTP/2 with Protocol Buffers serialization. | Bi-directional / Streaming | Ultra-Low (Binary compact format) | Internal microservice-to-microservice communication |
