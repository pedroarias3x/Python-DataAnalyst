#Importamos el paquete de pandas
#Lo podemos instalar con pip install pandas
import pandas as pd
import numpy as np

print('Comenzamos ejecucion')
# Creamos un diccionario con datos ficticios
datos = {
    'Persona': [f'Persona_{i+1}' for i in range(20)],
    'Salario_mensual': np.random.randint(1000, 3000, size=20),
    'Facturacion': np.random.randint(1000, 12000, size=20),
}

# Creamos el DataFrame
df = pd.DataFrame(datos)

# Calculamos la columna de Margen
df['Margen'] = df['Facturacion'] - df['Salario_mensual']

# Mostramos el DataFrame
print(df)




