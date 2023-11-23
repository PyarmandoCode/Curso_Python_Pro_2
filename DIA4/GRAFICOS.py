

# fig, ax = plt.subplots()
#
# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#
# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')
#
# plt.show()


"""
Grafico de Linea

import matplotlib.pyplot as plt
#todo datos
x = [1,2,3,4,5]
y= [2,4,6,7,10]
#todo crear el grafico de linea
plt.plot(x,y)
#todo etiquetas
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafico de Linea')
#Mostrar el Grafico
plt.show()
"""


"""
Grafico Barras (Ventas)

categorias = ['A','B','C','D']
ventas = [7,3,10,5]

#todo crear el grafico de barras
plt.bar(categorias,ventas)

#todo etiquetas y titulos

plt.xlabel('Categorias')
plt.ylabel('Ventas')
plt.title('Grafico de Barras')

#todo mostrar el grafico
plt.show()
"""

"""
Grafico PIE (Ventas)
"""
import matplotlib.pyplot as plt
#todo datos
categorias = ['A','B','C','D']
ventas = [7,3,10,5]

#todo crear el grafico
plt.figure(figsize=(6,6))
plt.pie(ventas,labels=categorias,autopct='%1.1f%%', startangle=140)

#todo titulo grafico
plt.title("Ventas Noviembre 2023")

#todo mostrar el grafico
plt.show()











