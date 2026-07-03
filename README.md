# Gen_matching_scripts

This directory contains the scripts used to match generator-level decays, apply FONLL weights, and calculate weighted and unweighted efficiencies for the CMS B-physics analysis.

## Workflow

```
Generator ROOT files
        │
        ▼
genmatcher_fully.py
        │
        ▼
Matched ROOT files
        │
        ▼
rdf_fonll_weight_applyer.py
        │
        ▼
weighted_root_files/
        │
        ▼
eff_checker.py
        │
        ▼
Efficiency summary + inclusive MiniAOD event counts
```

---

## Scripts

### `genmatcher_fully.py`

Matches generator-level decay chains within GENSIM ROOT files.

The script:

- Searches each generated event for the requested decay topology.
- Matches all requested decay products.
- Creates a new ROOT file containing only events with successfully matched decays.
- 
The output is used as the input for the weighting stage.

---

### `rdf_fonll_weight_applyer.py`

Applies FONLL production weights to the matched ROOT files.

The script:

- Reads the matched ROOT files.
- apllies the appropriate FONLL weight for each event.
- Stores the weighted ROOT files inside

```
weighted_root_files/
```

These weighted files are then used for efficiency calculations.

---

## `weighted_root_files`

Contains the FONLL-weighted ROOT files together with the efficiency calculation scripts.

### `eff_checker.py`

Calculates reconstruction efficiencies for both the weighted and unweighted samples.

The script:

- Computes efficiencies before and after applying FONLL weights.
- Reports the weighted and unweighted efficiencies.
- Returns the inclusive MiniAOD event count used in the efficiency calculation.

---

## Outputs

The workflow produces:

- Matched generator-level ROOT files
- FONLL-weighted ROOT files
- Weighted and unweighted efficiencies
- Inclusive MiniAOD event counts
