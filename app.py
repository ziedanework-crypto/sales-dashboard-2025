import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================================
# قراءة البيانات مع معالجة الترميز
# ================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv("dailysales.csv", encoding="utf-8-sig")
    except:
        try:
            return pd.read_csv("dailysales.csv", encoding="windows-1256")
        except:
            return pd.read_csv("dailysales.csv", encoding="latin1", errors="ignore")

df = load_data()

# ================================
# باقي الكود
# ================================
st.set_page_config(page_title="لوحة متابعة المبيعات", layout="wide")
st.title("📊 لوحة متابعة المبيعات")

st.subheader("📋 البيانات")
st.dataframe(df)

fig, ax = plt.subplots()
df.groupby("اسم المندوب")["صافي المبيعات"].sum().plot(kind="bar", ax=ax, color="skyblue")
st.pyplot(fig)
