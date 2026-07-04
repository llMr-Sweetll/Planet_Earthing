# Consent And Privacy Packet

Version: 0.1.0  
Status: draft for review, not legal advice

## Purpose

Pet the Plant can record identifiable human data. This packet defines the minimum consent and privacy controls required before any real human participant session.

## Data That May Identify A Participant

- face or body on video,
- voice on audio,
- hands or scars visible in video,
- pressure/touch pattern,
- gait or posture,
- timestamps linked to attendance,
- human breath CO2,
- body odor or scented-product VOC traces,
- operator notes.

## Consent Checklist

Before participation, the participant must understand:

- the study records plant-adjacent sensor data during a standardized interaction,
- video/audio may be recorded for protocol verification,
- pressure/touch data may be recorded,
- raw media are not public by default,
- de-identified derived features may be used for analysis,
- participation is voluntary,
- they can withdraw according to the withdrawal policy,
- they should avoid perfumes/scented products if VOC channels are active,
- this study does not claim to measure their emotions or intentions.

## Participant ID Rules

- Use participant IDs such as `H001`, `S014`, or `OP002`.
- Store the participant ID mapping outside git.
- Do not place names, phone numbers, emails, or consent forms in this repository.
- Do not include faces, voices, or raw participant media in public releases unless explicitly consented and reviewed.

## Draft Plain-Language Consent Text

```text
You are invited to take part in a research protocol design study about plant physiological measurements during standardized human-plant interaction. During the session, you may be asked to read a short script and/or touch a plant in a specified way for about 60 seconds.

The study may record video, audio, touch-pressure information, room microclimate, and plant sensor data. These recordings are used to verify timing, gesture, and data quality. The study is not designed to measure your emotions, thoughts, or intentions.

Raw video, audio, and identifiable participant information will be stored separately from public project files. Public project materials may include de-identified metadata, derived features, analysis code, and summary results. You may ask questions before participating and may withdraw according to the study withdrawal policy.
```

## Withdrawal Policy Placeholder

Before human data collection, fill in:

```text
Withdrawal contact:
Withdrawal deadline:
Data already included in aggregate analysis:
Raw media deletion procedure:
Derived feature deletion procedure:
Institutional/ethics review identifier, if any:
```

## Public Release Rule

Public release is allowed only for:

- synthetic data,
- de-identified metadata,
- de-identified derived feature tables,
- aggregate summaries,
- code and protocol documents.

Public release is not allowed for:

- raw video,
- raw audio,
- consent forms,
- participant identity maps,
- unreviewed raw human-session sensor streams.

