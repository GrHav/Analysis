!pip install seaborn
!pip install pandas
!pip install matplotlib

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

with st.sidebar:
    st.text("Pemula")
    st.image("https://media.istockphoto.com/id/1256527934/vector/air-quality-index-educational-scheme-with-excessive-quantities-of-substances-or-gases-in.jpg?s=612x612&w=0&k=20&c=vx4E-KMNVGwXLz7CQaziOSotMHDMa0_6CRnDazYdHEM=")

with st.container():
    st.subheader("Pollutant Demographics")

    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(30, 12))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x=all_df['PM2.5'], y=all_df['station'], data=all_df.sort_values(by='PM2.5', ascending=True).head(5), palette=colors, ax=ax[0,0]) 
    ax[0,0].set_ylabel(None)
    ax[0,0].set_xlabel(None)
    ax[0,0].invert_xaxis()
    ax[0,0].yaxis.set_label_position("right")
    ax[0,0].yaxis.tick_right()
    ax[0,0].set_title("Worst PM2.5 Station", loc="center", fontsize=15)
    ax[0,0].tick_params(axis='y', labelsize=12)

    sns.barplot(x=all_df['PM10'], y=all_df['station'], data=all_df.sort_values(by='PM10', ascending=True).head(5), palette=colors, ax=ax[0,1]) 
    ax[0,1].set_ylabel(None)
    ax[0,1].set_xlabel(None)
    ax[0,1].invert_xaxis()
    ax[0,1].yaxis.set_label_position("right")
    ax[0,1].yaxis.tick_right()
    ax[0,1].set_title("Worst PM10 Station", loc="center", fontsize=15)
    ax[0,1].tick_params(axis='y', labelsize=12)

    sns.barplot(x=all_df['SO2'], y=all_df['station'], data=all_df.sort_values(by='SO2', ascending=True).head(5), palette=colors, ax=ax[1,0]) 
    ax[1,0].set_ylabel(None)
    ax[1,0].set_xlabel(None)
    ax[1,0].invert_xaxis()
    ax[1,0].yaxis.set_label_position("right")
    ax[1,0].yaxis.tick_right()
    ax[1,0].set_title("Worst SO2 Station", loc="center", fontsize=15)
    ax[1,0].tick_params(axis='y', labelsize=12)

    sns.barplot(x=all_df['NO2'], y=all_df['station'], data=all_df.sort_values(by='NO2', ascending=True).head(5), palette=colors, ax=ax[1,1]) 
    ax[1,1].set_ylabel(None)
    ax[1,1].set_xlabel(None)
    ax[1,1].invert_xaxis()
    ax[1,1].yaxis.set_label_position("right")
    ax[1,1].yaxis.tick_right()
    ax[1,1].set_title("Worst NO2 Station", loc="center", fontsize=15)
    ax[1,1].tick_params(axis='y', labelsize=12)

    sns.barplot(x=all_df['CO'], y=all_df['station'], data=all_df.sort_values(by='CO', ascending=True).head(5), palette=colors, ax=ax[2,0]) 
    ax[2,0].set_ylabel(None)
    ax[2,0].set_xlabel(None)
    ax[2,0].invert_xaxis()
    ax[2,0].yaxis.set_label_position("right")
    ax[2,0].yaxis.tick_right()
    ax[2,0].set_title("Worst CO Station", loc="center", fontsize=15)
    ax[2,0].tick_params(axis='y', labelsize=12)

    sns.barplot(x=all_df['O3'], y=all_df['station'], data=all_df.sort_values(by='O3', ascending=False).head(5), palette=colors, ax=ax[2,1]) 
    ax[2,1].set_ylabel(None)
    ax[2,1].set_xlabel(None)
    ax[2,1].yaxis.set_label_position("right")
    ax[2,1].yaxis.tick_right()
    ax[2,1].set_title("Best O3 Station", loc="center", fontsize=15)
    ax[2,1].tick_params(axis='y', labelsize=12)

    st.subheader("Best & Worst Index Pollutants Station")
    st.pyplot(fig)
with st.expander("See explanation"):
    st.write("Semakin tinggi index pada PM2.5, PM10, CO, SO2, NO2 dan O3 maka semakin berbahayanya tempat tersebut. Polutan atau polusi tersebut dapat merusak dan mengganggu pernapasan.")

with st.container():
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(30, 12))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x=all_df['PM2.5'], y=all_df['station'], data=all_df.sort_values(by='PM2.5', ascending=True).head(5), palette=colors, ax=ax[0]) 
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Highest PM2.5 Station", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.barplot(x=all_df['PM10'], y=all_df['station'], data=all_df.sort_values(by='PM10', ascending=True).head(5), palette=colors, ax=ax[1])
    ax[1].set_title("Best PM2.5 Station", loc="center", fontsize=15)
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("Highest PM10 Station", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)
    st.subheader("Station With The Highest PM index")
    st.pyplot(fig)
with st.expander("See explanation"):
    st.write("Semakin tinggi index yang muncul di grafik tersebut, semakin berbahayanya tempat tersebut untuk manusia karena PM (Partikel Matter) dapat merusak paru-paru. Diharapkan untuk pengunjung dalam menggunakan masker agar mengantisipasi kemasukkannya PM2.5 atau PM10 ke paru-paru.")

st.caption('Copyright (c) Dicoding 2025')
