# ESP32-C6 Feather Pin Map

## Purpose

Define the initial GPIO assignments for the ESP32-C6 Feather motor-control firmware.

This file will be updated after confirming the final usable GPIO pins from the Adafruit ESP32-C6 Feather pinout.

## A4988 Control Signals

| Signal | ESP32 Pin | A4988 Pin | Purpose |
|---|---|---|---|
| STEP | TBD | STEP | Step pulse output |
| DIR | TBD | DIR | Direction control |
| EN | TBD | EN | Driver enable control |

## Required Shared Connections

| Connection | Purpose |
|---|---|
| ESP32 GND → A4988 GND | Shared logic reference |
| PSU GND → A4988 GND | Motor power reference |
| PSU GND → ESP32 GND | Common system ground |

## Notes

- STEP and DIR must use digital output-capable GPIO pins.
- EN is optional for the first test but should be included for safety later.
- Avoid using pins required for USB, boot, or board-specific functions unless confirmed safe.
- Final pin assignments must be verified against the Adafruit ESP32-C6 Feather documentation before wiring.
