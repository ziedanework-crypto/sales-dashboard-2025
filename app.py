import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================================
# قراءة البيانات
# ================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv("dailysales.csv", encoding="utf-8-sig")
    except:
        return pd.read_csv("dailysales.csv", encoding="latin1")

df = load_data()

# ================================
# العنوان الرئيسي
# ================================
st.set_page_config(page_title="لوحة متابعة المبيعات", layout="wide")
st.title("📊 لوحة متابعة المبيعات")
st.markdown("تقرير تفاعلي لعرض أداء المناديب وتحقيق الأهداف")

# ================================
# ملخص سريع
# ================================
col1, col2, col3, col4 = st.columns(4)
col1.metric("إجمالي المبيعات", f"{df['صافي المبيعات'].sum():,.0f}")
col2.metric("إجمالي عدد العملاء", df["اتصالات العملاء"].sum())
col3.metric("إجمالي تحقيق الهدف مبيعات", f"{df['تحقيق الهدف المبيعات'].mean():.2f}")
col4.metric("إجمالي تحقيق الهدف اتصالات", f"{df['تحقيق الهدف الاتصالات'].mean():.2f}")

# ================================
# جدول البيانات
# ================================
st.subheader("📋 بيانات تفصيلية")
st.dataframe(df, use_container_width=True)

# ================================
# رسم بياني: المبيعات حسب المندوب
# ================================
st.subheader("📈 المبيعات حسب المندوب")
fig, ax = plt.subplots(figsize=(10, 5))
df.groupby("اسم المندوب")["صافي المبيعات"].sum().plot(kind="bar", ax=ax, color="skyblue")
ax.set_ylabel("إجمالي المبيعات")
ax.set_xlabel("المندوب")
st.pyplot(fig)

# ================================
# رسم بياني: تحقيق الهدف
# ================================
st.subheader("🎯 نسبة تحقيق الأهداف (مبيعات)")
fig2, ax2 = plt.subplots(figsize=(10, 5))
df.plot(
    kind="bar",
    x="اسم المندوب",
    y="تحقيق الهدف المبيعات",
    ax=ax2,
    color="green",
    legend=False
)
ax2.set_ylabel("تحقيق الهدف")
st.pyplot(fig2)

# ================================
# فلترة بيانات
# ================================
st.subheader("🔎 فلترة")
names = st.multiselect("اختر المناديب", options=df["اسم المندوب"].unique(), default=df["اسم المندوب"].unique())
filtered_df = df[df["اسم المندوب"].isin(names)]
st.dataframe(filtered_df, use_container_width=True)
