# Proactive Communication Traces

## Overview

This section focuses on analyzing **proactive behavior** from commercial travel eSIM profiles, specifically how some profiles can **silently initiate communication** or interact without user involvement. 

The following datasets capture such behaviors for two real-world eSIM providers: **Holafly** and **eSIM Access**.

---

## Holafly/

This folder contains packet captures and traces related to the Holafly travel eSIM:

- `Holafly_first_startup_trace.pcapng`  
  Captured immediately after the eSIM profile was first installed and enabled. This trace shows unsolicited STK activity and network signaling that occurred without any user action.

- `Holafly_trace_sim_app_interaction.pcapng`  
  Shows interactions between the device and the eSIM applet, including proactive commands.

- `py_stim_trace`  
  Decoded logs and protocol-level output from interactions with the eSIM profile, extracted using the PySim toolset.

---

## eSIM_Access/

This folder includes traces captured during eSIM provisioning and activation using a eSIM Access profile:

- `eSIM_Access_trace.pcapng`  
  Full packet capture of SIM activity post-installation.

- `PySim_trace.txt`  
  Decoded logs and protocol-level output from interactions with the eSIM profile, extracted using the PySim toolset.

These traces demonstrate how **reseller-generated profiles** can contain embedded logic or references that perform backend interactions automatically, even when the user takes no action.


---

## Reference

For analysis, methodology, and implications of these traces, refer to our paper:  
**"eSIMplicity or eSIMplification? Privacy and Security Risks in the eSIM Ecosystem"**
