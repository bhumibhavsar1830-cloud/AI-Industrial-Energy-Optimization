<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00E87A&height=180&section=header&text=EcoCore%20AI&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI-Powered%20Industrial%20Energy%20%26%20Carbon%20Optimization&descAlignY=58&descAlign=50" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![MIT License](https://img.shields.io/badge/License-MIT-00E87A?style=for-the-badge)](LICENSE)

**An AI-powered system that monitors industrial energy consumption, predicts carbon emissions, and gives actionable recommendations — helping factories cut costs and reduce their carbon footprint.**

📄 **[View Full Idea Pitch →](./ecocore_pitch_v3.pdf)**

</div>

---

## 📌 Overview

EcoCore AI is built for small and medium-scale manufacturing industries that have **no visibility** into their real-time energy usage. The system uses Machine Learning to predict energy consumption and carbon emissions, then displays everything on an interactive **Streamlit dashboard** with clear recommendations for operators.

---

## 🚨 Problem

- ❌ No real-time visibility into energy usage
- ❌ No carbon emission tracking
- ❌ No predictive analysis — problems are noticed too late
- ❌ High electricity costs with no way to optimize

---

## ✅ Solution

| Feature | Description |
|---------|-------------|
| ⚡ **Energy Monitoring** | Tracks real-time energy consumption per machine |
| 🧠 **AI Prediction** | Predicts peak usage hours and emission spikes |
| 🎯 **Recommendations** | Tells operators exactly what action to take |
| 📊 **Dashboard** | Interactive Streamlit charts and trend views |
| 📋 **Compliance Reports** | Auto-generated BEE & ISO 50001 aligned reports |
| 💰 **ROI Tracker** | Shows cost savings and emission reduction in real time |
| ☁️ **SaaS Model** | Cloud-based platform, no hardware installation needed |
| 🏭 **B2B Focus** | Sold directly to factories and manufacturing industries |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| Dashboard | Streamlit |
| ML / AI | Scikit-learn, Pandas, NumPy |
| Serialized Model | carbon_model.pkl |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
AI-Industrial-Energy-Optimization/
│
├── app/
│   ├── app1.py              ← Streamlit dashboard (main app)
│   ├── carbon_model.pkl     ← Trained ML model
│   └── requirements.txt     ← Python dependencies
│
├── data/
│   ├── energy_data.csv      ← Industrial energy sensor dataset
│   └── train_model.py       ← Training script
│
├── ml_model/
│   ├── train_model.py       ← Training script
│   └── carbon_model.pkl     ← Trained ML model
│
├── ecocore_pitch_v3.pdf     ← Full idea pitch document
├── LICENSE
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/bhumibhavsar1830-cloud/AI-Industrial-Energy-Optimization.git
cd AI-Industrial-Energy-Optimization
```

**2. Install dependencies**
```bash
cd app
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app1.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 🧠 How It Works

```
Factory Sensor Data (CSV)
        ↓
Data Preprocessing (Pandas)
        ↓
Random Forest ML Model
        ↓
Energy & Carbon Predictions
        ↓
Streamlit Dashboard + Recommendations
```

---

## 🧠 ML Model

- **Algorithm** — Random Forest Regressor
- **Predicts** — Energy Consumption (kWh) + Carbon Emissions (kg CO₂)
- **Input Features** — Machine type, operating hours, load %, temperature, time of day
- **Training** — Run `ml_model/train_model.py` → auto generates `app/carbon_model.pkl`
- **Evaluation** — MAE, RMSE, R² Score

---

## 💼 Business Model

EcoCore AI follows a **SaaS + B2B** approach:

| Model | Details |
|-------|---------|
| ☁️ **SaaS** | Cloud-based platform — factories subscribe monthly/annually, no hardware needed |
| 🏭 **B2B Direct Sales** | Sold to manufacturing plants, factory managers, and industrial groups |
| 🤝 **Consulting Add-On** | Energy audit + optimization consulting for premium clients |
| 🏛️ **Govt Partnerships** | Alignment with BEE (Bureau of Energy Efficiency) and MSME schemes |
| 📦 **Licensing** | White-label licensing to large industrial corporations |

> **Target Market** — Small & Medium Manufacturing Industries across India

---

## 📈 Impact

- ✅ Up to 25–30% reduction in energy wastage
- ✅ Real-time CO₂ emission visibility
- ✅ Simplified compliance reporting
- ✅ Immediate cost savings from day 1

---

## 🗺️ Roadmap

- [x] ML model training & serialization (`train_model.py` → `carbon_model.pkl`)
- [x] Streamlit interactive dashboard
- [x] CSV data pipeline
- [ ] IoT / MQTT real-time sensor feed
- [ ] Multi-factory support
- [ ] Cloud deployment on Streamlit Cloud
- [ ] Mobile-friendly interface

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NIT Surat Hackathon](https://img.shields.io/badge/NIT%20Surat-ASHINE%202026-00E87A?style=for-the-badge)

<img src="https://capsule-render.vercel.app/api?type=waving&color=00E87A&height=120&section=footer&text=Saving%20Energy%20%7C%20Saving%20the%20Planet%20%7C%20EcoCore%20AI&fontSize=18&fontColor=ffffff&fontAlignY=65&animation=fadeIn" width="100%"/>

</div>
