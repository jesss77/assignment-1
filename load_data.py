import pandas as pd 
from sqlalchemy import create_engine


csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(csv_url)

df.columns = [col.strip().replace(" ", "_") for col in df.columns]

USER = "postgres"
PASSWORD = "Admin@123"
HOST = "localhost"
PORT = "5432"
DBNAME = "etl_course"

# Use parameters instead of embedding password in URL
engine = create_engine(f"postgresql+psycopg2://{USER}@{HOST}:{PORT}/{DBNAME}",connect_args={"password": PASSWORD})


table_name = "students_data"
schema_name = "raw_data"

df.to_sql(table_name, engine, schema=schema_name, if_exists='replace', index=False)
print(f"Data loaded successfully into {table_name}!")
