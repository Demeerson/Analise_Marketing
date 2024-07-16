import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel('teste.xlsx')

# Definir a consulta SQL para calcular o total de clientes por intervalo de hora
consulta_sql = """
SELECT 
    CASE 
        WHEN strftime('%M', Hora) BETWEEN '00' AND '59' THEN strftime('%H', Hora) || ':00 - ' || strftime('%H', Hora) || ':59'
    END AS intervalo_hora,
    COUNT(Cliente) AS total_clientes
FROM 
    df
GROUP BY 
    intervalo_hora
ORDER BY 
    intervalo_hora;  -- Ordenar do maior para o menor
"""

# Executar a consulta SQL usando pandasql
resultado = sqldf(consulta_sql, locals())

# Plotar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(resultado['intervalo_hora'], resultado['total_clientes'], color='skyblue')
plt.xlabel('Intervalo de Hora')
plt.ylabel('Total de Clientes')
plt.title('Total de Clientes por Intervalo de Hora')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
