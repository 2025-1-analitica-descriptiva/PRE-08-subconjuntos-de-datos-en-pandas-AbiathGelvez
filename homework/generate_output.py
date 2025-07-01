import pandas as pd
import os

# asegurarse de crear el directorio de salida
os.makedirs("files/output", exist_ok=True)

# leer el archivo CSV de entrada
df = pd.read_csv("files/input/truck_event_text_partition.csv")

# seleccionar las columnas de interés
columns_to_keep = ["driverId", "truckId", "eventTime", "eventType", "routeName"]

filtered_df = df[columns_to_keep]

# guardar el archivo de salida
filtered_df.to_csv("files/output/specific-columns.csv", index=False)

print("Archivo files/output/specific-columns.csv generado correctamente.")
