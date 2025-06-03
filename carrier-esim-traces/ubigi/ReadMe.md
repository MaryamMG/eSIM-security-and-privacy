# Ubigi eSIM Logcat Trace

## Overview

This folder contains detailed `logcat` traces captured from a **Pixel Android phone** during multiple lifecycle operations of a **Ubigi eSIM**. The logs were collected to analyze network behavior and system responses during eSIM provisioning and connectivity events.

All logs were captured using the `logcat` tool on Linux, with timestamps included to mark key stages of the experiment.

---

## Key Events Captured

- **eSIM Installation**  
  - Timestamp: *Sep 29, 11:32*

- **First Activation & Data Attempt**  
  - Timestamp: *11:33*  
  - Data was enabled, but **no internet connectivity** was observed initially.

- **Deactivation**  
  - Timestamp: *~11:36*

- **Second Activation Attempt**  
  - Timestamp: *~11:39*  
  - After several attempts, **network connection was eventually established**.

- **Third Deactivation**  
  - Timestamp: *13:57*

- **Fourth Activation**  
  - Timestamp: *13:59*

- **Fourth Deactivation**  
  - Timestamp: *14:01*

- **eSIM Erasure and Reinstallation**  
  - Timestamp: *14:01 onwards*

---

## Notes

- All logs are raw and unmodified for authenticity.
- They provide visibility into both radio and IMS registration events, data connection states, and operator-specific behaviors.
- Useful for debugging or analyzing eSIM lifecycle handling in consumer environments using Ubigi as the carrier.

---

## Tooling

- Logs captured with: `logcat`
- Device used: **Google Pixel**
- Operating system: **Android**

---
