# 🚀 Flix Pricing Optimization System

A **production-style data pipeline + analytics dashboard** that detects pricing inefficiencies using clustering and delivers actionable insights through an interactive UI.

---

## 📌 Project Overview

The **Flix Pricing Optimization System** analyzes large-scale pricing data (~800K+ records) to:

* Identify **overpriced and underpriced items**
* Generate **recommended prices**
* Segment data using **clustering (unsupervised ML)**
* Provide **business insights via dashboards and reports**

---

## 🎯 Key Features

### 🔍 Data Processing Pipeline

* Handles large datasets efficiently (800K+ rows)
* Data cleaning and preprocessing
* Feature engineering for pricing insights

### 🧠 Machine Learning

* Clustering-based segmentation (K-Means)
* Price deviation detection
* Intelligent price recommendations

### 📊 Reporting System

* Excel report with:

  * Summary sheet
  * Flagged cases (High / Low pricing)
  * Sample dataset
* Optimized for performance (avoids heavy Excel crashes)

### 🌐 Interactive Dashboard (Streamlit)

* KPI Cards (High / Low / Optimal pricing)
* Pie chart (price distribution)
* Scatter plot (price vs recommended)
* Cluster visualization
* Sidebar filters
* Data preview table

---

## 🏗️ Project Structure

```
flix_pricing_system/
│
├── main.py                  # Data pipeline & ML logic
├── dashboard.py             # Streamlit UI dashboard
├── requirements.txt         # Dependencies
│
├── outputs/
│   ├── results.xlsx         # Lightweight report
│   └── full_data.csv        # Complete dataset
│
├── data/                    # Raw input data (optional)
└── .venv/                   # Virtual environment
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/manojpm181/flix-pricing-system.git
cd flix-pricing-system
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Step 1: Run Data Pipeline

```
python main.py
```

✅ Generates:

* `outputs/full_data.csv`
* `outputs/results.xlsx`

---

### 🔹 Step 2: Launch Dashboard

```
streamlit run app/streamlit_app.py
```

🌐 Open in browser:

```
http://localhost:8501
```

---

## 📊 Dashboard Preview

### Features:

* 📌 KPI Metrics (High / Low / Optimal)
* 📊 Price Distribution (Pie Chart)
* 📈 Price vs Recommended Scatter Plot
* 🧠 Cluster Analysis
* 🔍 Dynamic Filters
* 📋 Data Table

---

## 🧠 Technical Stack

| Layer         | Technology            |
| ------------- | --------------------- |
| Language      | Python                |
| Data          | Pandas, NumPy         |
| ML            | Scikit-learn (KMeans) |
| Visualization | Plotly                |
| Dashboard     | Streamlit             |
| Reporting     | OpenPyXL              |

---

## ⚡ Performance Optimizations

* Avoids Excel overload by limiting rows
* Stores full dataset in CSV format
* Uses caching (`@st.cache_data`) for fast UI
* Reduces memory-heavy formatting operations

---

## 🚨 Challenges Solved

### ❌ Large Dataset Handling

✔ Optimized processing for 800K+ rows

### ❌ Excel Memory Crash

✔ Limited export + CSV separation

### ❌ Disk Space Issues

✔ Redirected temp storage & reduced file size

### ❌ Slow UI Rendering

✔ Sampling + caching used

---

## 💡 Business Impact

* Identifies **revenue leakage**
* Improves **pricing strategy**
* Enables **data-driven decisions**
* Scales to real-world datasets

---

## 📈 Future Enhancements

* 🔮 AI-based dynamic pricing (real-time)
* 📡 API integration
* ☁️ Cloud deployment (AWS / GCP)
* 📊 Advanced analytics (forecasting)
* 🔐 Role-based dashboard access

---

## 👨‍💻 Author

**Manoj PM**
B.E. CSE
manojpoojari1511@gmail.com

---
## Result
<img width="1915" height="690" alt="Screenshot 2026-03-17 175533" src="https://github.com/user-attachments/assets/7a780d12-9eb2-4d9a-8240-9b0a5e547690" />
<img width="1497" height="621" alt="Screenshot 2026-03-17 175547" src="https://github.com/user-attachments/assets/8db258ab-9acf-4835-9f0d-2dfcdab352cc" />
<img width="1480" height="558" alt="Screenshot 2026-03-17 175603" src="https://github.com/user-attachments/assets/86507407-08aa-414e-b241-434a40c26c40" />
<img width="1434" height="562" alt="Screenshot 2026-03-17 175619" src="https://github.com/user-attachments/assets/091cde63-0f00-4e54-be8e-63e1acff5a92" />
<img width="1482" height="583" alt="Screenshot 2026-03-17 175629" src="https://github.com/user-attachments/assets/a431d2cb-ee0a-4de4-b378-2ab88d8a20b7" />
<img width="1472" height="530" alt="Screenshot 2026-03-17 175635" src="https://github.com/user-attachments/assets/20770f89-0db0-4e54-9426-8e7405bbf02a" />
<img width="1519" height="549" alt="Screenshot 2026-03-17 175642" src="https://github.com/user-attachments/assets/9ed62b89-b45f-4e28-bf23-7cd8623c79f1" />
<img width="1569" height="812" alt="Screenshot 2026-03-17 175702" src="https://github.com/user-attachments/assets/2d82f27a-f934-4441-b8ee-e560c8c897a2" />

---
## 🏁 Conclusion

This project demonstrates:

* End-to-end data pipeline design
* Machine learning integration
* Scalable data handling
* Interactive data visualization


⭐ If you found this useful, give it a star!
