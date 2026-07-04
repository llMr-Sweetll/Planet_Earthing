# Hardware Bill Of Materials

Version: 0.1.0  
Status: draft, vendor-neutral

## Tier 1: Minimum Viable Instrumentation

| Item | Purpose | Notes |
|---|---|---|
| High-input-impedance differential ADC | Surface electrical recording | Must resolve low-frequency millivolt-scale changes |
| Plant surface electrodes | Plant signal pickup | Prefer stable, documented electrode chemistry |
| Reference electrode | Differential reference | Placement must be standardized |
| Pressure glove or force-sensitive film | Human touch quantification | Required for host/stranger comparison |
| Temp/RH/CO2/light sensors | Confound tracking | Place near leaf, not across the room |
| Camera | Gesture verification | Fixed angle, time-synced |
| Microphone | Script timing and volume | Ultrasonic only if bioacoustics is in scope |
| Event marker button or TTL marker | Time alignment | Marks interaction start/stop |
| Time sync method | Cross-device alignment | NTP or hardware sync |

## Tier 2: Stronger Controls

| Item | Purpose | Notes |
|---|---|---|
| Dummy electrode/load channel | Detect electronic drift | Runs alongside plant channel |
| Motorized touch actuator | Repeatable mechanical control | Best way to separate human touch variation |
| Load cell under pot | Water-use proxy | Low-risk alternative to sap probe |
| Ultrasonic microphone | Plant stress sound detection | Needs quiet room and high sample rate |
| E-nose VOC array | Chemical signature | Needs blanks and drift correction |
| Clean-air or small chamber setup | VOC control | Avoids room air ambiguity |

## Tier 3: Specialist Instrumentation

| Item | Purpose | Notes |
|---|---|---|
| GC-MS validation | VOC compound confirmation | Use periodically, not necessarily every session |
| Thermal sap-flow probe | Water transport | Only for suitable stems; invasive |
| Leaf gas exchange system | Photosynthesis/transpiration | Expensive but interpretable |
| Infrared leaf temperature camera | Stomatal/water stress proxy | Watch reflections and room heat |
| Shielded chamber/Faraday cage | Electrical artifact control | Especially useful for weak electrophysiology |

## Procurement Notes

- Buy or build the pressure measurement first; without it, host versus stranger comparisons are weak.
- Prefer fewer well-calibrated channels over many uncalibrated novelty sensors.
- Choose sensors with timestamp export and documented calibration.
- Keep spare electrodes, cables, and gloves to avoid changing hardware mid-cohort.

