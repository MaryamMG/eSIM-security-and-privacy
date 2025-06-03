# Mint Mobile eSIM Reinstallation and Erasure Logs

## Overview

This folder contains log and network capture files collected during experiments with a **Mint Mobile eSIM** on a **Pixel 4** device. The focus was on analyzing system and network behavior during attempted eSIM reinstallation and erasure procedures.

Two tools were used for data collection:
- `logcat` for Android system logs
- `Wireshark` for capturing network traffic in `.pcap` format

---

## Contents

### PCAP Files

- `PCAPdroid_5_reinstall_before_erase.pcap`  
  Network capture while attempting to **reinstall the eSIM before erasing it**.

- `PCAPdroid_6_erase.pcap`  
  Network capture collected during the **eSIM erasure process**.

> Captured using **PCAPdroid** and analyzed with **Wireshark**.

---

### Logcat and Supporting Logs

- `pixel4_try-to-reinstall-before-erase.log`  
  Android `logcat` trace showing system-level events during the **reinstall attempt**.

- `sslkeylogfile5.txt`, `sslkeylogfile6.txt`  
  TLS key log files for decrypting HTTPS traffic in the above PCAPs using Wireshark.

---
