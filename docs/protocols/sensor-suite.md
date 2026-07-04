# Sensor Suite

Version: 0.1.0

## Sensor Philosophy

Every added sensor should either measure a plant response or measure a confound. The danger is not too little signal; it is measuring a pile of human artifacts and calling it plant recognition.

## Required Minimum Stack

| Channel | Purpose | Minimum notes |
|---|---|---|
| Surface electrical potential | Main plant electrophysiology channel | Differential measurement, stable reference, impedance checks |
| Pressure glove or tactile film | Touch confound control | Force, contact timing, stroke consistency |
| Microclimate | Confound control | Leaf-adjacent temperature, RH, CO2, light |
| Audio/video | Protocol verification | Human speech, gesture, entry/exit, accidental artifacts |
| Event marker | Alignment | Hardware or software marker for touch start/stop |

## Recommended Extended Stack

| Channel | Purpose | Caveats |
|---|---|---|
| Leaf vibration/piezo or accelerometer | Mechanical response and artifact tracking | Distinguish plant vibration from glove/cable motion |
| E-nose VOC array | Chemical response | High drift and human odor confounds; use blanks |
| Ultrasonic microphone | Stress bioacoustics | Requires high sampling rate and quiet room |
| Sap flow or water-status proxy | Water transport response | Thermal probes may wound small plants and may be too slow |
| Pot mass/load cell | Water-use proxy | Useful low-risk alternative to invasive sap probes |
| Electrode dummy/load channel | Instrument drift | Helps identify electronic artifacts |

## Suggested Sampling Rates

| Channel | Starting rate |
|---|---:|
| Electrical potential | 10 to 100 Hz |
| Pressure glove | 20 to 100 Hz |
| Piezo/accelerometer | 100 to 1000 Hz |
| Microclimate | 0.2 to 1 Hz |
| E-nose | 0.2 to 10 Hz |
| Ultrasonic audio | 192 kHz or appropriate ultrasonic recorder |
| Video | 30 fps minimum |

Pilot data should decide final rates.

## Electrical Recording Notes

- Use non-polarizable or well-characterized electrodes when possible.
- Record electrode placement with photos and a diagram.
- Keep cables strain-relieved and away from touch paths.
- Log impedance before and after sessions.
- Keep a dummy electrode channel or resistor input to detect shared electrical noise.
- Record local mains frequency and nearby devices.

## Pressure And Gesture Verification

The pressure channel is essential because host and stranger sessions are otherwise not matched. Log:

- peak force,
- mean force,
- force variance,
- number of strokes,
- stroke duration,
- contact area if available,
- hand used,
- glove ID,
- calibration status.

## VOC And Air Handling

If VOC/e-nose is used:

- Standardize airflow direction and exchange rate.
- Run blank chamber measurements.
- Ban perfume, scented lotion, cleaning sprays, and open solvents near the room.
- Track participant entry time because human breath and skin VOCs may dominate.
- Treat e-nose outputs as pattern sensors, not compound identification, unless validated by GC-MS.

## Sap Flow Decision Rule

Use thermal sap-flow probes only if:

- the selected species has suitable stem diameter,
- probe insertion will not compromise the longitudinal experiment,
- calibration is feasible,
- expected time dynamics match the research question.

If these conditions are not met, use pot mass, stem diameter variation, leaf temperature, or leaf gas exchange instead.

## Calibration Schedule

| Item | Frequency |
|---|---|
| Electrical baseline/dummy input | Daily |
| Electrode impedance | Before and after each session |
| Pressure glove zero and known-weight check | Daily and after glove changes |
| Microclimate sensors | Weekly cross-check |
| E-nose blank and reference gas | Before session block |
| Audio/video sync clap or marker | Daily |
| Clock synchronization | Daily |

