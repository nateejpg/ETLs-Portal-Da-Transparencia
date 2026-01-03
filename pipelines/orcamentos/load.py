import os
import pandas as pd
from sqlalchemy import create_engine

# CREATE DW CONNECTION

DB_HOST = "postgres-dw"
DB_PORT = "5432"
DB_NAME = "orcamentos_dw"
DB_USER = "admin"
DB_PASS = "password123"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

CSV_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/processed/orcamentos/orcamento_despesa_clean.csv"
    )
)

def load_to_postgres():
    if not os.path.exists(CSV_PATH):
        print(f"Error: File not found at {CSV_PATH}")
        return
    
    print("Reading processed CSV")
    df = pd.read_csv(CSV_PATH)

    print(f"Conencting to Data Warehouse ({DB_HOST})...")
    engine = create_engine(DATABASE_URL)

# LOAD TO DW

    print("Inserting data into table 'despesas_publicas'...")
    df.to_sql("despesas_publicas", engine, if_exists="replace", index=False)

    print("Data loaded successfully!")

if __name__ == "__main__":
    load_to_postgres()