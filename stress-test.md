#!/bin/bash

# This script installs the Apache web server and its benchmarking tools,
# then runs a performance test to see how it handles traffic.

# Use echo to provide feedback during execution
echo "--- Starting Server Setup and Benchmark ---"

# Step 1: Install Apache Web Server AND the required tools (including 'ab')
# We use -y to automatically say "yes" to any installation prompts.
echo "--> Installing Apache (httpd) and tools (httpd-tools)..."
sudo yum install -y httpd httpd-tools

# Step 2: Start the Apache service and enable it to launch on boot
echo "--> Starting and enabling Apache service..."
sudo systemctl start httpd
sudo systemctl enable httpd

# Wait a couple of seconds to ensure the service is fully up and running
sleep 2

# Step 3: Run the benchmark.
# We are sending a more realistic load: 10,000 total requests,
# with 100 requests happening at the same time (concurrency).
# We are targeting 'localhost' because we are testing the server we just installed.
echo "--> Running Apache Benchmark (ab) with 10,000 requests and 100 concurrent users..."
ab -n 10000 -c 100 http://localhost/

echo "--- Benchmark Complete ---"