import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load and clean data
df = pd.read_csv("US_Accidents_March23.csv")
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df = df.dropna(subset=['Start_Time'])

df['Hour'] = df['Start_Time'].dt.hour
sns.set(style='whitegrid')

#Accidents by Hour
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, hue='Hour', palette='rocket', legend=False)
plt.title('Accident Distribution by Hour of Day', fontsize=16, fontweight='bold')
plt.xlabel('Hour of Day (0–23)', fontsize=12)
plt.ylabel('Number of Accidents', fontsize=12)
plt.tight_layout()
plt.show()

#Top 10 Weather Conditions
top_weather = df['Weather_Condition'].value_counts().head(10).index
weather_df = df[df['Weather_Condition'].isin(top_weather)]

plt.figure(figsize=(12, 6))
sns.countplot(y='Weather_Condition', data=weather_df, order=top_weather, palette='mako', hue='Weather_Condition', legend=False)
plt.title('Top 10 Weather Conditions in Accidents', fontsize=16, fontweight='bold')
plt.xlabel('Accident Count', fontsize=12)
plt.ylabel('Weather Condition', fontsize=12)
plt.tight_layout()
plt.show()

#Grouped Road Feature Charts
df['Hour'] = df['Start_Time'].dt.hour
sns.set(style='whitegrid')

#Select and prepare binary road features
road_features = ['Bump', 'Junction', 'Traffic_Signal', 'Stop', 'Crossing']
df_bin = df[road_features].fillna(False).astype(bool)

counts_df = df_bin.apply(pd.Series.value_counts).T
counts_df.columns = ['Absent', 'Present']
counts_df = counts_df.reset_index().rename(columns={'index': 'Feature'})

grouped_df = counts_df.melt(id_vars='Feature', var_name='Presence', value_name='Count')

plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_df, x='Feature', y='Count', hue='Presence', palette='Set2')
plt.title('Accident Counts by Road Feature Presence', fontsize=16, fontweight='bold')
plt.xlabel('Road Feature')
plt.ylabel('Number of Accidents')
plt.legend(title='Presence')
plt.tight_layout()
plt.show()


#Heatmap of Accident Hotspots
heat_df = df[['Start_Lat', 'Start_Lng']].dropna().sample(10000)

m = folium.Map(location=[37, -95], zoom_start=5, tiles='CartoDB positron')
HeatMap(data=heat_df.values, radius=8, blur=10, max_zoom=10).add_to(m)
m.save("accident_hotspots_map.html")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load and clean data
df = pd.read_csv("US_Accidents_March23.csv")
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df = df.dropna(subset=['Start_Time'])

#Generate Heatmap of Accident Locations
heat_df = df[['Start_Lat', 'Start_Lng']].dropna().sample(10000)

m = folium.Map(location=[37, -95], zoom_start=5, tiles='CartoDB positron')
HeatMap(data=heat_df.values, radius=8, blur=10, max_zoom=10).add_to(m)
m.save("accident_hotspots_map.html")



print("Analysis complete. Heatmap saved as 'accident_hotspots_map.html'")
