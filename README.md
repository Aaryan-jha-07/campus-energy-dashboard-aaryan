#Campus Energy Consumption Analysis Tool
#Overview

This project is a Python-based application designed to manage, analyze, and visualize energy consumption data across multiple university buildings (e.g., Building A, Science Block). It utilizes Object-Oriented Programming (OOP) principles to ingest raw meter readings, calculate usage statistics, and generate actionable insights via reports and visual dashboards.

#Features

Synthetic Data Generation: Includes a script to generate realistic dummy data for testing purposes.

Data Ingestion & Cleaning: Automatically loads CSV files from a specific directory, validates columns, and merges them into a master dataset.

Statistical Analysis: Calculates key metrics per building (Mean, Min, Max, Total Consumption).

Visualization: Generates a visual dashboard (dashboard.png) showing consumption trends.

Reporting: Exports a summary text file (summary.txt) and processed CSV datasets.

#Prerequisites

You need Python 3.x installed along with the following libraries:

pandas

matplotlib

numpy

You can install the dependencies using pip:

#Bash
pip install pandas matplotlib numpy
Project Structure

#Plaintext
├── main.py                  # Core logic: Ingestion, Analysis, Visualization
├── dummy.py                 # Utility: Generates sample CSV data in /data folder
├── summary.txt              # Output: Executive summary report
├── dashboard.png            # Output: Visual graph of energy trends
├── building_summary.csv     # Output: Aggregated stats per building
├── cleaned_energy_data.csv  # Output: Merged and processed dataset
└── data/                    # Directory containing raw input CSVs
Usage Instructions

1. Generate Data

If you do not have raw meter data, run dummy.py first. This will create a data/ folder and populate it with sample CSV files for "Building_A", "Building_B", and "Science_Block".

Bash
python dummy.py
2. Run Analysis

Run the main script to process the data, generate the dashboard, and create reports.

Bash
python main.py
Outputs Explained

After running main.py, the following files are generated:

dashboard.png: A chart visualizing the energy consumption over time and by building.

summary.txt: A quick text report containing:

Total Campus Consumption (kWh)

Highest Consuming Building

Peak Load Time (Hour)

building_summary.csv: A spreadsheet detailing the Mean, Min, Max, and Sum of energy usage for every building.

cleaned_energy_data.csv: A unified file containing all validated readings from all buildings with timestamps standardized.

#Code Highlights

BuildingManager Class: Orchestrates the loading of data from multiple files.

Building & MeterReading Classes: Represents the physical infrastructure and data points, keeping the code modular.

Matplotlib Integration: Automatically formats and saves the dashboard image without requiring a GUI.
