# Hardware Bring-Up Plan

## Objective

Validate the first physical motion subsystem for the robotic arm platform.

The current goal is not to build the full robotic arm. The goal is to prove that one embedded controller can reliably command one stepper motor through one motor driver using a stable power system.

---

## Current Bring-Up Target

```text
ESP32-C6 Feather
        ↓ STEP / DIR
A4988 Stepper Driver
        ↓
NEMA17 Stepper Motor
```

Motor power:

```text
Mean Well LRS-150-12
        ↓ 12V
A4988 VMOT
```

Logic power during early testing:

```text
Laptop USB-C
        ↓
ESP32-C6 Feather
```

Later logic power:

```text
12V Main Rail
        ↓
12V → 5V Buck Converter
        ↓
ESP32 / sensors / logic electronics
```

---

## Hardware Available

- ESP32-C6 Feather
- Adafruit A4988 Stepper Driver
- NEMA17 Stepper Motor
- Adafruit Perma-Proto Board
- Soldering kit
- Multimeter

Purchased and awaiting delivery:

- Mean Well LRS-150-12 Power Supply
- 12V/24V → 5V 10A Buck Converter

---

## Required Safety Rules

1. Do not connect or disconnect the stepper motor while the driver is powered.
2. Verify PSU output voltage with a multimeter before connecting the motor driver.
3. Verify buck converter output voltage before connecting any logic electronics.
4. Confirm common ground between ESP32, motor driver, and power supply.
5. Set the A4988 current limit before extended motor testing.
6. Keep wiring short and organized.
7. Power off the system before changing wiring.
8. Monitor motor and driver temperature during first tests.

---

## A4988 Signals

Important control pins:

```text
STEP  → receives pulses from ESP32
DIR   → receives direction signal from ESP32
EN    → enables/disables driver output
VDD   → logic voltage
GND   → shared logic/power ground
VMOT  → motor power input
1A/1B → motor coil A
2A/2B → motor coil B
```

Core concept:

```text
Each STEP pulse causes motion.
DIR sets the direction of motion.
```

---

## First Wiring Plan

Initial wiring should be simple.

```text
ESP32 GND  → A4988 GND
ESP32 GPIO → A4988 STEP
ESP32 GPIO → A4988 DIR

Mean Well +12V → A4988 VMOT
Mean Well GND  → A4988 motor GND

NEMA17 coil pair A → A4988 1A / 1B
NEMA17 coil pair B → A4988 2A / 2B
```

Do not solder final wiring until the pinout and layout are verified.

---

## Motor Coil Identification

Before connecting the stepper motor:

1. Use the multimeter in resistance/continuity mode.
2. Find the two wire pairs that show continuity.
3. Mark one pair as coil A.
4. Mark the other pair as coil B.
5. Connect one pair to 1A/1B and the other to 2A/2B.

If the motor vibrates but does not rotate, the coil wiring may be incorrect.

---

## Current Limit Setup

The A4988 current limit must be adjusted before extended use.

Current-limit procedure will be documented during physical bring-up after confirming the exact board reference voltage behavior.

Important note:

Incorrect current limit can cause:
- weak motor torque
- skipped steps
- driver overheating
- motor overheating
- driver failure

---

## First Firmware Test

The first firmware test should be minimal.

Goal:

```text
Set direction.
Send 200 step pulses.
Pause.
Reverse direction.
Send 200 step pulses.
Repeat.
```

No ROS2 integration is required for the first motor spin test.

The first objective is to confirm that the ESP32 can generate clean STEP/DIR signals and that the A4988 can drive the NEMA17 motor reliably.

---

## First Test Success Criteria

The first bring-up test is successful if:

- PSU output is confirmed at 12V.
- A4988 powers without overheating.
- ESP32 remains stable over USB.
- STEP/DIR signals produce motor motion.
- Motor rotates in both directions.
- Motor does not skip steps at low speed.
- Driver does not overheat during short test.
- Wiring remains stable during testing.

---

## Expected Failure Modes

Possible early failures:

| Symptom | Likely Cause |
|---|---|
| Motor vibrates but does not rotate | Incorrect coil pairing |
| Motor does not move | STEP/DIR wiring issue |
| ESP32 resets | Grounding or power issue |
| Driver overheats | Current limit too high |
| Motor weak/skipping | Current limit too low |
| Random motion | Floating inputs or poor ground |
| No response | Driver disabled or sleep/reset issue |

---

## Bring-Up Sequence

1. Inspect hardware.
2. Identify A4988 pins.
3. Identify motor coil pairs.
4. Verify PSU voltage.
5. Connect motor power to A4988.
6. Connect motor coils.
7. Connect ESP32 GND to A4988 GND.
8. Connect ESP32 GPIO pins to STEP and DIR.
9. Set conservative current limit.
10. Upload minimal firmware.
11. Run low-speed motion test.
12. Monitor temperature.
13. Record results in engineering log.

---

## Documentation Requirements

During bring-up, record:

- wiring photos
- PSU voltage measurement
- buck converter voltage measurement
- A4988 current-limit setting
- firmware version
- first motion result
- failures observed
- fixes applied
- lessons learned

All results should be logged in:

```text
logs/bringup_logs/
```

---

## Next Milestone

The next milestone is:

```text
ESP32-C6 Feather → A4988 → NEMA17 reliable low-speed motion
```

Once this is stable, the system can move toward:

- serial command control
- ROS2 command integration
- limit switch homing
- telemetry reporting
- multi-axis expansion
