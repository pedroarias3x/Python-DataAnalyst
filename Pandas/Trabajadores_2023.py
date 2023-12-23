import pandas as pd
import matplotlib.pyplot as plt



#Establecemos la ruta del fichero
archivo_origen = 'Empleados2023.xlsx'
#Leemos la hoja del excel y la llevamos a un dataframe
#hojas_excel = pd.ExcelFile(archivo_origen).sheet_names
df = pd.read_excel(archivo_origen,sheet_name='2023')
print(df)


# Sumar la facturación mensual por trabajador
df['Facturacion Anual'] = df.groupby('Trabajador')['Facturacion'].transform('sum')

# Obtener los 3 trabajadores que más han facturado anualmente
top_trabajadores = df.groupby('Trabajador')['Facturacion Anual'].max().nlargest(3)

print(df)

# Crear un gráfico de barras
plt.bar(top_trabajadores.index, top_trabajadores.values, color='blue')
plt.xlabel('Trabajador')
plt.ylabel('Facturacion Anual')
plt.title('Top 3 Trabajadores por Facturacion Anual')
plt.show()