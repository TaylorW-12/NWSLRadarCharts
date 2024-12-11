import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import openpyxl



#df=pd.read_html('https://fbref.com/en/players/aa0f9aa7/scout/12460/Croix-Bethune-Scouting-Report',attrs={"id":"scout_full_AM"})[0]
#df.columns=['_'.join(col).strip() for col in df.columns.values]
# Save the DataFrame to a CSV file
#df.to_csv('croix_bethune_data.csv', index=False)
# Load the saved data when needed
#Croix Bethune
df = pd.read_excel('croix_bethune_data.xlsx',engine='openpyxl')
df = df.drop('Standard Stats_Percentile', axis=1)
df_transposed = df.transpose() # Set the first row as column titles 
df_transposed.columns = df_transposed.iloc[0] 
df_transposed =df_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df=df_transposed[selected_columns]
player_name = "Croix Bethune"
new_df["Player"] = player_name
print(new_df.head())

#Temwa Chawinga
df_1=pd.read_excel('temwa_chawinga_data.xlsx',engine='openpyxl')
df_1 = df_1.drop('Standard Stats_Percentile', axis=1)
df_1_transposed = df_1.transpose() # Set the first row as column titles 
df_1_transposed.columns = df_1_transposed.iloc[0] 
df_1_transposed =df_1_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_1=df_1_transposed[selected_columns]
player_name = "Temwa Chawinga"
new_df_1["Player"] = player_name
print(new_df_1.head())

#Sophia Smith 
df_3=pd.read_excel('sophie_smith_data.xlsx',engine='openpyxl')
df_3 = df_3.drop('Standard Stats_Percentile', axis=1)
df_3_transposed = df_3.transpose() # Set the first row as column titles 
df_3_transposed.columns = df_3_transposed.iloc[0] 
df_3_transposed =df_3_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_3=df_3_transposed[selected_columns]
player_name = "Sophia Smith"
new_df_3["Player"] = player_name
print(new_df_3.head())

#Barbra Banda
df_2=pd.read_excel('barbra_banda_data.xlsx',engine='openpyxl')
df_2 = df_2.drop('Standard Stats_Percentile', axis=1)
df_2_transposed = df_2.transpose() # Set the first row as column titles 
df_2_transposed.columns = df_2_transposed.iloc[0] 
df_2_transposed =df_2_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_2=df_2_transposed[selected_columns]
player_name = "Barbra Banda"
new_df_2["Player"] = player_name
print(new_df_2.head())

#Ouleymata Sarr
df_4=pd.read_excel('ouleymata_sarr_data.xlsx',engine='openpyxl')
df_4 = df_4.drop('Standard Stats_Percentile', axis=1)
df_4_transposed = df_4.transpose() # Set the first row as column titles 
df_4_transposed.columns = df_4_transposed.iloc[0] 
df_4_transposed =df_4_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_4=df_4_transposed[selected_columns]
player_name = "Ouleymata Sarr"
new_df_4["Player"] = player_name
print(new_df_4.head())

#Sydney Leroux
df_5=pd.read_excel('sydney_leroux_data.xlsx',engine='openpyxl')
df_5=df_5.drop('Standard Stats_Percentile', axis=1)
df_5_transposed= df_5.transpose() # Set the first row as column titles 
df_5_transposed.columns = df_5_transposed.iloc[0] 
df_5_transposed=df_5_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_5=df_5_transposed[selected_columns]
player_name = "Sydney Leroux"
new_df_5["Player"] = player_name
print(new_df_5.head())

#Ashley Hatch 
df_6=pd.read_excel('ashley_hatch_data.xlsx',engine='openpyxl')
df_6=df_6.drop('Standard Stats_Percentile', axis=1)
df_6_transposed= df_6.transpose() # Set the first row as column titles 
df_6_transposed.columns = df_6_transposed.iloc[0] 
df_6_transposed=df_6_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_6=df_6_transposed[selected_columns]
player_name = "Ashley Hatch"
new_df_6["Player"] = player_name
print(new_df_6.head())

#Lynn Williams
df_7=pd.read_excel('lynn_williams_data.xlsx',engine='openpyxl')
df_7=df_7.drop('Standard Stats_Percentile', axis=1)
df_7_transposed= df_7.transpose() # Set the first row as column titles 
df_7_transposed.columns = df_7_transposed.iloc[0] 
df_7_transposed=df_7_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_7=df_7_transposed[selected_columns]
player_name = "Lynn Williams"
new_df_7["Player"] = player_name
print(new_df_7.head())


#Trinity Rodman 
df_8=pd.read_excel('trinity_rodman_data.xlsx',engine='openpyxl')
df_8=df_8.drop('Standard Stats_Percentile', axis=1)
df_8_transposed= df_8.transpose() # Set the first row as column titles 
df_8_transposed.columns = df_8_transposed.iloc[0] 
df_8_transposed=df_8_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_8=df_8_transposed[selected_columns]
player_name = "Trinity Rodman"
new_df_8["Player"] = player_name
print(new_df_8.head())

#Mallory Swanson
df_9=pd.read_excel('mallory_sawanson_data.xlsx',engine='openpyxl')
df_9=df_9.drop('Standard Stats_Percentile', axis=1)
df_9_transposed= df_9.transpose() # Set the first row as column titles 
df_9_transposed.columns = df_9_transposed.iloc[0] 
df_9_transposed=df_9_transposed[1:]
selected_columns=['Goals','Assists','Successful Take-Ons','Ball Recoveries','Tackles Won','Goal-Creating Actions','Passes Completed','xG: Expected Goals','xAG: Exp. Assisted Goals']
new_df_9=df_9_transposed[selected_columns]
player_name = "Mallory Swanson"
new_df_9["Player"] = player_name
print(new_df_9.head())

df_concat = pd.concat([new_df, new_df_1, new_df_2, new_df_3, new_df_4,new_df_5,new_df_6,new_df_7,new_df_8,new_df_9], axis=0)
df_concat.reset_index(drop=True, inplace=True)


numeric_columns = ['Goals', 'Assists', 'Successful Take-Ons', 'Ball Recoveries',
                   'Tackles Won', 'Goal-Creating Actions', 'Passes Completed',
                   'xG: Expected Goals', 'xAG: Exp. Assisted Goals']
df_concat[numeric_columns] = df_concat[numeric_columns].apply(pd.to_numeric, errors='coerce') * 100

# Streamlit interface
st.title("Radar Chart: NWSL Player Comparison")
st.subheader("Developed by: Taylor Washington")
# Layout: Two columns
filters_col, chart_col = st.columns([1, 3])

# Filters on the left
with st.sidebar:
    st.header("Filters")
    player_1 = st.selectbox("Select Player 1", options=df_concat["Player"].unique())
    player_2 = st.selectbox("Select Player 2", options=df_concat["Player"].unique())
    st.write("Data Source: Fbref.com")

# Radar chart function
def create_radar_chart(player1, player2, df):
    fig = go.Figure()
    categories = numeric_columns  # Radar chart axes
    
    # Player 1 data
    player1_data = df[df["Player"] == player1].iloc[0][categories].tolist()
    player1_data += player1_data[:1]  # Close the loop
    fig.add_trace(go.Scatterpolar(
        r=player1_data,
        theta=categories + [categories[0]],
        fill='toself',
        name=player1
    ))
    
    # Player 2 data
    player2_data = df[df["Player"] == player2].iloc[0][categories].tolist()
    player2_data += player2_data[:1]  # Close the loop
    fig.add_trace(go.Scatterpolar(
        r=player2_data,
        theta=categories + [categories[0]],
        fill='toself',
        name=player2
    ))
    
    # Chart layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])  # Adjust range if needed
        ),
        showlegend=True,
        title="Forward Stats Comparison"
    )
    return fig

# Display radar chart on the right
with chart_col:
    if player_1 and player_2:
        radar_chart = create_radar_chart(player_1, player_2, df_concat)
        st.plotly_chart(radar_chart)
    else:
        st.write("Please select two players to display the radar chart.")

#Top Defenders
#Kerry Abello 
#Casey Krueger
#Page Nielsen 
#Ryan Williams 
#Nealy Martin 
#Alyssa Malonson 
#Kylie Strom 
#Caprice Dydasco
#Madison Curry 
#phobe Mcclernon 
#Reyna Reyes

#Top Midfielder
#Croix Bethune
#Yazmeen Ryan 
#Vanessa Dibernardo
#Debinha
#Jenna Nighswonger
#Sam Coffey 
#Rose Lavelle
#Barbara Davila
#Hailie Mace
#Lauren Milliet 

#Keepers
#Anna Moorhouse
#Shelby Hogan 
#Jane Campbell 
#Ann-Katrin Berger
#Aubrey Kingsbury 
#Kailen Sheridan 
#Almuth Schult
#Alyssa Naeher

#Per 90 stats
#Poessession percentages 
#Pass Accuracy 
#Shots on Target
#Defenders: Successful Tackles, Interceptions, Clearnaces
#Forwards: Goal scoring and playing abilities, assists

