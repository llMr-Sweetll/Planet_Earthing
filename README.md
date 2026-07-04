# Planet_Earthing

## Abstract

Planet_Earthing is an open research repository for designing a controlled human-plant interaction experiment called **Pet the Plant**. The study asks whether plant-derived physiological signals can distinguish standardized interaction with a familiar human host from standardized interaction with novel strangers, after controlling for mechanical touch, voice, heat, CO2, volatile organic compounds, timing, room entry, and sensor drift.

This repository currently contains protocol design, literature synthesis, data schemas, and analysis scaffolding. It does **not** yet contain experimental results. As of 2026-07-04, Planet_Earthing has collected **0** plant-session recordings.

## Research Status

| Item | Current state |
|---|---|
| Project stage | Protocol design and preregistration draft |
| Primary experiment | `Pet the Plant` |
| Empirical sessions collected | `0` |
| Main biological claim status | Untested by this project |
| Working language | "familiarity-associated plant signal difference" |
| Disallowed conclusion at this stage | "plants recognize people" |
| Primary experiment package | [experiments/pet-the-plant](experiments/pet-the-plant) |
| Evidence register | [docs/research/evidence-ledger.json](docs/research/evidence-ledger.json) |

Empirical Planet_Earthing sessions collected: **0**. The current repository is a protocol and research-design package, not evidence of an observed host-versus-stranger effect.

## Problem Statement

Plants are known to produce measurable physiological responses to mechanical stimulation, wounding, water stress, volatile cues, and other environmental changes [1-6]. Those observations justify measuring plant electrical, mechanical, chemical, and microenvironmental signals during a standardized human interaction.

They do **not** justify claims that plants identify individual humans, detect emotional intent, or possess animal-like consciousness. Controlled work on Backster-style "primary perception" did not support the claimed remote electrophysiological response [7], and this project does not assume plant consciousness or sentience [8].

The scientific problem is therefore narrow:

> Can a carefully instrumented plant produce repeatable, plant-derived signal differences between familiar-host and novel-stranger sessions after known physical and environmental confounds are measured and modeled?

## Literature Basis

### Plant electrophysiology is measurable

Plant electrical signaling is a legitimate measurement domain. A recent open-science electrophysiology study recorded responses from more than 15 plant species after tactile or flame stimuli, showing that plant electrical responses can be captured across species under stimulus-controlled conditions [1]. This supports electrical recording as a study channel, but it also implies that electrode stability, stimulus timing, and environmental artifacts must be handled carefully.

### Touch is a real biological stimulus

Brief mechanical touch can change plant traits. In potato, one minute of light leaf touching per day altered biomass allocation, glandular trichomes, volatile emissions, and insect interactions [2]. Mechanistic work in Arabidopsis also shows that touch response and thigmomorphogenesis involve regulated signaling pathways, including CAMTA and jasmonate-dependent components [3]. This supports studying "petting" as a real mechanical stimulus, but it also makes pressure, contact area, stroke count, and repeated-touch history major confounds.

### Wounding and stress can trigger systemic plant signals

Wounding studies show that plants can propagate long-distance calcium-based defense signals after local injury [4]. This is important background because it shows that plants can coordinate systemic physiological responses without animal nerves. It does not imply that gentle touch or human familiarity produces a comparable effect.

### Plant sounds and VOCs are stress-state channels, not proof of recognition

Khait et al. recorded ultrasonic airborne sounds from stressed tomato and tobacco plants under dehydration and cutting conditions, and those sounds carried information about plant type and stress condition [5]. Electronic-nose studies also show that plant volatile signatures can be classified in some settings [6]. These findings justify optional acoustic and VOC measurements, but human sessions introduce strong non-plant confounds: breath CO2, humidity, body odor, glove material, room airflow, fabric noise, and speech.

### Unsupported claims are excluded from the hypothesis

Horowitz, Lewis, and Gasteiger tested a Backster-style "primary perception" claim and found electrophysiological unresponsiveness to brine-shrimp killing [7]. This project therefore does not cite Backster-style claims as evidence. It treats familiar-human discrimination as an unproven hypothesis requiring direct controls.

## Research Gap

The literature supports these narrower statements:

- plants can produce measurable electrical responses to stimuli [1],
- touch can alter plant morphology, chemistry, and signaling [2,3],
- stress and wounding can produce systemic or acoustic responses [4,5],
- VOC signatures can sometimes be classified [6].

The literature does **not** establish that a plant can distinguish a familiar human from a stranger under matched physical conditions. Planet_Earthing is designed to test that gap without turning general plant responsiveness into a person-recognition claim.

## Hypotheses

Primary null hypothesis:

```text
H0: After controlling for touch pressure, gesture, voice, CO2, heat, VOCs,
microclimate, time of day, plant ID, participant ID, and sensor drift,
plant-derived features do not differ between HOST_TOUCH_VOICE and
NOVEL_STRANGER_TOUCH_VOICE sessions.
```

Primary alternative hypothesis:

```text
H1: Plant-derived features differ between HOST_TOUCH_VOICE and
NOVEL_STRANGER_TOUCH_VOICE sessions after measured confounds are controlled.
```

Secondary questions:

- Does any host-associated response change over repeated sessions?
- Can a classifier distinguish host from stranger sessions using plant-derived features under grouped holdout validation?
- Do object-touch, robot-touch, no-touch, and voice-playback controls explain any apparent effect?

## Experimental Design

The first single-plant run is treated only as instrumentation validation. A confirmatory claim requires a multi-plant cohort.

| Component | Planned design |
|---|---|
| Plant cohort | Pilot: at least 6 plants; confirmatory target to be recalculated from pilot variance |
| Main contrast | `HOST_TOUCH_VOICE` versus `NOVEL_STRANGER_TOUCH_VOICE` |
| Familiar condition | One host assigned to repeated standardized sessions |
| Stranger condition | Novel participants with no prior exposure to the plant |
| Repeated non-host condition | Separates "known person" from host/caretaker effects |
| Mechanical controls | `OBJECT_TOUCH`; `ROBOT_TOUCH` if available |
| Presence and sound controls | `NO_TOUCH_BASELINE`; `VOICE_PLAYBACK_ONLY`; human-nearby/no-touch if implemented |
| Interaction duration | 60 seconds |
| Baseline window | Minimum 5 minutes before interaction |
| Recovery window | Minimum 10 minutes after interaction |
| Session verification | Time-synced audio/video plus event markers |

## Measurement Plan

| Channel | Role in the experiment | Main confounds |
|---|---|---|
| Surface electrical potential | Primary plant electrophysiology channel | Electrode drift, cable motion, humidity, mains noise |
| Pressure glove or tactile sensor | Measures human touch force and timing | Calibration drift, glove material, contact geometry |
| Leaf vibration or accelerometer | Separates plant motion from mechanical artifact | Cable movement, room vibration, hand movement |
| Microclimate | Tracks temperature, relative humidity, CO2, and light near the leaf | Human breath, HVAC, door opening |
| Audio/video | Verifies speech, timing, gesture, and accidental contact | Privacy, storage, observer bias |
| VOC/e-nose | Optional chemical-state channel | Human odor, cleaning products, humidity, airflow |
| Ultrasonic microphone | Optional stress-sound channel | Fabric, mouth, glove, HVAC, and room sounds |
| Water-status proxy | Optional slow physiological channel | Probe invasiveness, watering schedule, time lag |

Sap-flow probes are not assumed to be appropriate for small potted plants. If the selected species cannot support them safely, less invasive proxies such as pot mass, leaf temperature, or stem diameter variation are preferred.

## Analysis Plan

The analysis unit is the session, not individual time-series rows. Row-wise train/test splits are disallowed because they would leak plant, date, and sensor-state information.

Primary model family:

```text
feature ~ condition
        + pressure_summary
        + microclimate_summary
        + session_day
        + time_of_day
        + soil_moisture
        + (1 | plant_id)
        + (1 | participant_id)
        + (1 | cohort_id)
```

Machine-learning evaluation must use:

- plant-derived features only for the plant-only classifier,
- grouped splits by plant, participant, and date block,
- held-out stranger sessions,
- permutation-label tests,
- a confound-only comparison model,
- feature-importance review for pressure, drift, and microclimate leakage.

Success criteria are intentionally strict:

- corrected `p < 0.01` for the preregistered primary contrast,
- effect size estimated on plant/session aggregates, not time-series rows,
- plant-only classifier AUC above chance under grouped holdout validation,
- failure of confound-only models to explain the result,
- replication across independent plant cohorts.

## Current Repository Contents

| Path | Purpose |
|---|---|
| [docs/research/evidence-ledger.json](docs/research/evidence-ledger.json) | Machine-readable evidence matrix |
| [docs/research/evidence-summary.md](docs/research/evidence-summary.md) | Plain-language evidence summary |
| [docs/research/fact-check.md](docs/research/fact-check.md) | Claim-by-claim fact check |
| [docs/research/literature-map.md](docs/research/literature-map.md) | Topic-organized literature notes |
| [docs/protocols/preregistration.md](docs/protocols/preregistration.md) | Preregistration draft |
| [docs/protocols/experimental-protocol.md](docs/protocols/experimental-protocol.md) | Session protocol |
| [docs/protocols/statistical-analysis-plan.md](docs/protocols/statistical-analysis-plan.md) | Statistical and ML analysis rules |
| [docs/protocols/sensor-suite.md](docs/protocols/sensor-suite.md) | Sensor requirements and caveats |
| [docs/specs/data-dictionary.md](docs/specs/data-dictionary.md) | Session metadata and data schema |
| [experiments/pet-the-plant](experiments/pet-the-plant) | Experiment-specific templates |
| [src/planetearthing](src/planetearthing) | Lightweight validation and feature-summary helpers |

## How To Use This Repo

```bash
git clone https://github.com/llMr-Sweetll/Planet_Earthing.git
cd Planet_Earthing
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 scripts/validate_repo.py
```

The validation script checks that the README keeps its research-report structure, required reference markers are present, JSON templates are valid, the session metadata template is valid, and disallowed overclaiming language is absent.

## Ethics And Data Handling

This study design involves human participants, video, audio, touch-pressure traces, possible human VOC traces, and precise timestamps. Raw participant media, consent forms, names, and identifiable sensor streams must not be committed to the repository. Public data releases require consent review, de-identification, and a separate data-release decision.

## License

Repository code, protocols, and documentation are released under the [MIT License](LICENSE). Future datasets may use separate release terms after consent and de-identification review.

## References

[1] Madariaga, D. et al. "A library of electrophysiological responses in plants - a model of transversal education and open science." *Plant Signaling & Behavior* (2024). DOI: [10.1080/15592324.2024.2310977](https://doi.org/10.1080/15592324.2024.2310977).

[2] Markovic, D., Nikolic, N., Glinwood, R., Seisenbaeva, G., and Ninkovic, V. "Plant Responses to Brief Touching: A Mechanism for Early Neighbour Detection?" *PLOS ONE* 11(11): e0165742 (2016). DOI: [10.1371/journal.pone.0165742](https://doi.org/10.1371/journal.pone.0165742).

[3] Darwish, E. et al. "Touch signaling and thigmomorphogenesis are regulated by complementary CAMTA3- and JA-dependent pathways." *Science Advances* 8(20): eabm2091 (2022). DOI: [10.1126/sciadv.abm2091](https://doi.org/10.1126/sciadv.abm2091).

[4] Toyota, M. et al. "Glutamate triggers long-distance, calcium-based plant defense signaling." *Science* 361(6407): 1112-1115 (2018). DOI: [10.1126/science.aat7744](https://doi.org/10.1126/science.aat7744).

[5] Khait, I. et al. "Sounds emitted by plants under stress are airborne and informative." *Cell* 186(7): 1328-1336.e10 (2023). DOI: [10.1016/j.cell.2023.03.009](https://doi.org/10.1016/j.cell.2023.03.009).

[6] Laothawornkitkul, J. et al. "Discrimination of Plant Volatile Signatures by an Electronic Nose: A Potential Technology for Plant Pest and Disease Monitoring." *Environmental Science & Technology* 42(22): 8433-8439 (2008). DOI: [10.1021/es801738s](https://doi.org/10.1021/es801738s).

[7] Horowitz, K. A., Lewis, D. C., and Gasteiger, E. L. "Plant Primary Perception: Electrophysiological Unresponsiveness to Brine Shrimp Killing." *Science* 189(4201): 478-480 (1975). DOI: [10.1126/science.189.4201.478](https://doi.org/10.1126/science.189.4201.478).

[8] Taiz, L. et al. "Plants Neither Possess nor Require Consciousness." *Trends in Plant Science* 24(8): 677-687 (2019). DOI: [10.1016/j.tplants.2019.05.008](https://doi.org/10.1016/j.tplants.2019.05.008).
