# Load Balancing & Reverse Proxies (L4 vs L7)

> **Must-Know Fundamentals**: Distributing traffic effectively and eliminating single points of failure.

---

## 1. Layer 4 vs Layer 7 Load Balancing

| Dimension | Layer 4 (Transport Layer: TCP/UDP) | Layer 7 (Application Layer: HTTP/HTTPS/gRPC) |
| :--- | :--- | :--- |
| **OSI Layer** | Transport (IP address and Port number) | Application (URL path, HTTP headers, Cookies) |
| **Inspection** | Does NOT decrypt SSL or inspect packet payloads. | Decrypts TLS (SSL Termination) and inspects HTTP body/headers. |
| **Routing Decisions** | Routes purely based on source/dest IP and Port. | Can route `/api/v1/checkout` to Service A and `/images/*` to CDN/Service B. |
| **Performance** | ⚡ Extremely high throughput, minimal CPU overhead. | Slightly higher CPU overhead due to TLS termination & header parsing. |
| **Technologies** | AWS NLB (Network Load Balancer), HAProxy, IPVS | AWS ALB (Application Load Balancer), Nginx, Envoy, Traefik |

---

## 2. Load Balancing Algorithms

1. **Round Robin & Weighted Round Robin**:
   - Requests distributed sequentially across servers.
   - Weighted assigns more requests to higher-spec hardware.
2. **Least Connections & Least Response Time**:
   - Directs traffic to the server with fewest active connections or lowest latency. Ideal for long-lived sessions (WebSockets).
3. **IP Hash**:
   - Hash of client IP determines the backend server (simple session stickiness).
   - *Downside*: Many corporate users behind NAT share identical public IP, causing load imbalance.
4. **Consistent Hashing**:
   - Uses a hash ring with virtual nodes.
   - Essential for stateful servers (Distributed Caches, WebSocket Gateways) because adding or removing a server only remaps $K/N$ keys rather than reshuffling all traffic.

---

## 3. High Availability of Load Balancers (Who balances the Load Balancer?)

A single load balancer is a Single Point of Failure (SPOF). Production setups use:
1. **DNS Round Robin / GeoDNS**: DNS resolves a domain to multiple load balancer public IPs based on geographical proximity.
2. **VRRP / Keepalived (Virtual IP Floating)**: Two load balancers share a virtual IP. If primary fails health checks, the backup claims the IP address via ARP broadcast in milliseconds.
