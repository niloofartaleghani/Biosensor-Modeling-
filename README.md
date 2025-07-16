## 🧪 Lactate-Biosensor-Modeling

Numerical modeling of amperometric biosensors for detecting L-lactate under uncompetitive inhibition using explicit finite difference methods.
This repository accompanies the research article “Numerical modeling of L-lactate biosensors with uncompetitive inhibition using Explicit Finite Difference schemes”, which introduces a mechanistically justified and computationally efficient framework for simulating electrochemical biosensors used in point-of-care testing (POCT) for conditions like sepsis.
We simplify the ping-pong bi-bi enzymatic kinetics under oxygen-saturated conditions and incorporate a physically realistic uncompetitive inhibition model accounting for interferents such as ascorbic acid. The resulting partial differential equation (PDE) system captures the spatial and temporal evolution of substrate, product, and inhibitor concentrations within the sensor membrane.

This repository contains:
Python code for solving the dimensionless PDEs using explicit finite difference
Generated figures demonstrating substrate/inhibitor dynamics and sensor responses
Data files and parameter sets used in the study
This open-source framework aims to support future development of biosensor models in clinical diagnostics and biomedical engineering.

**Published Work**
Design and Model-Guided Optimization of a Novel Point-of-Care Lactate Biosensor
Niloofar Taleghani, Nastaran Taleghani, Vikramaditya G. Yadav

Department of Chemical and Biological Engineering, The University of British Columbia, Vancouver, BC V6T 1Z3, Canada

## Highlights

- Implements the ping-pong Bi-Bi enzymatic kinetics for lactate oxidase (LOx)
- Simplifies the model under **oxygen-rich conditions**, treating O₂ as saturating
- Models **ascorbic acid (vitamin C)** as an **uncompetitive inhibitor**, relevant for sepsis patients
- Solves the substrate-product-inhibitor PDE system using **explicit second-order finite difference**
- Visualizes substrate/inhibitor profiles and biosensor current response
- Enables parameter sweeps for sensor optimization

---


https://doi.org/10.1016/j.talanta.2024.126668
