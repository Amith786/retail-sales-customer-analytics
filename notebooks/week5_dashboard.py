import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("online_retail_cleaned.csv")

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    return df


df = load_data()

# ============================================================
# TITLE
# ============================================================

st.title("📊 Retail Sales & Customer Analytics Dashboard")

st.markdown(
    "Interactive business analytics dashboard for the Online Retail dataset."
)

st.divider()

# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")

# Country filter
countries = sorted(df["Country"].dropna().unique())

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All Countries"] + countries
)

# Year filter
years = sorted(df["Year"].dropna().unique())

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All Years"] + years
)

# Apply filters
filtered_df = df.copy()

if selected_country != "All Countries":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

if selected_year != "All Years":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

# ============================================================
# KPI CALCULATIONS
# ============================================================

total_revenue = filtered_df["TotalSales"].sum()

total_transactions = len(filtered_df)

average_transaction = (
    filtered_df["TotalSales"].mean()
    if len(filtered_df) > 0
    else 0
)

total_quantity = filtered_df["Quantity"].sum()

total_products = filtered_df["StockCode"].nunique()

total_countries = filtered_df["Country"].nunique()

# ============================================================
# KPI SECTION
# ============================================================

st.subheader("📈 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Revenue",
        f"£{total_revenue:,.2f}"
    )

with col2:
    st.metric(
        "🧾 Total Transactions",
        f"{total_transactions:,}"
    )

with col3:
    st.metric(
        "💳 Average Transaction",
        f"£{average_transaction:,.2f}"
    )


col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "📦 Total Quantity",
        f"{total_quantity:,}"
    )

with col5:
    st.metric(
        "🛍️ Unique Products",
        f"{total_products:,}"
    )

with col6:
    st.metric(
        "🌍 Countries",
        f"{total_countries:,}"
    )

st.divider()

# ============================================================
# DATASET OVERVIEW
# ============================================================

st.subheader("📋 Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.write(
        f"**Records displayed:** {len(filtered_df):,}"
    )

with col2:
    st.write(
        f"**Active country filter:** {selected_country}"
    )

# ============================================================
# MONTHLY SALES TREND
# ============================================================

st.subheader("📈 Monthly Sales Revenue Trend")

monthly_sales = (
    filtered_df
    .groupby(["Year", "Month"], as_index=False)["TotalSales"]
    .sum()
)

monthly_sales["YearMonth"] = (
    monthly_sales["Year"].astype(str)
    + "-"
    + monthly_sales["Month"].astype(str).str.zfill(2)
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly_sales["YearMonth"],
    monthly_sales["TotalSales"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Revenue (£)")
ax.set_title("Monthly Sales Revenue Trend")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ============================================================
# TOP PRODUCTS
# ============================================================

st.subheader("🏆 Top 10 Products by Revenue")

top_products = (
    filtered_df
    .groupby("Description", as_index=False)["TotalSales"]
    .sum()
    .sort_values("TotalSales", ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    top_products["Description"].astype(str)[::-1],
    top_products["TotalSales"][::-1]
)

ax.set_xlabel("Total Revenue (£)")
ax.set_ylabel("Product")
ax.set_title("Top 10 Products by Total Revenue")

plt.tight_layout()

st.pyplot(fig)

# ============================================================
# COUNTRY PERFORMANCE
# ============================================================

st.subheader("🌍 Revenue by Country")

country_sales = (
    filtered_df
    .groupby("Country", as_index=False)["TotalSales"]
    .sum()
    .sort_values("TotalSales", ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    country_sales["Country"][::-1],
    country_sales["TotalSales"][::-1]
)

ax.set_xlabel("Total Revenue (£)")
ax.set_ylabel("Country")
ax.set_title("Top 10 Countries by Total Revenue")

plt.tight_layout()

st.pyplot(fig)


# ============================================================
# DAY OF WEEK ANALYSIS
# ============================================================

st.subheader("📅 Revenue by Day of Week")

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_sales = (
    filtered_df
    .groupby("DayOfWeek", as_index=False)["TotalSales"]
    .sum()
)

day_sales["DayOfWeek"] = pd.Categorical(
    day_sales["DayOfWeek"],
    categories=day_order,
    ordered=True
)

day_sales = day_sales.sort_values("DayOfWeek")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    day_sales["DayOfWeek"],
    day_sales["TotalSales"]
)

ax.set_xlabel("Day of Week")
ax.set_ylabel("Total Revenue (£)")
ax.set_title("Revenue by Day of Week")

plt.xticks(rotation=30)
plt.tight_layout()

st.pyplot(fig)


# ============================================================
# TRANSACTION VALUE DISTRIBUTION
# ============================================================

st.subheader("💷 Transaction Sales Distribution")

transaction_values = filtered_df["TotalSales"].dropna()

# Remove extreme values for clearer visualization
upper_limit = transaction_values.quantile(0.99)

typical_transactions = transaction_values[
    transaction_values <= upper_limit
]

fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(
    typical_transactions,
    bins=30
)

ax.set_xlabel("Transaction Sales (£)")
ax.set_ylabel("Frequency")
ax.set_title(
    "Distribution of Transaction Sales "
    "(Up to 99th Percentile)"
)

plt.tight_layout()

st.pyplot(fig)


# ============================================================
# TOP COUNTRY TABLE
# ============================================================

st.subheader("📋 Top 10 Countries – Revenue Details")

country_table = country_sales.copy()

country_table["TotalSales"] = country_table["TotalSales"].map(
    lambda x: f"£{x:,.2f}"
)

country_table = country_table.rename(
    columns={
        "Country": "Country",
        "TotalSales": "Revenue"
    }
)

st.dataframe(
    country_table,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Retail Sales & Customer Analytics | "
    "Junior Data Analyst – Business Analytics with Python | YuvaIntern"
)