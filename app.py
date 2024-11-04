import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit configuration
st.set_page_config(page_title="Diwali Sales Data Analysis", layout="wide")

# Title and Introduction
st.title("🪔 Diwali Sales Data Analysis 🪔")
st.markdown(
    """
    Welcome to the Diwali Sales Data Analysis App! 
    Upload your dataset to explore sales trends, customer insights, and more. 
    Use the sidebar to navigate through different analysis sections.
    """
)

# Sidebar for user navigation
st.sidebar.header("Navigation")
uploaded_file = st.sidebar.file_uploader("Upload your Diwali Sales CSV file", type="csv")

# Load and process data if file is uploaded
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='unicode_escape')
    st.sidebar.success("File uploaded successfully!")
    
    # Sidebar options for data exploration
    st.sidebar.subheader("Data Exploration Options")
    show_data_shape = st.sidebar.checkbox("Show Data Shape", True)
    show_data_head = st.sidebar.checkbox("Show First 5 Rows", True)
    show_data_info = st.sidebar.checkbox("Show Dataset Info", False)
    show_summary_stats = st.sidebar.checkbox("Show Summary Statistics", True)

    # Main section for data exploration
    st.subheader("📊 Data Exploration")

    if show_data_shape:
        st.write("### Dataset Shape")
        st.write(df.shape)

    if show_data_head:
        st.write("### First Five Rows of Data")
        st.write(df.head())

    if show_data_info:
        st.write("### Dataset Information")
        buffer = pd.io.common.StringIO()
        df.info(buf=buffer)
        info = buffer.getvalue()
        st.text(info)

    # Data Cleaning
    st.subheader("🧹 Data Cleaning")
    st.write("Dropping irrelevant columns and handling missing values.")
    columns_to_drop = ['Status', 'unnamed1']
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], axis=1, inplace=True)
    df.dropna(inplace=True)

    # Type Conversion
    if 'Amount' in df.columns:
        df['Amount'] = df['Amount'].astype(int)
        st.write("Converted `Amount` column to integer.")

    if show_summary_stats:
        st.write("### Summary Statistics")
        st.write(df.describe())

    # Sidebar for visualization options
    st.sidebar.subheader("Visualization Options")
    show_amount_dist = st.sidebar.checkbox("Show Amount Distribution", True)
    
    # Visualization section
    st.subheader("📈 Visualizations")
    if show_amount_dist:
        st.write("### Distribution of Sales Amount")
        fig, ax = plt.subplots()
        sns.histplot(df['Amount'], kde=True, ax=ax)
        st.pyplot(fig)
    
    # Additional placeholder for future visualizations
    st.write("### Additional Visualizations (Coming Soon)")
    st.info("Select visualization options from the sidebar.")
    
else:
    st.warning("Please upload a CSV file to begin analysis.")
