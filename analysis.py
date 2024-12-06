import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('D:\Assignment_4\data\ifood_df 1.csv')
    
    # Perform analysis (e.g., calculate mean)
    mean_value = data['Income'].mean()

    return {'mean': mean_value}
