# ESP32-C6 Feather Pin Map

## Purpose

Define the initial GPIO assignments for the ESP32-C6 Feather motor-control firmware.

This file will be updated after confirming the final usable GPIO pins from the Adafruit ESP32-C6 Feather pinout.

---

## A4988 Control Signals

| Signal | ESP32 Pin | A4988 Pin | Purpose |
|---|---|---|---|
| STEP | GPIO16 | STEP | Step pulse output |
| DIR | GPIO17 | DIR | Direction control |
| EN | GPIO18 | EN | Driver enable control |

---

## Required Shared Connections

| Connection | Purpose |
|---|---|
| ESP32 GND → A4988 GND | Shared logic reference |
| PSU GND → A4988 GND | Motor power reference |
| PSU GND → ESP32 GND | Common system ground |

---

## Initial Firmware Configuration

```cpp
#define STEP_PIN 16
#define DIR_PIN 17
#define EN_PIN 18
