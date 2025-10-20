import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Setup ---
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

st.title("🦠 CORD-19 Research Data Explorer")
st.write("""
This app allows basic exploration of COVID-19 research papers 
from the **CORD-19 dataset**. Use the filters below to explore 
trends in publications, journals, and research focus.
""")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df.dropna(subset=['title', 'abstract'], inplace=True)
    return df

df = load_data()

# --- Sidebar ---
st.sidebar.header("Filter Options")
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider("Select Year Range", year_min, year_max, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# --- Stats ---
st.write(f"### Total Papers: {len(filtered_df):,}")
st.write(f"Selected years: {year_range[0]} - {year_range[1]}")

# --- Visualization 1: Publications Over Time ---
st.subheader("📈 Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# --- Visualization 2: Top Journals ---
st.subheader("🏛️ Top 10 Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# --- Visualization 3: Abstract Word Count Distribution ---
st.subheader("🧩 Abstract Word Count Distribution")
filtered_df['abstract_word_count'] = filtered_df['abstract'].apply(lambda x: len(str(x).split()))
st.line_chart(filtered_df['abstract_word_count'].value_counts().sort_index())

# --- Show Data Sample ---
st.subheader("📄 Sample Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'publish_time']].head(15))
