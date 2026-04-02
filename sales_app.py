import streamlit as st
import pandas as pd

# Title and description
st.title("Sales Summary Dashboard")
st.subheader("Simple interactive sales report by category")

data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Tablet", "Jacket"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [1200, 300, 800, 450, 600, 700]
}

df = pd.DataFrame(data)

# Sidebar for filters
st.sidebar.title("Filters")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data based on selection
filtered_df = df[df["Category"] == category]

# Main content
st.write(f"Showing data for category: {category}")

st.dataframe(filtered_df)

# Line chart
st.line_chart(filtered_df.set_index("Product")["Sales"])