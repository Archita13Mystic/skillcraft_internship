import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "task_1.xlsx"
data = pd.read_excel(file_path, sheet_name="Data", skiprows=3)

# Convert all column names to string (for consistent access)
data.columns = data.columns.map(str)

# Filter for India's total population data
india_data = data[(data['Country Name'] == 'India') & (data['Indicator Name'] == 'Population, total')]

# Extract total population for the years 2020, 2021, and 2022
years = ['2020', '2021', '2022']
india_pop = india_data[years].values.flatten()

# Simulated age group proportions (adjust if real data is available)
age_distribution = {
    '0–20 years': 0.35,
    '21–64 years': 0.55,
    '65+ years': 0.10
}

# Calculate population in each age group for each year
pop_by_group = {
    year: {
        group: int(total_pop * proportion)
        for group, proportion in age_distribution.items()
    }
    for year, total_pop in zip(years, india_pop)
}


# Bar Chart

plt.figure(figsize=(8, 5))
groups_2022 = pop_by_group['2022']
plt.bar(groups_2022.keys(), groups_2022.values(), color=['skyblue', 'lightgreen', 'salmon'])
plt.title("India's Population in 2022 by Age Group")
plt.ylabel('Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#Pie Chart

plt.figure(figsize=(6, 6))
plt.pie(groups_2022.values(), labels=groups_2022.keys(), autopct='%1.1f%%', startangle=140,
        colors=['skyblue', 'lightgreen', 'salmon'])
plt.title("Age Group Distribution in India (2022)")
plt.tight_layout()
plt.show()

