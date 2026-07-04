# Literature Map

Last updated: 2026-07-04

## 1. Plant Electrical Signaling

Plant electrical signals are real and useful. Action potentials, variation potentials, slow wave potentials, and local voltage changes can reflect wounding, touch, abiotic stress, and environmental transitions. The challenge is that plant electrical recordings are slow, noisy, and highly sensitive to electrode condition, humidity, light, and movement.

Key sources:

- [A library of electrophysiological responses in plants](https://pmc.ncbi.nlm.nih.gov/articles/PMC10950275/)
- [Electrical Signaling of Plants under Abiotic Stressors](https://pmc.ncbi.nlm.nih.gov/articles/PMC8509212/)
- [Plant electrophysiology with conformable organic electronics](https://pmc.ncbi.nlm.nih.gov/articles/PMC10371018/)

Design use:

- Record multi-hour baselines before interpreting 60 second events.
- Measure electrode impedance and contact condition.
- Use a Faraday shield or at least document electromagnetic noise sources.
- Include object-touch and human-nearby controls.

## 2. Touch, Mechanostimulation, And Thigmomorphogenesis

Plants sense mechanical stimulation. Touch can alter calcium signaling, phosphorylation, gene expression, morphology, defense priming, and growth allocation. This is the strongest rationale for measuring "petting" as a biological stimulus. It is also the strongest reason that human touch differences must be measured carefully.

Key sources:

- [In touch: plant responses to mechanical stimuli](https://doi.org/10.1111/j.1469-8137.2004.01263.x)
- [Plant Responses to Brief Touching](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165742)
- [TREPH1 touch response, PNAS](https://www.pnas.org/doi/abs/10.1073/pnas.1814006115)
- [Touch signaling and thigmomorphogenesis, Science Advances](https://www.science.org/doi/10.1126/sciadv.abm2091)
- [Pavement cells distinguish touch from letting go](https://pubmed.ncbi.nlm.nih.gov/37188852/)

Design use:

- Log touch onset, release, stroke direction, contact area, and pressure.
- Treat pressure glove data as a primary covariate, not a nice-to-have.
- Use an object or robot touch to estimate mechanical artifacts.

## 3. Wound, Calcium, And Defense Signaling

Wounding is not the same as gentle petting, but it provides a well-characterized positive-control domain. Work on glutamate receptor-like channels and long-distance calcium waves shows that plants can rapidly coordinate systemic responses without nerves.

Key sources:

- [Mousavi et al. 2013](https://pubmed.ncbi.nlm.nih.gov/23969459/)
- [Toyota et al. 2018](https://www.science.org/doi/10.1126/science.aat7744)

Design use:

- Include a positive control only if it does not compromise the longitudinal plant.
- If using a positive-control plant, keep it separate from the main familiar/stranger specimen.

## 4. VOCs And Electronic Noses

Plants emit volatile organic compounds related to growth, defense, disease, mechanical damage, and environmental conditions. E-nose systems can classify some plant VOC signatures, but they are vulnerable to humidity, airflow, sensor drift, and human odor contamination.

Key sources:

- [Discrimination of Plant Volatile Signatures by an Electronic Nose](https://pubmed.ncbi.nlm.nih.gov/19068829/)
- [USDA/ARS review of e-nose plant pest detection](https://www.ars.usda.gov/research/publications/publication/?seqNo115=349614)
- [Sensors review](https://www.mdpi.com/1424-8220/18/2/378)

Design use:

- Separate plant VOC sampling from human breath/body odor where possible.
- Use clean-air blanks before and after sessions.
- Consider periodic GC-MS validation if the e-nose becomes central to claims.

## 5. Plant Bioacoustics

Recent work supports airborne ultrasonic emissions from stressed plants such as tomato and tobacco under dehydration or cutting conditions. This does not imply plants "talk" in a human sense, but it supports ultrasonic recording as a possible stress-state channel.

Key sources:

- [Sounds emitted by plants under stress are airborne and informative](https://www.cell.com/cell/fulltext/S0092-8674%2823%2900262-3)
- [EurekAlert summary](https://www.eurekalert.org/news-releases/983739)

Design use:

- Record ultrasonic audio if stress emissions are a target.
- Separate plant emissions from fabric, glove, room, HVAC, and mouth sounds.

## 6. Sap Flow And Water Relations

Sap-flow methods are established in plant ecophysiology, especially for woody stems and trees. Thermal dissipation probes can be invasive and may be poorly matched to a small potted houseplant or to fast 60 second event detection.

Key sources:

- [Lu, Urban, Zhao 2004 record](https://hero.epa.gov/reference/5794015/)
- [Dynamax TDP overview](https://dynamax.com/products/transpiration-sap-flow/tdp-sap-velocity-thermal-dissipation-probe)
- [USFS caveat on thermal-dissipation consistency](https://research.fs.usda.gov/treesearch/36210)

Design use:

- Make sap flow optional unless the selected species has suitable stem geometry.
- Consider pot mass, leaf gas exchange, or stem diameter variation as less invasive water-status alternatives.

## 7. Human-Plant Bioelectric Interaction Claims

There are recent exploratory studies and preprints on plant bioelectric changes during human movement or presence. They are relevant as hypothesis-generating work, but they do not yet establish familiar-human recognition or emotional communication. Treat them as design inspiration, not as confirmatory evidence.

Key sources:

- [Can Plants Sense Humans?](https://pmc.ncbi.nlm.nih.gov/articles/PMC10422342/)
- [Machine learning plant bioelectric recordings with human movement, MIT DSpace](https://dspace.mit.edu/handle/1721.1/164094)
- [Plant Bioelectric Early Warning Systems, arXiv](https://arxiv.org/abs/2506.04132)

Design use:

- Include rigorous negative controls and grouped holdouts.
- Treat unusually high classifier performance as a leakage warning until proven otherwise.

## 8. Plant Sentience And Consciousness Debate

The repo does not need to settle plant sentience. It only needs to measure whether condition labels predict plant physiology under strong controls. Avoid language that equates plant signals with pain, feelings, recognition, or preference unless future evidence justifies it.

Key sources:

- [Plants Neither Possess nor Require Consciousness](https://www.cell.com/trends/plant-science/fulltext/S1360-1385%2819%2930126-8)
- [Debunking a myth: plant consciousness](https://pmc.ncbi.nlm.nih.gov/articles/PMC8052213/)
- [A critical review of plant sentience](https://link.springer.com/article/10.1007/s10539-024-09953-1)

