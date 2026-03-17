import pandas as pd

def preprocess(df):
    df = df.copy()

    
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

    
    df['price'] = pd.to_numeric(df['weighted_average_price'], errors='coerce')

    
    df['load'] = 1 - (df['available_seats'] / df['total_seats'])

    
    df['rating'] = pd.to_numeric(df['bus_score'], errors='coerce')

    
    df['reviews'] = pd.to_numeric(df['number_of_reviews'], errors='coerce')

    
    df['rank'] = df['srp_rank'].str.split("/").str[0]
    df['rank'] = pd.to_numeric(df['rank'], errors='coerce')

    
    df = df.dropna(subset=['price', 'load', 'rating', 'reviews'])

    print("✅ Preprocessing Complete")
    return df