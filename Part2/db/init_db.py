import pandas as pd
from sqlalchemy import create_engine


conn_str =  (
    "mssql+pyodbc://MEHAK-PC/BMW_VIN"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(conn_str)

vin = pd.read_csv("Part2/data/vin.csv")
parts = pd.read_csv("Part2/data/parts.csv")
mapping = pd.read_csv("Part2/data/mapping.csv")

vin.to_sql("Car", engine, if_exists="replace", index=False)
parts.to_sql("Part", engine, if_exists="replace", index=False)
mapping.to_sql("CarPartMap", engine, if_exists="replace", index=False)

print("Data uploaded to MSSQL successfully.")
