import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FEMA TSA Dashboard (Sample Dataset)")
st.write("Author:Charlotte Neme")

# Load your sample file (must be in the same folder)
df = pd.read_excel("FEMA Data Sample.xlsx")

st.header("1. Dataset Summary")
st.write("Number of rows:", df.shape[0])
st.write("Number of columns:", df.shape[1])


# -----------------------------
# HISTOGRAM OF REPAIR AMOUNT
# -----------------------------
st.header("2. Histogram of Repair Amount")
fig1 = px.histogram(df, x="repairAmount", nbins=40, title="Distribution of Repair Amounts")
st.plotly_chart(fig1)

st.write("Insight:")
st.write("Most households have low or zero repair amounts. A few have much higher values, which creates a long right tail.")


# -----------------------------
# BOXPLOT OF REPAIR AMOUNT BY TSA ELIGIBILITY
# -----------------------------
st.header("3. Repair Amount by TSA Eligibility")
fig2 = px.box(df, x="tsaEligible", y="repairAmount",
              labels={"tsaEligible": "TSA Eligible (0 = No, 1 = Yes)"},
              title="Repair Level Differences Between Eligible and Non-Eligible Households")
st.plotly_chart(fig2)

st.write("Insight:")
st.write("Households marked as eligible tend to have higher repair amounts compared to non-eligible households.")


# -----------------------------
# OPTIONAL: SHOW YOUR OTHER CHARTS
# -----------------------------
st.header("4. Additional Charts")

st.subheader("Repair Amount Histogram (from earlier analysis)")
st.image("chart_repair_histogram.png")




# -----------------------------
# END
# -----------------------------

st.header("5. Conclusion")
st.write(
    "This dashboard gives a simple view of repair needs and TSA eligibility using the smaller FEMA sample dataset. "
    "Most households show low repair amounts, while a small number have much higher values. "
    "The boxplot suggests that households marked as eligible often have higher repair needs. "
    "Together, these charts help show how repair levels relate to short-term housing support decisions."
)

st.write("This dashboard summarizes repair levels and TSA eligibility patterns using the FEMA sample dataset.")




