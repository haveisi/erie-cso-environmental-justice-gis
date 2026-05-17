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

## Project Overview

...

## Project Significance

This project demonstrates how GIS and spatial automation can support environmental justice analysis by identifying overlaps between aging wastewater infrastructure, socially vulnerable populations, historical disinvestment patterns, and flood-prone areas.

## Research Questions

...

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
<img width="895" height="548" alt="image" src="https://github.com/user-attachments/assets/49ac9d78-2922-4633-aeda-45e7a60ab13e" />

### Figure 3 — Environmental Justice Vulnerability and CSO Exposure

Composite EJ vulnerability index based on poverty, renter occupancy, and nonwhite population.
<img width="905" height="517" alt="image" src="https://github.com/user-attachments/assets/ab77780b-e78e-4d1e-9656-571a18a9ae19" />

### Figure 4 — Flood Risk and CSO Exposure

Overlay of FEMA flood-prone areas and CSO exposure zones.
<img width="900" height="539" alt="image" src="https://github.com/user-attachments/assets/c832bb21-726f-410c-a7e8-7edbcc1cb3e3" />

### Figure 5 — Spatial Concentration of CSO Intensity

Kernel density estimation of cumulative CSO overflow intensity.
<img width="1196" height="818" alt="image" src="https://github.com/user-attachments/assets/24806cb6-c1c3-43d0-aaf0-e943d716d7d5" />

### Figure 6 — Census Tract Burden of CSO Exposure

Classification of census tracts based on CSO exposure burden.
<img width="922" height="505" alt="image" src="https://github.com/user-attachments/assets/e16ceec9-c303-42f2-b01d-9deb70b3017c" />

---

## ArcPy Workflow
## ArcPy Workflow

Raw Data  
↓  
Data Cleaning  
↓  
Buffer Analysis  
↓  
Spatial Join & EJ Analysis  
↓  
Kernel Density Hotspot Analysis  
↓  
Summary Statistics  
↓  
Automated Figure & Table Export


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

## Key Findings

Figures and statistical outputs are stored in:

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
## Key Findings

- Historically redlined neighborhoods show higher overlap with CSO exposure zones.
- Census tracts near CSO infrastructure exhibit elevated poverty and renter occupancy rates.
- Spatial hotspot analysis identifies concentrated CSO intensity near central Erie infrastructure corridors.
- Flood-prone areas substantially intersect with CSO exposure buffers, indicating compounding infrastructure vulnerability..

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
