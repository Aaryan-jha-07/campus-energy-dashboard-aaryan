import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path



class MeterReading:
    """Represents a single energy reading."""
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    """Represents a building and holds its readings."""
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

class BuildingManager:
    """Manages multiple buildings and handles data ingestion."""
    def __init__(self):
        self.buildings = []
        self.master_df = pd.DataFrame()

    def load_data(self, directory_path):
        """Task 1: Ingestion and Validation"""
        path = Path(directory_path)
        all_data = []

        for file_path in path.glob('*.csv'):
            try:
       
                building_name = file_path.stem 
                
               
                df = pd.read_csv(file_path)
                
                if 'timestamp' not in df.columns or 'kwh' not in df.columns:
                    print(f"Skipping {file_path}: Missing columns.")
                    continue

                df['Building'] = building_name
               
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                
                all_data.append(df)
                
                new_building = Building(building_name)
                for _, row in df.iterrows():
                    reading = MeterReading(row['timestamp'], row['kwh'])
                    new_building.add_reading(reading)
                self.buildings.append(new_building)
                
                print(f"Successfully loaded: {file_path.name}")

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

   
        if all_data:
            self.master_df = pd.concat(all_data, ignore_index=True)
            return self.master_df
        else:
            return pd.DataFrame()


def calculate_daily_totals(df):
    """Resamples data to calculate total daily consumption."""

    temp_df = df.set_index('timestamp')
   
    daily_stats = temp_df.groupby('Building').resample('D')['kwh'].sum().reset_index()
    return daily_stats

def building_wise_summary(df):
    """Calculates mean, min, max, and total per building."""
    summary = df.groupby('Building')['kwh'].agg(['mean', 'min', 'max', 'sum'])
    return summary



def generate_dashboard(df):
    """Creates a dashboard with 3 plots."""
    if df.empty:
        print("No data to visualize.")
        return

   
    fig, axs = plt.subplots(3, 1, figsize=(10, 18))
    fig.suptitle('Campus Energy-Use Dashboard', fontsize=16)

    daily_df = calculate_daily_totals(df)
    for building in daily_df['Building'].unique():
        subset = daily_df[daily_df['Building'] == building]
        axs[0].plot(subset['timestamp'], subset['kwh'], label=building)
    axs[0].set_title('Daily Consumption Trends')
    axs[0].set_ylabel('Total kWh')
    axs[0].legend()

    
    summary = building_wise_summary(df)
    axs[1].bar(summary.index, summary['sum'], color=['#4CAF50', '#2196F3', '#FF9800'])
    axs[1].set_title('Total Energy Consumption per Building')
    axs[1].set_ylabel('Total kWh')

    df['hour'] = df['timestamp'].dt.hour
    for building in df['Building'].unique():
        subset = df[df['Building'] == building]
        axs[2].scatter(subset['hour'], subset['kwh'], alpha=0.5, label=building)
    axs[2].set_title('Peak Hour Consumption Analysis')
    axs[2].set_xlabel('Hour of Day (0-23)')
    axs[2].set_ylabel('kWh')
    axs[2].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('dashboard.png')
    print("Dashboard saved as 'dashboard.png'.")



def generate_reports(df):
    """Exports CSVs and creates a text summary."""
    if df.empty:
        return

    df.to_csv('cleaned_energy_data.csv', index=False)
    
   
    summary_df = building_wise_summary(df)
    summary_df.to_csv('building_summary.csv')

    total_consumption = df['kwh'].sum()
    highest_building = summary_df['sum'].idxmax()
    peak_hour = df.groupby('hour')['kwh'].sum().idxmax()

    report_content = (
        f"--- Executive Summary ---\n"
        f"Total Campus Consumption: {total_consumption:.2f} kWh\n"
        f"Highest Consuming Building: {highest_building}\n"
        f"Peak Load Time (Hour): {peak_hour}:00\n"
        f"Data processed for {len(summary_df)} buildings.\n"
    )

    
    with open('summary.txt', 'w') as f:
        f.write(report_content)
    
   
    print("\n" + report_content)



if __name__ == "__main__":
 
    manager = BuildingManager()
    

    print("--- Starting Data Ingestion ---")
    df_main = manager.load_data('data')
    
    if not df_main.empty:
    
        print("--- Generating Visualizations ---")
        generate_dashboard(df_main)
        
       
        print("--- Generating Reports ---")
        generate_reports(df_main)
        
        print("\nProcess Complete. Check directory for output files.")
    else:
        print("No data found in /data/ directory.")
        
     