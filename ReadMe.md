# eSIM Security and Privacy Analysis

## Project Overview

This project investigates the **security and privacy risks** in the eSIM ecosystem, with a particular focus on travel eSIMs, reseller behavior, profile management, and private LTE deployments. Our goal is to understand the operational characteristics of eSIMs in real-world conditions and uncover systemic weaknesses that impact user control, transparency, and data sovereignty.

We performed a series of experiments using commercial eSIMs, programmable testbeds, and traffic analysis. The experiments explore:
- Data routing paths and jurisdictional exposure
- Reseller access and control over user data
- Silent/proactive communication from installed profiles
- Lifecycle failures in eSIM deletion and reinstallation
- Threats from private network operators

---

## Folder Breakdown

### `Travel-eSIMs/`
This folder includes screenshots and metadata about **travel eSIMs** purchased and tested from a variety of international providers.

### `Proactive-Communication/`
Contains low-level logs of **proactive behavior** observed from travel eSIM profiles. Using SIMtrace2 and a programmable sysmoEUICC1 module, we captured unsolicited STK commands, and background communications triggered by installed eSIMs—demonstrating actions that occur without user initiation.

### `Amarisoft-PrivateNetwork/`
In this section, we evaluated **eSIM installation, activation, and deletion** on a private LTE network using the Amarisoft Callbox. The logs include both phone-side (`logcat`) and network-side (MME, NAS, attach procedure) traces. We show how offline deletions can silently fail and cause profile lock-in, consistent with denial-of-service scenarios described in the paper.

### `carrier-esim-traces/`
Logs from four **Mint Mobile eSIMs** captured using both `logcat` and **Wireshark**. These include multiple installations, activations, deactivations, and erasure attempts—highlighting edge-case behaviors, such as failed deletions and reinstallation problems.

### `eSIM-Resellers/`
Documents the internal workings of multiple **reseller platforms**, including eSIMAccess and Telnyx. We created accounts and provisioned our own eSIMs to observe:
- Access to user metadata (EIDs, ICCIDs, MSISDNs)
- Ability to send SMS, assign public IPs, and revoke profiles
- Live dashboards and API documentation that expose private device state to resellers

These experiments emphasize how reseller dashboards can track or control user activity, often without consent or transparency.

---


## Reference

For full technical details, methodology, and analysis, refer to our paper:  
**"eSIMplicity or eSIMplification? Privacy and Security Risks in the eSIM Ecosystem"**

This document is intended to supplement that research with reproducible data and real-world evidence.

