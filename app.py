import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================================
# قراءة البيانات مع معالجة الترميز
# ================================
@st.cache_data
def load_data():
    encodings = ["utf-8-sig", "windows-1256", "latin1"]
    for enc in encodings:
        try:
            with open("dailysales.csv", "r", encoding=enc, errors="ignore") as f:
                return pd.read_csv(f)
        except Exception as e:
            print(f"فشل مع الترميز: {enc} - {e}")
    return pd.DataFrame()  # في حالة فشل كل المحاولات

df = load_data()

# ================================
# باقي الكود
# ================================
st.set_page_config(page_title="لوحة متابعة المبيعات", layout="wide")
st.title("📊 لوحة متابعة المبيعات")

if df.empty:
    st.error("❌ تعذر قراءة ملف dailysales.csv، جرّب رفع نسخة بالترميز UTF-8.")
else:
    st.subheader("📋 البيانات")
    st.dataframe(df)

    fig, ax = plt.subplots()
    if "اسم المندوب" in df.columns and "صافي المبيعات" in df.columns:
        df.groupby("اسم المندوب")["صافي المبيعات"].sum().plot(kind="bar", ax=ax, color="skyblue")
        st.pyplot(fig)
    else:
        st.warning("⚠️ تأكد أن الأعمدة (اسم المندوب، صافي المبيعات) موجودة بالملف.")
