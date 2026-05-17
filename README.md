````markdown
# Erie CSO Environmental Justice GIS Analysis

Spatial analysis of combined sewer overflow (CSO) exposure, environmental justice vulnerability, historical redlining, and flood risk in Erie, Pennsylvania using ArcGIS Pro and ArcPy automation.

---

## Project Overview

This project investigates how combined sewer overflow (CSO) infrastructure overlaps with socially vulnerable communities in Erie, Pennsylvania. The analysis integrates:

- CSO outfall locations
- Census tract demographic indicators
- Historical HOLC redlining maps
- FEMA flood risk zones
- Spatial hotspot analysis

The project combines GIS mapping, environmental justice analysis, and automated ArcPy workflows to produce reproducible spatial analysis outputs.

---

## Research Questions

- Which census tracts experience the highest CSO exposure burden?
- Do socially vulnerable communities face greater proximity to CSO infrastructure?
- How do historical redlining patterns overlap with CSO exposure?
- Where are spatial hotspots of CSO intensity located?
- How does flood risk intersect with CSO exposure zones?

---

## Methods

### Spatial Analysis

- 1 km CSO exposure buffer analysis
- Census tract spatial joins
- Kernel Density hotspot analysis
- Flood risk overlay analysis
- Environmental justice vulnerability indexing
- Historical HOLC redlining overlays

### Environmental Justice Indicators

The EJ vulnerability index includes:

- Poverty rate
- Percent nonwhite population
- Percent renter occupancy

### Automation

The workflow was automated using ArcPy:

- Buffer creation
- Spatial selections
- Summary statistics
- Automated figure exports
- Automated table exports

---

## Technologies Used

- ArcGIS Pro
- ArcPy
- Python
- ACS Census Data
- FEMA Flood Data
- HOLC Redlining Data

---

## Repository Structure

```text
erie-cso-environmental-justice-gis/
├── scripts/
│   └── erie_cso_model.py
├── outputs/
│   ├── figures/
│   └── tables/
├── layouts/
├── README.md
└── .gitignore
````

---

## Key Figures

### Figure 2 — Historical Redlining and CSO Exposure

Overlay of HOLC grades and 1 km CSO exposure zones.

### Figure 3 — Environmental Justice Vulnerability and CSO Exposure

Composite EJ vulnerability index based on poverty, renter occupancy, and nonwhite population.

### Figure 4 — Flood Risk and CSO Exposure

Overlay of FEMA flood-prone areas and CSO exposure zones.

### Figure 5 — Spatial Concentration of CSO Intensity

Kernel density estimation of cumulative CSO overflow intensity.

### Figure 6 — Census Tract Burden of CSO Exposure

Classification of census tracts based on CSO exposure burden.

---

## ArcPy Workflow

Main workflow script:

```python
scripts/erie_cso_model.py
```

The script automates:

1. CSO buffer generation
2. EJ exposure analysis
3. Spatial selection of exposed tracts
4. Summary statistics generation
5. Figure export automation
6. CSV table exports

---

## Outputs

### Figures

Located in:

```text
outputs/figures/
```

### Statistical Tables

Located in:

```text
outputs/tables/
```

Includes:

* exposed_stats.csv
* non_exposed_stats.csv

---

## Example Findings

Preliminary results suggest that census tracts located within CSO exposure zones exhibit:

* Higher poverty rates
* Higher renter occupancy
* Greater concentrations of socially vulnerable populations

The analysis also reveals spatial overlap between historical disinvestment patterns and contemporary infrastructure risk exposure.

---

## Future Improvements

* Add interactive dashboards
* Incorporate temporal overflow data
* Add stormwater volume modeling
* Integrate water quality indicators
* Expand ArcPy modularization and logging
* Develop reproducible geoprocessing toolbox

---

## Author

Dr. Hadi Veisi
University of Wisconsin–Stevens Point

Research areas:

* Environmental justice
* Climate resilience
* Infrastructure vulnerability
* Spatial analysis
* Sustainability transitions

```
```
