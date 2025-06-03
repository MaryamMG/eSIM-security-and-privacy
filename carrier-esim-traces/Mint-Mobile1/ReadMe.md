# eSIM Lifecycle and Transfer Logs

## Overview

This folder contains a series of `logcat`-captured logs collected from both **Pixel 4** and **Galaxy S22** devices. The logs document various stages of eSIM lifecycle events such as downloading, installing, validating, activating, erasing, and transferring eSIM profiles. These logs are valuable for analyzing Android system behavior during eSIM provisioning and transfer scenarios.

---

## File Descriptions

### Pixel 4 Logs

- `pixel4_esim_download_QRCode.txt`  
  Log of eSIM download using a QR code.

- `pixel4_esim_install_QRcode.txt`  
  Installation log after successful QR scan and download.

- `pixel4_esim_activate_after_install.txt`  
  Logs showing activation right after installation.

- `pixel4_esim_after_validation-esim.txt`  
  Log captured after eSIM profile validation step.

- `pixel4_esim_before-activation.txt`  
  System state before activation.

- `pixel4_esim_after-erased-esim.txt`  
  Log showing system behavior after erasing the eSIM profile.

- `pixel4_esim_tranfer_to_galaxy-S22-2.txt`  
  Log from an attempted transfer of an eSIM from Pixel 4 to Galaxy S22 (trial 2).

---

### Galaxy S22 Logs

- `galaxy-s22_as-new-device_accepting_esim_tranfer.txt`  
  Log of Galaxy S22 acting as a recipient during eSIM transfer from another device.


---



