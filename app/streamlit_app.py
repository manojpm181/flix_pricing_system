import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Bus Pricing Dashboard", layout="wide")

st.title("🚍 Bus Pricing Intelligence Dashboard")

# ---------------- LOAD ----------------
@st.cache_data
def load_data():
    import os

    if not os.path.exists("outputs/flagged_cases.csv"):
        with st.spinner("⚙️ Running pricing pipeline... please wait (first time only)"):
            from main import run_pipeline
            run_pipeline()

    df_flagged = pd.read_csv("outputs/flagged_cases.csv")
    df_sample = pd.read_csv("outputs/sample_data.csv")
    df_summary = pd.read_csv("outputs/summary.csv")

    return df_flagged, df_sample, df_summary

# ---------------- SAFE SORT ----------------
order = ['LOW', 'OK', 'HIGH']
df_summary = df_summary[df_summary['Flag'].isin(order)]
df_summary = df_summary.set_index('Flag').reindex(order).reset_index()

# ---------------- KPI ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

high = df_summary[df_summary['Flag'] == "HIGH"]['Count'].sum()
low = df_summary[df_summary['Flag'] == "LOW"]['Count'].sum()
ok = df_summary[df_summary['Flag'] == "OK"]['Count'].sum()

total = high + low + ok if (high + low + ok) > 0 else 1

# ✅ PREMIUM KPI DESIGN
col1.markdown(f"""
### 🔴 High Price  
## {high:,} ({high/total:.1%})
""")

col2.markdown(f"""
### 🟡 Low Price  
## {low:,} ({low/total:.1%})
""")

col3.markdown(f"""
### 🟢 Optimal  
## {ok:,} ({ok/total:.1%})
""")

# ---------------- INSIGHTS ----------------
st.markdown("### 📊 Insights")

st.success(f"""
• **{high/total:.1%}** buses are overpriced  
• **{low/total:.1%}** buses are underpriced  
• **{ok/total:.1%}** are optimally priced  
""")

# ---------------- BAR CHART ----------------
st.subheader("📊 Pricing Summary")

fig = px.bar(
    df_summary,
    x="Flag",
    y="Count",
    color="Flag",
    color_discrete_map={
        "HIGH": "red",
        "LOW": "orange",
        "OK": "green"
    }
)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ---------------- FLAGGED TABLE ----------------
st.subheader("🚨 Flagged Cases")
st.dataframe(df_flagged.head(100))

# ---------------- TOP OVERPRICED ----------------
st.subheader("🔥 Top 10 Overpriced Routes")

top_high = df_flagged[df_flagged['flag'] == "HIGH"] \
    .sort_values(by='price', ascending=False) \
    .head(10)

st.dataframe(top_high)

# ---------------- TOP UNDERPRICED ----------------
st.subheader("💸 Top 10 Underpriced Routes")

top_low = df_flagged[df_flagged['flag'] == "LOW"] \
    .sort_values(by='price', ascending=True) \
    .head(10)

st.dataframe(top_low)

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filters")

cluster = st.sidebar.selectbox(
    "Select Cluster",
    sorted(df_flagged['cluster'].dropna().unique())
)

filtered = df_flagged[df_flagged['cluster'] == cluster]

# ---------------- CLUSTER DATA ----------------
st.subheader(f"🔍 Cluster {cluster} Data")
st.dataframe(filtered)

# ---------------- PIE CHART ----------------
st.subheader("📈 Cluster Flag Distribution")

fig2 = px.pie(
    filtered,
    names='flag',
    color='flag',
    color_discrete_map={
        "HIGH": "red",
        "LOW": "orange",
        "OK": "green"
    }
)

st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

# ---------------- SCATTER ----------------
if 'price' in df_flagged.columns and 'median_price' in df_flagged.columns:
    st.subheader("📉 Price vs Median Price")

    sample_df = df_flagged.sample(min(3000, len(df_flagged)), random_state=42)

    fig3 = px.scatter(
        sample_df,
        x="price",
        y="median_price",
        color="flag",
        color_discrete_map={
            "HIGH": "red",
            "LOW": "orange",
            "OK": "green"
        },
        opacity=0.6
    )

    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

# ---------------- EXTRA INSIGHT ----------------
avg_price = df_flagged['price'].mean()
st.caption(f"Average ticket price: ₹{avg_price:,.0f}")

# ---------------- DOWNLOAD ----------------
st.subheader("⬇️ Download Data")

st.download_button(
    label="Download Flagged Cases CSV",
    data=df_flagged.to_csv(index=False),
    file_name="flagged_cases.csv",
    mime="text/csv"
)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("  Manoj P M |🚀 Built with Streamlit | Bus Pricing Intelligence System")

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import os

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Bus Pricing Dashboard",
#     layout="wide",
#     page_icon="🚍"
# )

# st.title("🚍 Bus Pricing Intelligence Dashboard")

# # ---------------- FILE PATH ----------------
# file_path = "outputs/results.xlsx"

# # ---------------- LOAD DATA ----------------
# @st.cache_data
# def load_data():
#     if not os.path.exists(file_path):
#         st.error("❌ Excel file not found! Run main.py first.")
#         st.stop()

#     df_flagged = pd.read_excel(file_path, sheet_name="Flagged Cases")
#     df_sample = pd.read_excel(file_path, sheet_name="Sample Data")
#     df_summary = pd.read_excel(file_path, sheet_name="Summary")

#     return df_flagged, df_sample, df_summary


# df_flagged, df_sample, df_summary = load_data()

# # ---------------- KPI SECTION ----------------
# st.subheader("📌 Key Metrics")

# col1, col2, col3 = st.columns(3)

# high = df_summary[df_summary['Flag'].str.contains("HIGH", case=False)]['Count'].sum()
# low = df_summary[df_summary['Flag'].str.contains("LOW", case=False)]['Count'].sum()
# ok = df_summary[df_summary['Flag'].str.contains("OK", case=False)]['Count'].sum()

# total = high + low + ok

# # ✅ Metrics with %
# col1.metric("🔴 High Price", f"{high} ({high/total:.1%})")
# col2.metric("🟡 Low Price", f"{low} ({low/total:.1%})")
# col3.metric("🟢 Optimal", f"{ok} ({ok/total:.1%})")

# # ---------------- SUMMARY CHART ----------------
# st.subheader("📊 Pricing Summary")

# fig_summary = px.bar(
#     df_summary,
#     x="Flag",
#     y="Count",
#     color="Flag",
#     title="Overall Price Distribution"
# )

# st.plotly_chart(fig_summary, use_container_width=True)

# # ---------------- FLAGGED CASES ----------------
# st.subheader("🚨 Flagged Cases (Top 100)")
# st.dataframe(df_flagged.head(100))

# # ---------------- SIDEBAR FILTER ----------------
# st.sidebar.header("🔍 Filters")

# cluster = st.sidebar.selectbox(
#     "Select Cluster",
#     sorted(df_flagged['cluster'].unique())
# )

# filtered = df_flagged[df_flagged['cluster'] == cluster]

# # ---------------- CLUSTER ANALYSIS ----------------
# st.subheader(f"🔍 Cluster Analysis (Cluster {cluster})")
# st.dataframe(filtered)

# # ---------------- FLAG DISTRIBUTION ----------------
# st.subheader("📈 Flag Distribution (Selected Cluster)")

# fig_cluster = px.pie(
#     filtered,
#     names='flag',
#     title=f"Cluster {cluster} Distribution"
# )

# st.plotly_chart(fig_cluster, use_container_width=True)

# # ---------------- SCATTER PLOT ----------------
# if 'price' in df_flagged.columns and 'recommended_price' in df_flagged.columns:
#     st.subheader("📈 Price vs Recommended Price")

#     sample_df = df_flagged.sample(min(3000, len(df_flagged)), random_state=42)

#     fig_scatter = px.scatter(
#         sample_df,
#         x="price",
#         y="recommended_price",
#         color="flag",
#         opacity=0.7
#     )

#     st.plotly_chart(fig_scatter, use_container_width=True)

# # ---------------- DOWNLOAD ----------------
# st.subheader("⬇️ Download Data")

# st.download_button(
#     label="Download Flagged Cases",
#     data=df_flagged.to_csv(index=False),
#     file_name="flagged_cases.csv",
#     mime="text/csv"
# )

# # ---------------- FOOTER ----------------
# st.markdown("---")
# st.markdown("🚀 Built with Streamlit | Bus Pricing Intelligence System")
