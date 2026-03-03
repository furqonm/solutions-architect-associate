# 🏎️ Apache Web Server Benchmark Suite

This repository contains a streamlined automation script designed to deploy the Apache HTTP Server and immediately perform a stress test using the `ab` (Apache Benchmark) tool.

It is ideal for testing the baseline performance of a new virtual machine or verifying server stability under concurrent load.

---

## 📜 The Automation Script

The script handles the end-to-end process: installation, service activation, and performance profiling.

```bash
#!/bin/bash

# This script installs the Apache web server and its benchmarking tools,
# then runs a performance test to see how it handles traffic.

echo "--- Starting Server Setup and Benchmark ---"

# 1. Install Apache Web Server AND the required tools (including 'ab')
echo "--> Installing Apache (httpd) and tools (httpd-tools)..."
sudo yum install -y httpd httpd-tools

# 2. Start and enable Apache service
echo "--> Starting and enabling Apache service..."
sudo systemctl start httpd
sudo systemctl enable httpd

# Pause to ensure service stability
sleep 2

# 3. Run the benchmark
# 10,000 total requests | 100 concurrent users
echo "--> Running Apache Benchmark (ab) with 10,000 requests and 100 concurrent users..."
ab -n 10000 -c 100 http://localhost/

echo "--- Benchmark Complete ---"

```

---

## 🛠️ Technical Breakdown

### **1. Package Installation**

The script installs `httpd` (the server) and `httpd-tools`. The latter is critical because it contains the **Apache Benchmark (ab)** utility, a high-performance tool used for measuring how many requests per second your server can sustain.

### **2. Service Initialization**

Using `systemctl`, the script ensures the server is not only running now but will automatically persist through system reboots.

### **3. The Benchmark Logic**

The command `ab -n 10000 -c 100` simulates a heavy traffic spike:

* **Total Requests (`-n`)**: 10,000 individual hits to the server.
* **Concurrency (`-c`)**: 100 users hitting the server at the exact same millisecond.

---

## 📊 Understanding Your Results

After the script runs, pay close attention to these three metrics in the terminal output:

| Metric | What it tells you |
| --- | --- |
| **Requests per second** | This is your server's "throughput." Higher is better. |
| **Time per request** | The average latency a user experiences (in milliseconds). |
| **Failed requests** | If this is above zero, your server is "dropping the ball" under the current load. |

---

## 🚀 How to Run

1. **Clone** this repository to your Linux instance.
2. **Make it executable**: `chmod +x benchmark.sh`
3. **Run with sudo**: `./benchmark.sh`

> [!TIP]
> If you are running this on a small instance (like a `t2.micro`), keep an eye on CPU credits. High concurrency tests can quickly exhaust burstable performance.
