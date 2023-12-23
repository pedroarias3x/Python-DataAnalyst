#Importamos el paquete de pandas
#Lo podemos instalar con pip install pandas
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generar datos de ejemplo para 20 trabajadores y 12 meses en 2023
fecha_inicio = datetime(2023, 1, 1)
trabajadores = 20
meses = 12

# Creamos un diccionario con datos ficticios
datos = {
    'Persona': [f'Persona_{i+1}' for i in range(20)],
    'Salario_mensual': np.random.randint(2500, 7000, size=20),
    'Facturacion': np.random.randint(1000, 12000, size=20),
}


data = {
    "Nombre Trabajador": [f"Trabajador{i}" for i in range(1, trabajadores + 1) for _ in range(meses)],
    "ID Trabajador": [i for i in range(1, trabajadores + 1) for _ in range(meses)],
    "Fecha": [fecha_inicio + timedelta(days=30 * i) for i in range(meses) for _ in range(trabajadores)],
    "Facturación Mensual": [10000 + i * 500 for i in range(trabajadores) for _ in range(meses)],
    "Coste Salario Bruto Mensual": [6000 + i * 300 for i in range(trabajadores) for _ in range(meses)],
    "Otros Gastos Mensuales": [500 + i * 50 for i in range(trabajadores) for _ in range(meses)],
}

# Creamos el DataFrame
df = pd.DataFrame(datos)

# Calculamos la columna de Margen
df['Margen'] = df['Facturacion'] - df['Salario_mensual']




# Guardar en un archivo Excel
with pd.ExcelWriter('analisis_rentabilidad_2023.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Datos', index=False)

print("Archivo Excel creado exitosamente.")
