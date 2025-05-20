import streamlit as st
import pandas as pd
from app.utils import load_country_data, plot_metric_boxplot, generate_summary_table, plot_country_ranking

st.set_page_config(page_title="Solar Challenge Dashboard", layout="wide")

st.title("🌞 Cross-Country Solar Potential Dashboard")

# Sidebar filters
st.sidebar.header("Select Options")
countries = ["Benin", "Togo", "Sierraleone"]
selected_countries = st.sidebar.multiselect("Choose Countries", countries, default=countries)
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Load data
data = load_country_data(selected_countries)

if not data.empty:
    st.subheader(f"📊 Boxplot of {metric} by Country")
    st.pyplot(plot_metric_boxplot(data, metric))

    st.subheader("📋 Summary Statistics (Mean / Median / Std Dev)")
    st.dataframe(generate_summary_table(data))

    st.subheader("📈 Country Ranking by Average GHI")
    st.pyplot(plot_country_ranking(data, "GHI"))
else:
    st.warning("No countries selected or data not found.")
