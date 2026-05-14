# Firmware Design Plan

## Objective

Develop scalable embedded firmware for the ESP32-C6 Feather capable of reliable stepper motor control, future telemetry reporting, diagnostics, and integration with higher-level robotics software.

The initial firmware goal is intentionally minimal:

```text
Generate reliable STEP/DIR signals for one NEMA17 stepper motor through the A4988 driver.
```

The firmware architecture should remain scalable so additional robotics features can be added without major rewrites.

---

# Initial Firmware Goals

The first firmware milestone is:

1. Configure GPIO outputs.
2. Set motor direction.
3. Generate STEP pulses.
4. Reverse direction.
5. Repeat motion reliably.

The purpose of this phase is hardware validation and motion-system verification.

---

# Initial Firmware Architecture

Planned early firmware structure:

```text
main loop
    ↓
motion test logic
    ↓
STEP pulse generation
    ↓
A4988 driver
    ↓
NEMA17 motor motion
```

Initial implementation should prioritize:
- readability
- stability
- predictable timing
- simple debugging

---

# GPIO Responsibilities

Initial GPIO usage:

| Signal | Function |
|---|---|
| STEP | Generates movement pulses |
| DIR | Controls rotation direction |
| EN | Optional driver enable control |
| GND | Shared reference ground |

Future GPIO additions:
- limit switches
- fault inputs
- telemetry indicators
- status LEDs
- sensor interfaces

---

# STEP/DIR Control Model

The A4988 uses a simple digital control model:

```text
STEP pulse
    → move motor

DIR level
    → set rotation direction
```

Motor speed is determined by pulse frequency.

```text
Higher pulse frequency
    → faster motor rotation
```

---

# Initial Motion Strategy

Early tests should use:
- low pulse frequency
- low acceleration
- short motion sequences

The objective is stable and repeatable motion rather than high speed.

---

# Future Motion Features

Planned future motion improvements:
- acceleration ramps
- non-blocking timing
- coordinated motion
- motion queues
- position tracking
- homing logic
- fault recovery
- state-machine control

---

# Current Limiting Awareness

Firmware development must account for hardware current limits.

Even perfect firmware cannot compensate for:
- incorrect A4988 current limit
- unstable power
- poor grounding
- incorrect coil wiring

Hardware validation and firmware validation must occur together.

---

# Planned Firmware Modules

Future modular structure:

```text
main.cpp
    ↓
motor_controller
    ↓
step_generator
    ↓
telemetry_system
    ↓
fault_manager
    ↓
serial_command_parser
```

Possible future module breakdown:

```text
motor_controller/
telemetry/
fault_handling/
serial_protocol/
homing/
diagnostics/
```

---

# Telemetry Goals

Planned telemetry output:

```text
BOOT
READY
MOVING
DONE
FAULT
```

Future telemetry expansion:
- motor state
- estimated position
- driver temperature
- fault codes
- homing status
- command acknowledgements

---

# Serial Communication Goals

Future serial command examples:

```text
MOVE:1000
STOP
HOME
STATUS
```

Example future responses:

```text
OK:MOVING
OK:DONE
FAULT:LIMIT
FAULT:OVERCURRENT
```

The protocol should remain human-readable during early development to simplify debugging.

---

# ROS2 Integration Plan

Future ROS2 architecture:

```text
ROS2 node
    ↓
serial bridge
    ↓
ESP32 firmware
    ↓
motor controller
```

The ESP32 firmware should eventually support:
- command parsing
- telemetry transmission
- fault reporting
- future synchronized motion commands

---

# State Machine Planning

Future firmware should evolve toward explicit state management.

Planned states:

```text
BOOT
INIT
IDLE
READY
ACTIVE
FAULT
RECOVERY
```

State-based control will improve:
- debugging
- fault handling
- reliability
- scalability
- system clarity

---

# Development Philosophy

Firmware development should prioritize:
- stability first
- deterministic behavior
- simple debugging
- modular growth
- maintainable structure
- scalable architecture

Advanced robotics features should only be added after stable low-level motion control is proven.

---

# Immediate Firmware Milestone

The next firmware milestone is:

```text
ESP32 generates reliable STEP pulses
→ A4988 receives control signals
→ NEMA17 rotates reliably in both directions
```

This is the foundational embedded-control milestone for the entire robotic platform.
