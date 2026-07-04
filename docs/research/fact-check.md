# Fact Check

Last updated: 2026-07-04

This document separates what plant science already supports from what the Pet the Plant study would need to demonstrate.

For the machine-readable source matrix used by CI, see [evidence-ledger.json](evidence-ledger.json). For a shorter prose summary, see [evidence-summary.md](evidence-summary.md).

## Bottom Line

Plants have rich, measurable signaling systems. They can respond to touch, wounding, humidity, light, sound vibration, chemical cues, and other stressors through electrical, calcium, hydraulic, hormonal, mechanical, volatile, and gene-expression pathways.

That does **not** mean the plant recognizes a familiar person, reads intention, or experiences emotion. The familiar-human question is currently best treated as exploratory and falsifiable.

Planet_Earthing has collected no plant-session data yet. Any claim about host-versus-stranger differences must be read as a planned test, not an observed result.

## Claim Table

| Claim | Current status | Notes for this repo | Sources |
|---|---|---|---|
| Plant electrical signals can be measured from leaves/stems and change after stimuli. | Supported | Use electrophysiology as a legitimate signal channel, but expect drift and environmental artifacts. | [Plant electrophysiology library](https://pmc.ncbi.nlm.nih.gov/articles/PMC10950275/), [abiotic stress review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8509212/), [conformable plant electrodes](https://pmc.ncbi.nlm.nih.gov/articles/PMC10371018/) |
| Mechanical touch can alter plant physiology. | Supported | This supports touch controls, not familiarity claims. Repeated touch can itself become a stress treatment. | [Braam 2005 review](https://doi.org/10.1111/j.1469-8137.2004.01263.x), [brief touching in potato](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165742), [TREPH1 touch response](https://www.pnas.org/doi/abs/10.1073/pnas.1814006115), [Science Advances touch signaling](https://www.science.org/doi/10.1126/sciadv.abm2091) |
| Plant cells can distinguish touch onset from touch release. | Supported in specific experimental systems | Useful for designing event markers around touch start and stop. Do not generalize to human recognition. | [PubMed: pavement cells distinguish touch from letting go](https://pubmed.ncbi.nlm.nih.gov/37188852/) |
| Wounding can trigger long-distance electrical/calcium/defense signaling. | Supported | Include wound or heat stimulus as a positive control only if ethically and practically appropriate for plants. | [Mousavi et al. 2013](https://pubmed.ncbi.nlm.nih.gov/23969459/), [Toyota et al. 2018](https://www.science.org/doi/10.1126/science.aat7744) |
| Stressed plants can emit airborne ultrasonic sounds. | Supported for tested species/stressors | Audio should include ultrasonic recording if this modality is central. Expect stress-state specificity. | [Cell 2023 plant sounds](https://www.cell.com/cell/fulltext/S0092-8674%2823%2900262-3), [EurekAlert summary](https://www.eurekalert.org/news-releases/983739) |
| Electronic noses can discriminate some plant VOC signatures. | Supported with limitations | E-nose data are confound-prone: ambient VOCs, human odor, cleaning products, airflow, and humidity matter. Validate with GC-MS if possible. | [ACS e-nose study](https://pubmed.ncbi.nlm.nih.gov/19068829/), [USDA/ARS review](https://www.ars.usda.gov/research/publications/publication/?seqNo115=349614), [Sensors review](https://www.mdpi.com/1424-8220/18/2/378) |
| Thermal sap-flow methods can quantify plant water transport. | Supported for suitable stems/trunks, with caveats | A thermal dissipation probe may be inappropriate for a small houseplant. Use only when stem size and wounding risk are acceptable. | [EPA HERO record for Lu et al. 2004](https://hero.epa.gov/reference/5794015/), [USFS multi-year caveat](https://research.fs.usda.gov/treesearch/36210) |
| Mimosa pudica can habituate to repeated disturbance. | Plausible but debated | Relevant to habituation/sensitization, but it does not imply sentience or person recognition. Replication and behavioral definitions matter. | [Gagliano et al. abstract](https://pubmed.ncbi.nlm.nih.gov/24390479/), [Learning in Plants review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4814444/), [field study](https://www.cambridge.org/core/journals/journal-of-tropical-ecology/article/memory-and-habituation-to-harmful-and-nonharmful-stimuli-in-a-field-population-of-the-sensitive-plant-mimosa-pudica/FF81969C25326848890AA22B1D1F5780) |
| Backster-style "primary perception" or response to remote human intention is established. | Unsupported | Controlled attempts failed to replicate the brine-shrimp killing claim. Do not cite Backster as evidence for the hypothesis. | [Science replication abstract](https://pubmed.ncbi.nlm.nih.gov/17781887/), [Science DOI](https://www.science.org/doi/10.1126/science.189.4201.478) |
| Plants are conscious or sentient in the animal-like sense. | Unsupported as a working scientific assumption | The repo can investigate plant signaling without claiming consciousness, pain, emotion, or intention. | [Plants Neither Possess nor Require Consciousness](https://www.cell.com/trends/plant-science/fulltext/S1360-1385%2819%2930126-8), [Debunking a myth: plant consciousness](https://pmc.ncbi.nlm.nih.gov/articles/PMC8052213/), [critical review of plant sentience](https://link.springer.com/article/10.1007/s10539-024-09953-1) |
| A plant can identify a familiar human from a stranger using only plant sensor data. | Exploratory | This is the core question. Any positive result must defeat pressure, odor, voice, CO2, heat, schedule, analyst leakage, and person-identity artifacts. | [Human movement biosensor pilot](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422342/), [MIT DSpace ML thesis/paper record](https://dspace.mit.edu/handle/1721.1/164094), [arXiv human-plant bioelectric program](https://arxiv.org/abs/2506.04132) |
| One plant over six months can prove the effect. | Unsupported | A single plant can debug instruments. It cannot support generalizable claims or separate plant-specific drift from condition effects. | Statistical design principle; see [analysis plan](../protocols/statistical-analysis-plan.md) |

## Design Implications

1. The repo should use plant electrophysiology language, not "galvanic skin response equivalent." Plants do not have skin or human-like sweat-gland physiology.
2. The main contrast should be phrased as "familiarity-associated signal differences," not "recognition" until alternative explanations are exhausted.
3. Host versus stranger is confounded by odor, voice, gait, breath CO2, radiant heat, microbiome, pressure, touch path, schedule, and experimenter expectations.
4. The strongest design includes host, repeated non-host, novel stranger, voice playback, robot/object touch, human nearby/no touch, and no-touch baselines.
5. Machine learning must use grouped holdouts. Random row-wise splits will almost certainly exaggerate performance.

## Revision To The Original Problem Statement

The original draft is a useful spark, but the confirmatory version should change these points:

- Replace "single plant specimen" with "instrumentation demo on one plant, confirmatory cohort on multiple plants."
- Replace "same species, age, size" with a documented plant inclusion protocol and plant-level random effects.
- Add a repeated non-host condition to separate "familiar person" from "the only person seen repeatedly."
- Add a human-nearby/no-touch control to separate touch from heat, CO2, VOCs, sound, and electromagnetic artifacts.
- Treat sap-flow probes as optional because they can wound small plants and may have insufficient time resolution for a 60 second interaction.
- Add ethics/consent language for human audio/video, pressure glove data, and potential human VOC traces.
