# 🚨 Community Risk Intelligence Agent  
### *AI-driven, event-aware community alerting system built with Google Gemini + ADK (Capstone Project)*

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-blue.svg)]()  
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

## 📌 Overview  

The **Community Risk Intelligence Agent** is an **event-driven multi-agent system** that:

- ⚠️ Detects community events (weather, air quality, fire, news, transport)  
- 🧠 Uses **Gemini** to classify risks  
- 🗂️ Stores structured memory + event chains  
- 👪 Notifies affected users based on location  
- 📝 Generates personalized guidance checklists  
- 🧪 Includes an evaluation harness comparing heuristic vs environmental scoring  
- 🛠️ Has **full CI integration** + modular Python package

---

## 🚨 Features
### ✔️ Event-Driven Architecture(EDA)
Uses ADK's `Event Bus` to handle:
- Raw incoming alerts
- Alerts
- Guidance generation

### ✔️ AI-Driven Classification
Each event is:
-Analyzed by Gemini
-Ranked 0-1
-Categorized (low/medium/high)
-Stored with explaination

### ✔️ Environmental Intelligence Add-On
Optimal environmental risk scoring using:
- PM2.5 + air quality
- Temperature extreme detection
- Humidity / wind threat modeling

### ✔️ Two Execution Modes
|**Mode**           | **LLM Used**                 |  **Purpose**                          |
|-----------------|-------------------------------|--------------------------------------|
|**Offline Mode** |     LocalStubLLM              |     Fast testing, CI, no API needed  |
|**Live Mode**    |     Gemini Flash / Flash Lite |     Final evaluation and deployment  |

### ✔️ Synthetic Scenario Test Harness
Evaluates impact of environmental data using structured synthetic events.

### ✔️ Notebook Evaluation Section
Produces:
- Detailed per-case comparison
- Baseline vs enriched scoring
- Charts (bar/line)
- JSONL evaluation logs

### ✔️ Full Project Package
Production-ready Python package with:
- CI workflow
- Automated notebook execution tests
- Unit tests
- MIT license
- Banner + badges

---

## 🧩 Architecture
### High-Level Agent Flow
```
 ┌────────────────┐        ┌─────────────────────┐
 │  Data Agent    │        │  Risk Analysis Agent │
 │ (Event Source) │ ───▶   │ (Gemini / Local LLM) │
 └────────────────┘        └──────────┬───────────┘
                                      │ alert
                                      ▼
                       ┌─────────────────────────┐
                       │     Community Agent     │
                       │ (User Matching + Notify)│
                       └──────────┬──────────────┘
                                  │
                                  ▼
                        ┌──────────────────────┐
                        │     Guide Agent      │
                        │ (Gemini Checklist)   │
                        └──────────────────────┘
```

---

## 🌐 Modes of Operation

### **1. Offline Mode (LocalStubLLM)**
- Runs anywhere (safe mode)  
- Deterministic outputs  
- Ideal for CI & offline testing  

### **2. Live Mode (Gemini)**
Uses Google’s:
- `gemini-2.5-flash-lite`  
- ADK session runtime  
- Real-time risk scoring + guidance  

To enable:
```python
import os
os.environ["GOOGLE_API_KEY"] = "YOUR_KEY_HERE"
```
---

## 📚 Files Included
### 📝 Main Notebook
- `community-risk-intelligence-agent_patched.ipynb`
  ✔️ Final polished notebook
  ✔️ Auto-detects whether project_package is available
  ✔️ Fully compatible with Kaggle + GitHub Actions

---

### 📁 Project Package
`project_package_bundle.zip` includes:
```
project_package/
└── agents.py
└── __init__.py
└── tests/
    └── test_agents_module.py
```
Purpose:
- Makes code **modular & testable**
- Enables reuse across notebooks
- Required for CI import tests

---

### ⚙️ CI Files
`ci_files_bundle.zip` includes:
```
.github/workflows/ci.yml
requirements-ci.txt
pytest.ini
tests/
    └── run_notebook_tests.py
```
CI Features:
- Runs notebook import smoke tests
- Tests LocalStubLLM classification
- Creates required runtime directories
- Skips Gemini tests automatically if no API key
- Ensures build reproducibility


---

## 🧪 Evaluation Summary

Synthetic test cases demonstrate clear improvement when environmental metadata is included.

| **Case**        | **Baseline Score** |    **Env Score**  |     **Result**                 |
|---------------|--------------------|-------------------|--------------------------------|
| clean_air	    |      low	         |         low	     |         same severity          |
| moderate_pm	  |      low	         |         higher	   |         better sensitivity     |
| high_pm	      |      low	         |         medium	   |         correctly upgraded     |
| extreme_heat	|      low	         |         higher	   |         reasonable increase    |
| high_humidity |	     low	         |         higher	   |         medium sensitivity     |
| windy	        |      low	         |         higher	   |         more realistic ranking |

JSONL output saved to:
```
agent_memory/compare_results.jsonl
```

### Key Insight 🚀
The agent correctly **elevates PM-heavy scenarios** while ignoring non-dangerous variation — demonstrating intelligent environmental risk reasoning.

---

## ▶️ Running the Notebook
### Offline (safe mode)
Just run all cells — no API key needed.
### Live (Gemini mode)
Set your key:
```python
import os
os.environ["GOOGLE_API_KEY"] = "YOUR_KEY"
```
Then run the notebook.
Risk analysis + guidance will use **Gemini 2.5 Flash Lite**.

---

## 📄 License
MIT License — free to use, modify, and distribute.

---

## 👤 Author
**Md Kamran Akhter**
