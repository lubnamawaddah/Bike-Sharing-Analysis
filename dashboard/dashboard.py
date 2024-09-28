import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("dashboard/clean_day.csv")
hour_df = pd.read_csv("dashboard/clean_hour.csv")

day_df['date'] = pd.to_datetime(day_df['date'])

# Mengambil nilai min dan max dari kolom 'date'
min_date = day_df["date"].min()
max_date = day_df["date"].max()

with st.sidebar:
    # Menambahkan logo
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Date',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Menghitung total bike sharing, total casual users, dan total registered users
total_bike_sharing = day_df['casual'].sum() + day_df['registered'].sum()
total_casual_users = day_df['casual'].sum()
total_registered_users = day_df['registered'].sum()

# Menambahkan judul pada dashboard
st.title('Bike Rental Dashboard')

# Membuat 3 kolom
col1, col2, col3 = st.columns(3)

# Menampilkan total bike sharing
with col1:
    st.metric(label="Total Bike Rentals", value=f"{total_bike_sharing:,}")

# Menampilkan total casual users
with col2:
    st.metric(label="Total Casual Users", value=f"{total_casual_users:,}")

# Menampilkan total registered users
with col3:
    st.metric(label="Total Registered Users", value=f"{total_registered_users:,}")

st.markdown("---")

# Total rental per bulan
st.subheader("Monthly Rentals by Year")
selected_year = st.selectbox("Select Year", options=day_df['year'].unique())
filtered_data = day_df[day_df['year'] == selected_year]
plt.figure(figsize=(10, 5))
sns.lineplot(data=filtered_data, x='month', y='count', errorbar=None, marker='o')
plt.title(f'Number of Rentals by Month in {selected_year}', fontsize=16)
plt.xlabel(None)
plt.ylabel(None)
plt.xticks(filtered_data['month'])
plt.grid()
plt.tight_layout()
st.pyplot(plt)

st.markdown("---")

# Total rental berdasarkan musim
st.subheader("Total Rentals per Season")
seasonal_data = day_df.groupby('season')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x='count', y='season', data=seasonal_data.sort_values(by='count', ascending=False), palette=colors, ax=ax)
ax.set_title('Number of Rental by Season', loc='center', fontsize=28)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=17)
st.pyplot(fig)

st.markdown("---")

# Total rental berdasarkan kondisi cuaca
st.subheader("Rental Count by Weather Conditions")
weather_data = day_df.groupby('weather')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3"]
sns.barplot(y="count", x="weather", data=weather_data.sort_values(by="count", ascending=False), palette=colors, ax=ax)
ax.set_title("Number of Rental by Weather", loc="center", fontsize=28)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=17)
for i, count in enumerate(weather_data['count']):
    plt.text(weather_data['weather'].iloc[i], count, str(count), ha='center', va='bottom', fontsize=20)
st.pyplot(fig)

st.markdown("---")

# Total rental berdasarkan holiday
st.subheader("Rentals on Holidays")
holiday_data = day_df.groupby('holiday')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3"]
sns.barplot(y="count", x="holiday", data=holiday_data.sort_values(by="count", ascending=False), palette=colors, ax=ax)
ax.set_title("Number of Rental by Holiday", loc="center", fontsize=28)
ax.set_ylabel(None)
ax.set_xlabel("0: Not Holiday, 1: Holiday", fontsize=25)
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=17)
for i, count in enumerate(holiday_data['count']):
    plt.text(holiday_data['holiday'].iloc[i], count, str(count), ha='center', va='bottom', fontsize=20)
st.pyplot(fig)

st.markdown("---")

# Total rental berdasarkan workingday
st.subheader("Rentals on Working Days")
workingday_data = day_df.groupby('workingday')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#D3D3D3", "#90CAF9"]
sns.barplot(y="count", x="workingday", data=workingday_data.sort_values(by="count", ascending=False), palette=colors, ax=ax)
ax.set_title("Number of Rental by Working Day", loc="center", fontsize=28)
ax.set_ylabel(None)
ax.set_xlabel("0: Not Working Day, 1: Working Day", fontsize=25)
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=17)
for i, count in enumerate(workingday_data['count']):
    plt.text(workingday_data['workingday'].iloc[i], count, str(count), ha='center', va='bottom', fontsize=20)
st.pyplot(fig)

st.markdown("---")

# Total rental berdasarkan hari dalam seminggu
st.subheader("Rentals by Day of the Week")
weekday_data = day_df.groupby('weekday')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#87CEEB", "#ADD8E6", "#E0BBE4", "#FFCCCB", "#FF69B4", "#DDA0DD", "#FFDEAD"]
sns.barplot(y="count", x="weekday", data=weekday_data, palette=colors, ax=ax)
ax.set_title("Number of Rental by Week Day", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=25)
ax.tick_params(axis='y', labelsize=17)
for i, count in enumerate(weekday_data['count']):
    plt.text(weekday_data['weekday'].iloc[i], count, str(count), ha='center', va='bottom', fontsize=20)
st.pyplot(fig)

st.markdown("---")

# Total rental pengguna casual dan registered berdasarkan jenis hari
st.subheader("Bike User Distribution Based on Day Type")
combined_data = day_df.groupby(['day_type']).agg({'casual': 'sum', 'registered': 'sum'}).reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = range(len(combined_data))
# Bar untuk pengguna casual
bars1 = ax.bar([p - bar_width/2 for p in x], combined_data['casual'], width=bar_width, label='Casual', color='lightblue')
# Bar untuk pengguna terdaftar
bars2 = ax.bar([p + bar_width/2 for p in x], combined_data['registered'], width=bar_width, label='Registered', color='salmon')
ax.set_title('Number of Rental by Day Type', fontsize=14)
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.set_xticks(x)
ax.set_xticklabels(combined_data['day_type'])
ax.legend(title='User')
for bar in bars1 + bars2:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), 
            ha='center', va='bottom', fontsize=12)
st.pyplot(fig)

st.markdown("---")

# Total rental berdasarkan jam
st.subheader("Hourly Rental Trends")
plt.figure(figsize=(10, 5))
sns.lineplot(data=hour_df, x='hour', y='count', errorbar=None, marker='o')
plt.title('Number of Rental by Hour', fontsize=16)
plt.xlabel('Hour', fontsize=12)
plt.ylabel(None)
plt.xticks(range(0, 24))
plt.grid()
plt.tight_layout()
st.pyplot(plt)

st.markdown("---")

st.caption('Copyright © 2024 Lubna Mawaddah')