# Cafeteria de la Pontificia Universidad Javeriana
**_Sebastian Enriquez y Jhon Silva_**

## Problema Central

La idea es poder automatizar el cobro de los almuerzos brindados por la cafeteria, así que se han fijado varios precios y descuentos por cada uno de los productos que se vende. La idea es poder tener en cuenta varias cosas a la hora de resolver el problema:
1. El rol de la persona, si es profesor o estudiante.
2. La cédula.
3. El código del producto.
4. La cantidad de unidades que pagará la persona.
5. El precio del producto.
6. Los descuentos, ya que el estudiante en sí tiene un descuento del 30%, el profesor tiene uno del 20% y los estudiantes becados tienen un 50% de descuento.

## Modelo Computacional

La solución del problema central se implemento en el lenguaje de python, el cual se puede ver en el archivo adjuntado con el nombre de **"Cafeteria Herramientas"**.

### Entrada
Basicamente, el algoritmo lee como entrada diversos datos personales y del producto para que el cliente pueda al fin y al cabo realizar la compra necesaria.

### Salida
La idea es que la salida del código en este caso sea de nada más y nada menos que solo una línea de la siguiente forma: El "**_Rol de la persona_**" con cédula "**_Número de la Cédula_**", debe pagar "**_Valor del producto_**" por el producto "**_Código del producto_**"

### Cálculos implementados
En este caso se necesitó de varios cáculos matemáticos para resolver el problema en particular, ya que era necesario calcular los descuentos de las personas con el valor de los productos, y si había una cantidad de productos a comprar mayor de uno también era necesario tenerlo en cuenta.

| Rol | Descuento |
| :-----: | :-----: |
| Estudiantes | 30 porciento |
| Profesores | 20 porciento  |
| Estudiantes Becados | 50 porciento |

![Logo Javeriana](https://www2.javerianacali.edu.co/sites/ujc/files/styles/img_noticias_290_125/public/node/announcement/field_image_box/logo_javeriana_cali_0_0_0.jpg?itok=pzdTtiVU)




