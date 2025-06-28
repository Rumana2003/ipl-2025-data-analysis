import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===================================================
# 1️⃣ LOAD THE DATA
# ===================================================
data_file = r'D:\data analytic projects\project 5\deliveries.csv'  # Use raw strings for Windows paths
df = pd.read_csv(data_file)

# Inspect available columns
print("\nAvailable Columns:", df.columns)

# ===================================================
# 2️⃣ CREATE TOTAL_RUNS COLUMN
# ===================================================
# According to your dataset, total runs = runs_of_bat + extras
df['total_runs'] = df['runs_of_bat'] + df['extras']

# ===================================================
# 3️⃣ TOTAL RUNS PER TEAM
# ===================================================
team_runs = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
team_runs.plot(kind='bar', color='green')
plt.title('Total Runs by Team (All Matches)')
plt.xlabel('Team')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.show()

# ===================================================
# 4️⃣ TOTAL WICKETS PER BOWLING TEAM
# ===================================================
wickets = df[df['player_dismissed'].notna()].groupby('bowling_team')['player_dismissed'].count().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
wickets.plot(kind='bar', color='red')
plt.title('Total Wickets Taken by Bowling Team')
plt.xlabel('Team')
plt.ylabel('Number of Wickets')
plt.xticks(rotation=45)
plt.show()

# ===================================================
# 5️⃣ TOP 10 BATSMEN BY TOTAL RUNS
# ===================================================
top_batsmen = df.groupby('striker')['runs_of_bat'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_batsmen.plot(kind='bar', color='blue')
plt.title('Top 10 Batsmen by Total Runs')
plt.xlabel('Batsman')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.show()

# ===================================================
# 6️⃣ TOP 10 BOWLERS BY TOTAL WICKETS
# ===================================================
top_bowlers = df[df['player_dismissed'].notna()].groupby('bowler')['player_dismissed'].count().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_bowlers.plot(kind='bar', color='orange')
plt.title('Top 10 Bowlers by Wickets')
plt.xlabel('Bowler')
plt.ylabel('Number of Wickets')
plt.xticks(rotation=45)
plt.show()

# ===================================================
# 7️⃣ CORRELATION HEATMAP
# ===================================================
numeric_data = df.select_dtypes(include='number')
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Numerical Features')
plt.show()
