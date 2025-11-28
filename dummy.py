import pandas as pd
import numpy as np
import os
from datetime import datetime


os.makedirs('data', exist_ok=True)

def generate_dummy_data(building_name):
 
    dates = pd.date_range(end=datetime.now(), periods=24*30, freq='H')
    
    
    consumption = np.random.randint(10, 100, size=len(dates))
    
    df = pd.DataFrame({'timestamp': dates, 'kwh': consumption})
    
    
    filename = f"data/{building_name}.csv"
    df.to_csv(filename, index=False)
    print(f"Created {filename}")


generate_dummy_data("Building_A")
generate_dummy_data("Building_B")
generate_dummy_data("Science_Block")