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
<img width="1312" height="782" alt="image" src="https://github.com/user-attachments/assets/4ae7a992-3fc5-4558-b846-2db5310677c2" />
![Figure23](outputs/figures/Fig.%203.png)

### Figure 3 — Environmental Justice Vulnerability and CSO Exposure

Composite EJ vulnerability index based on poverty, renter occupancy, and nonwhite population.
<img width="1341" height="749" alt="image" src="https://github.com/user-attachments/assets/4bca6a1e-99ac-4717-b803-3a171f3bc8a3" />

![Figure 3](outputs/figures/Fig.%203.png)

### Figure 4 — Flood Risk and CSO Exposure

Overlay of FEMA flood-prone areas and CSO exposure zones.

<img width="1330" height="777" alt="image" src="https://github.com/user-attachments/assets/820551d0-04fc-4cb8-a674-a264f1087a57" />

![Figure 4](outputs/figures/Fig.%203.png)

### Figure 5 — Spatial Concentration of CSO Intensity

Kernel density estimation of cumulative CSO overflow intensity.
<img width="1192" height="775" alt="image" src="https://github.com/user-attachments/assets/68f5f07b-4ff7-4b10-a5cd-6a09f35e3e82" />

![Figure 5](outputs/figures/Fig.%203.png)

### Figure 6 — Census Tract Burden of CSO Exposure

Classification of census tracts based on CSO exposure burden.
<img width="1317" height="709" alt="image" src="https://github.com/user-attachments/assets/79b2965b-97f8-4198-aa7f-6859ccca6fd3" />

![Figure 6](outputs/figures/Fig.%203.png)
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
