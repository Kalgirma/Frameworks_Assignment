## 🧬 CORD-19 Data Explorer (Streamlit Project)

### Overview
This project analyzes the **CORD-19 (COVID-19 Open Research Dataset)** to explore global research trends related to COVID-19.  
It uses **Pandas**, **Matplotlib**, and **Streamlit** to clean, analyze, and visualize research paper metadata — including publication trends, top journals, and keyword frequencies.

---

### 🎯 Objectives
- Load and explore real-world research data  
- Clean and preprocess datasets  
- Visualize publication trends and journal activity  
- Build an interactive Streamlit dashboard  
- Present findings in a clear and accessible format  

---

### 📁 Project Structure
```
CORD19-Streamlit/
│
├── app.py                         # Streamlit main app
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
│
├── data/
│   └── metadata.csv  (Download link provided below)
│
├── analysis/
│   └── data_analysis.py           # Data cleaning and EDA script
│
└── docs/
    └── Reflection_Report_Part5.docx  # Learning reflection
```

---

### 📊 Dataset

This project uses the **CORD-19 (COVID-19 Open Research Dataset)** — a large collection (≈1 GB) of scholarly articles about COVID-19 and related coronaviruses.

Because of its size, the dataset is **not stored in this repository**.  
Please download it directly from the official source below:

> 🔗 **CORD-19 Dataset Download:**  
> [https://www.semanticscholar.org/cord19](https://www.semanticscholar.org/cord19)

After downloading, place the file in:
```
CORD19-Streamlit/data/metadata.csv
```

*(If you’ve preprocessed your own version, you may host it on Google Drive, Dropbox, or Kaggle and update the link above.)*

---

### ⚙️ Installation & Setup

#### 1. Create a virtual environment (optional but recommended)
```bash
python -m venv env
env\Scripts\activate   # On Windows
source env/bin/activate  # On macOS/Linux
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the Streamlit App
```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

### 📈 Features
- **Publications by Year:** visualize annual publication trends  
- **Top Journals:** identify the most active publishers  
- **Word Cloud:** highlight frequent keywords in paper titles  
- **Interactive Data Table:** preview a subset of the dataset  
- **Year Range Filter:** dynamically control displayed years  

---

### 🧰 Tools & Libraries
- **Python 3.8+**  
- **Pandas** – Data analysis  
- **Matplotlib / Seaborn** – Visualization  
- **WordCloud** – Keyword frequency visualization  
- **Streamlit** – Interactive web app framework  

---

### 🔍 Insights
- Research publications **peaked between 2020 and 2021** during the height of the pandemic.  
- Certain journals consistently dominated COVID-19 publishing.  
- Keyword trends emphasize topics like *SARS-CoV-2*, *infection*, and *vaccine*.  

---

### 🪞 Reflection
This project provided hands-on experience with:
- Real-world data analysis and cleaning  
- Building interactive dashboards using Streamlit  
- Structuring and visualizing research data effectively  

Full reflection available in `docs/Reflection_Report_Part5.docx`.

---

### 👤 Author
**Kalab Girma Mekuria**  
Independent Researcher & Junior Software Developer  
October 2025
