<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="180" viewBox="0 0 1200 180">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0a2e1a;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#0d3d22;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0a2e1a;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="1200" height="180" fill="url(#grad)" rx="0"/>
  <polygon points="0,130 1200,80 1200,180 0,180" fill="#00E87A" opacity="0.15"/>
  <polygon points="0,150 1200,110 1200,180 0,180" fill="#00E87A" opacity="0.1"/>
  <text x="600" y="90" font-family="Arial" font-size="58" font-weight="bold" fill="#00E87A" text-anchor="middle">EcoCore AI</text>
  <text x="600" y="130" font-family="Arial" font-size="22" fill="#ffffff" text-anchor="middle" opacity="0.9">AI-Powered Industrial Energy &amp; Carbon Optimization</text>
</svg>

# 🌿 EcoCore AI
### AI-Powered Industrial Energy & Carbon Optimization

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![MIT License](https://img.shields.io/badge/License-MIT-00E87A?style=for-the-badge)](LICENSE)

<br/>

**An AI-powered system that monitors industrial energy consumption, predicts carbon emissions, and gives actionable recommendations — helping factories cut costs and reduce their carbon footprint.**

<br/>

📄 **[View Full Idea Pitch →](./ecocore_pitch_v3.pdf)**

</div>

---

## 📌 Overview

EcoCore AI is built for small and medium-scale manufacturing industries that have **no visibility** into their real-time energy usage. The system uses Machine Learning to predict energy consumption and carbon emissions, then displays everything on an interactive **Streamlit dashboard** with clear recommendations for operators.

---

## 🚨 Problem

Most factories in India operate without any intelligent energy monitoring:

- ❌ No real-time visibility into energy usage
- ❌ No carbon emission tracking
- ❌ No predictive analysis — problems are noticed too late
- ❌ High electricity costs with no way to optimize

---

## ✅ Solution

| Feature | Description |
|--------|-------------|
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
| Model Training | Jupyter Notebook |
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



```
✅ Up to 25–30% reduction in energy wastage
✅ Real-time CO₂ emission visibility
✅ Simplified compliance reporting
✅ Immediate cost savings from day 1
```

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

**Built for NIT Surat · ASHINE Hackathon 2026**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NIT Surat Hackathon](https://img.shields.io/badge/NIT%20Surat-ASHINE%202026-00E87A?style=for-the-badge)

<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="120" viewBox="0 0 1200 120">
  <defs>
    <linearGradient id="footerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0a2e1a;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#0d3d22;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0a2e1a;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="1200" height="120" fill="url(#footerGrad)"/>
  <polygon points="0,0 1200,50 1200,0" fill="#00E87A" opacity="0.15"/>
  <polygon points="0,0 1200,30 1200,0" fill="#00E87A" opacity="0.1"/>
  <text x="600" y="80" font-family="Arial" font-size="18" fill="#00E87A" text-anchor="middle" font-weight="bold">🌿 EcoCore AI — Saving Energy, Saving the Planet</text>
</svg>

</div>
