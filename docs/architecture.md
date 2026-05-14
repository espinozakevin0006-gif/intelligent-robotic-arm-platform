# System Architecture

## Project Objective

The objective of this platform is to develop a scalable embedded robotics system capable of reliable motor control, future ROS2 integration, telemetry reporting, diagnostics, and multi-axis robotic manipulation.

Development is intentionally staged to prioritize reliable hardware integration before introducing higher-level robotics software complexity.

---

# Current Development Architecture

The current system is focused on single-axis motor-control validation.

## Current Hardware Pipeline

```text
ESP32-C6 Feather
        ↓ STEP/DIR
A4988 Stepper Driver
        ↓
NEMA17 Stepper Motor
```

## Current Power Architecture

```text
Wall AC
    ↓
Mean Well LRS-150-12
    ↓ 12V Rail
A4988 VMOT
```

Initial ESP32 development will temporarily use USB-C power from the development laptop during early bring-up and testing.

---

# Planned Logic Power Architecture

```text
12V Main Rail
        ↓
12V → 5V Buck Converter
        ↓
5V Logic Rail
        ├── ESP32
        ├── future sensors
        └── future embedded electronics
```

---

# Embedded Control Architecture

The ESP32-C6 Feather is responsible for:
- GPIO-based STEP pulse generation
- DIR signal control
- future enable/disable logic
- future telemetry generation
- future serial communication
- future fault handling
- future limit switch monitoring

Initial firmware objectives:
- reliable pulse generation
- directional control
- repeatable motion
- stable timing behavior

---

# Stepper Driver Architecture

The A4988 stepper driver acts as the interface between low-current embedded logic and high-current motor actuation.

Important signal relationships:

```text
STEP pulse
    → motor movement

DIR signal
    → rotation direction
```

The A4988 requires:
- proper current limiting
- shared system ground
- stable motor power
- correct motor coil pairing

---

# Future ROS2 Architecture

Planned ROS2 structure:

```text
ROS2 Node
    ↓
Serial Bridge
    ↓
ESP32 Firmware
    ↓
Motor Driver
    ↓
Motor Actuation
```

Future planned ROS2 capabilities:
- command publishing
- telemetry monitoring
- diagnostics
- state-machine integration
- future motion coordination

---

# Development Philosophy

The system is being developed incrementally:

```text
single-axis validation
    ↓
power validation
    ↓
firmware validation
    ↓
telemetry integration
    ↓
multi-axis expansion
    ↓
mechanical integration
    ↓
higher-level robotics software
```

This staged approach reduces debugging complexity and improves system reliability during development.

---

# Current Technical Priorities

Current engineering priorities:
- stable power integration
- safe wiring practices
- A4988 current limiting
- embedded GPIO control
- repeatable motor motion
- structured documentation
- scalable architecture planning

---

# Identified Risks

Current identified engineering risks:
- incorrect current-limit configuration
- unstable wiring
- grounding mistakes
- improper motor coil identification
- excessive thermal loading
- scaling before subsystem validation

---

# Long-Term Expansion Goals

Future planned system expansion includes:
- multi-axis robotic arm integration
- limit switch homing
- telemetry infrastructure
- diagnostics and fault reporting
- ROS2 communication bridge
- coordinated motion control
- future perception integration
- future manipulation planning
