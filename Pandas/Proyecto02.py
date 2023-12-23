import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Configuración de Faker para generar nombres y ID ficticios
fake = Faker()

# Crear datos ficticios para 20 trabajadores y cada mes de 2023
num_trabajadores = 20
num_meses = 12
anio = 2023

# Lista de meses en 2023
meses_2023 = [datetime(anio, mes, 1).strftime('%B') for mes in range(1, num_meses + 1)]

# Crear datos
data = {
    'Nombre trabajador': [fake.name() for _ in range(num_trabajadores) for _ in range(num_meses)],
    'ID trabajador': [fake.uuid4() for _ in range(num_trabajadores) for _ in range(num_meses)],
    'Mes': meses_2023 * num_trabajadores,
    'Facturación mensual': [random.randint(0, 15000) for _ in range(num_trabajadores * num_meses)],
    'Coste Salario mensual bruto': [random.randint(3000, 8000) for _ in range(num_trabajadores * num_meses)],
    'Otros gastos mensuales': [random.randint(500, 1000) for _ in range(num_trabajadores * num_meses)]
}

df = pd.DataFrame(data)

# Exportar a un archivo Excel
excel_file_path = 'datos_trabajadores_2023.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Datos exportados a {excel_file_path}")
