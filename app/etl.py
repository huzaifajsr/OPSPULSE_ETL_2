import pandas as pd
import os
import time
from sqlalchemy import create_engine

def run_etl():
    # Extract
    df = pd.read_csv("data/sample.csv")

    # Transform
    df = df.dropna()
    df['processed'] = True

    # Load
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@db:5432/{os.getenv('DB_NAME')}"
    
    time.sleep(10)  # wait for DB to start
    engine = create_engine(db_url)

    df.to_sql("processed_data", engine, if_exists="replace", index=False)

    print("ETL pipeline executed successfully!")

if __name__ == "__main__":
    run_etl()