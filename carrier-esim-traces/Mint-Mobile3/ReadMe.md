# Mint Mobile eSIM Installation Traffic Captures

## Overview

This folder contains network capture files related to **Mint Mobile eSIM installation attempts**, including both successful and unsuccessful sessions. The captures were collected using `tcpdump` and analyzed via Wireshark.

The goal was to observe network behavior, TLS negotiation, and potential failure points during profile download and installation.

---

## Contents

### PCAP / PCAPNG Files

- `mint_installation.pcapng`  
  Network capture during a **successful Mint Mobile eSIM installation** attempt.

- `unsuccessfull_installation.pcapng`  
  Network capture from a **failed installation attempt**, useful for comparison and failure analysis.

- `mint_tcpdump.pcap`  
  Raw packet capture using `tcpdump`.

---

