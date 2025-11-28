# Ecostrain — Microbial Stress-Response Evolution Model

Ecostrain is a simulation and analysis project that explores how microbial populations adapt to environmental stressors such as temperature, pH, toxins, and nutrient scarcity.  
The project models stress-induced mutation patterns, survival probabilities, and population-level evolutionary trajectories over multiple generations.

This project is part of a 6-project computational evolution portfolio (BioSpire, EcoLens, Ecostrain, EON, GeneFlux, GeneScopeX).

---

## 🌱 Scientific Motivation
Microorganisms continuously face fluctuating and harsh environments.  
Ecostrain answers key biological questions:

- How do microbes adapt when exposed to long-term stress?
- Which mutations become dominant under environmental pressure?
- How does stress intensity affect population survival and diversity?
- Can we predict evolutionary bottlenecks or population collapse?

---

## 🔬 Core Features
- Stress-response mutation engine  
- Survival probability modelling  
- Multi-generation evolution simulation  
- Heatmaps, stress-fitness curves, and diversity plots  
- Log files capturing evolutionary history  
- Modular, easy-to-extend Python architecture  

---

## 📁 Folder Structure

code/
ecostrain_seq.py
stress_engine.py
survival_model.py
run_ecostrain_plot.py
helper_functions.py
example_microbe.fasta

graphs/
stress_fitness_curve.png
diversity_heatmap.png

logs/
ecostrain_log.json
final_population_stats.txt

yaml
Copy code

---

## ▶️ How to Run

### **1. Install Python**
python --version

markdown
Copy code

### **2. Install dependencies**
pip install numpy matplotlib

scss
Copy code

(Install Biopython if your sequence file uses FASTA:)
pip install biopython

markdown
Copy code

### **3. Run the simulation**
python code/run_ecostrain_plot.py

yaml
Copy code

This will:
- Run multi-generation evolution  
- Apply stress-based selection  
- Generate visualizations  
- Save logs and final statistics  

Outputs appear in:

- `graphs/`
- `logs/`

---

## 📊 Generated Outputs
- **stress_fitness_curve.png** — How stress level affects fitness over generations  
- **diversity_heatmap.png** — Mutation diversity under different stress intensities  
- **final_population_stats.txt** — Best strain characteristics  
- **ecostrain_log.json** — Detailed event-by-event evolutionary log  

---

## 🎓 Reviewer Notes (Admissions Friendly)
Ecostrain demonstrates:
- understanding of real microbial stress biology  
- analytical thinking and computational modelling  
- clean code practices and modular architecture  
- ability to generate and interpret scientific visualizations  

This project complements BioSpire and EcoLens by focusing on **population-level evolution under stress**, bridging computational biology with environmental microbiology.

---

## 🔗 Portfolio Link  
Complete 6-project evolution research collection:  
https://west-route-a3b.notion.site/BioGraph-Evolution-Research-Portfolio-2b69325d1ab1804dab15f731b8af6581?source=copy_link

