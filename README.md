# linux-log-monitor
A Python-based centralized log monitoring system that detects SSH brute-force attacks in real-time across multiple Linux nodes and sends automated SMTP alerts.
# 🛡️ Linux Log Monitoring & Alerting System

A real-time security monitoring architecture designed to centralize authentication logs across multiple Linux nodes. This system utilizes a Python detection engine to identify SSH brute-force attacks and instantly trigger automated email notifications to administrators.

## 🏗️ Architecture
This project uses a Manager-Worker topology:
* **Worker Node (Kali Linux):** Forwards `/var/log/auth.log` telemetry via UDP over Port 514.
* **Manager Node (Ubuntu Server):** Acts as the centralized log aggregator using `rsyslog` and hosts the Python detection engine.

## ✨ Key Features
* **Real-time Stream Parsing:** Uses a low-overhead continuous read loop (similar to `tail -f`) to process logs with zero latency.
* **Automated Threat Detection:** Instantly identifies `Failed password` strings indicative of SSH brute-force attempts.
* **Metadata Extraction:** Dynamically parses syslog formatting to identify the compromised node's hostname.
* **SMTP Alerting:** Securely dispatches incident reports to an administrator inbox via TLS-encrypted email.
* **Secure Credential Management:** Utilizes Python `dotenv` to isolate application passwords from the source code.

## 🛠️ Technology Stack
* **OS:** Ubuntu Server 24.04, Kali Linux
* **Networking:** Netplan, VirtualBox Host-Only Subnetting, UFW (Uncomplicated Firewall)
* **Log Transport:** Syslog Protocol (RFC 5424) via `rsyslog`
* **Language:** Python 3 (`smtplib`, `os`, `time`)

## 🚀 Setup Instructions
1. Ensure `rsyslog` is configured on both the client (forwarding `*.* @MANAGER_IP:514`) and the server (listening on `imudp` port 514).
2. Clone this repository to your Manager node.
3. Create a `.env` file in the root directory and add your email app password:
   ```text
   EMAIL_PASSWORD=your_secure_app_password
   sender_email=write your_email
