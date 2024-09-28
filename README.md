# Bike Sharing Analysis

This repository contains the final project of the "Belajar Analisis Data dengan Python" course from Dicoding. This project focuses on data analysis and dashboard creation using a bike sharing dataset.

## Streamlit Link
https://dashboard-bike-rentals.streamlit.app/

## Project Work Stages
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Data Visualization
- Dashboard creation using Streamlit

## Project Installation
1. **Clone this repository**
     ```bash
     git clone https://github.com/lubnamawaddah/Bike-Sharing-Analysis.git
     ```

2. **Move to directory**
     ```bash
     cd Bike-Sharing-Analysis
     ```

3. **Install library**
     ```bash
     pip install -r requirements.txt
     ```

4. **Run streamlit app**
     ```bash
     streamlit run dashboard.py
     ```

## Directory Structure
```bash
bike-sharing-analysis/
│
├── dashboard/                 
│   ├── clean_day.csv          # Cleaned dataset for daily bike rentals
│   ├── clean_hour.csv         # Cleaned dataset for hourly bike rentals
│   ├── logo.png               # Logo image for the dashboard
│   └── app.py                 # Streamlit app for the dashboard
│
├── data/
│   ├── day.csv                # Original dataset for daily bike rentals
│   ├── hour.csv               # Original dataset for hourly bike rentals
│   └── Readme.txt             # Additional information about the datasets
│
├── notebook.ipynb             # Jupyter notebook for exploratory analysis.
├── requirements.txt           # File for package dependencies
├── url.txt                    # Contains the link to the deployed Streamlit app
└── README.md                  # Project README file
```