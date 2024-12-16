# clustering_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.title("Clustering Application")

# Upload file
uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset Preview", data.head())
    
    # Data preprocessing
    data_cleaned = data.drop(['Country'], axis=1)
    data_cleaned.fillna(data_cleaned.mean(), inplace=True)
    
    # Standardization
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_cleaned)
    
    # K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(data_scaled)
    data['Cluster'] = labels
    st.write("Clustered Data", data)
    
    # Visualization
    st.bar_chart(data['Cluster'].value_counts())
