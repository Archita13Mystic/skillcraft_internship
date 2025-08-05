import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load and clean data
df = pd.read_csv("US_Accidents_March23.csv")
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df = df.dropna(subset=['Start_Time'])

# === Generate Heatmap of Accident Locations ===
heat_df = df[['Start_Lat', 'Start_Lng']].dropna().sample(10000)

m = folium.Map(location=[37, -95], zoom_start=5, tiles='CartoDB positron')
HeatMap(data=heat_df.values, radius=8, blur=10, max_zoom=10).add_to(m)
m.save("accident_hotspots_map.html")
