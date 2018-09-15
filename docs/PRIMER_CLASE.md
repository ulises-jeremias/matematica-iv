# Primer Clase

## Introducción

En la clase dictada el día 7 de septiembre de 2018 se muestran áreas de aplicación de los números complejos. Para esto se repasan conceptos vistos en la teoría y se muestra la importancia de los mismos en el área del análisis de frecuencias, como pueden ser la generación procedural de terrenos en el plano tridimensional y análisis de audios.

A lo largo de la presentación se hace énfasis en los conceptos de amplitud, frecuencia y fase de una función trigonométrica para comprender así las distintas formas de representación de un número complejo y como es que los mismos se relacionan con las aplicaciones mencionadas.

Se puede ver el código de los ejemplos planteados en el directorio `examples` de este repositorio o en el siguiente [repositorio de github](https://github.com/ulises-jeremias/frequency-analysis-with-FFT).

## Resumen de la clase

Como se menciona anteriormente, los contenidos de la clase son aplicaciones de los Números Complejos.

Hablar de aplicaciones de los números complejos es algo dificil debido a que están presentes en muchisimas cosas, más de las que podemos imaginar y preguntarnos para que los utilizamos es equivalente a preguntarnos ¿para qué sirven los números naturales?, ¿para qué utilizamos números reales?. La respuesta a estas preguntas es simple.

Los números naturales los utilizamos para contar, es decir que todo problema que se plantee en el dominio del conteo se va a relacionar con este conjunto de números.

Por otro lado, los números reales surgen como una necesidad para poder representar nuevas cantidades. Para la época en la que surgen estos números ya se tenían en cuenta los racionales, números los cuales se sabía que los egipcios utilizaban para la resolución de problemas prácticos, sin embargo, fue con el desarrollo de la matemática griega cuando se consideró el aspecto filosófico de *número*. Los pitagóricos descubrieron que las relaciones armónicas entre las notas musicales correspondían a cocientes de números enteros, lo que les inspiró a buscar proporciones numéricas en todas las demás cosas, y lo expresaron con la máxima **todo es número**. Posteriormente, se obtiene que no toda cantidad es un número racional y es ahí cuando surge la necesidad de definir una nueva forma de representar las cantidades, y nuevamente, como una necesidad se definen los números reales.

De todo esto, podemos ver que los números surgen a lo largo de la historia como una necesidad para representar cantidades y aspectos del mundo físico y los números complejos no son una excepción. Surgen como una necesidad para resolver la busqueda de raices de determinados polinomios de grado 2 y 3. Por nuestra parte, vamos a evaluar como es que nos sirven los números complejos y como es que nos sirve entender cada uno de los conceptos detras de los mismos.

## Aplicaciones

Como todo conjunto de números, los números complejos son herramientas. Es importante entender que, para algunos de los ejemplos que se plantean a continuación uno podría ignorar la existencia de los números complejos, pero siempre es importante conocer las herramientas de las que uno dispone al momento de resolver un problema y especialmente cuando existe alguna ventaja al momento de utilizarlas.

Para resumir las aplicaciones existente vamos a separar las mismas en dos categorías.

### Representación de objetos en el plano bidimensional

Este es el aspecto de los números complejos en el que pienso primero si tengo que nombrar aplicaciones de los mismos. Como se sabe, los números complejos no solo extienden el conjunto de los números reales desde un punto de vista algebraico, sino tambien desde un punto geometrico. El plano complejo es una extensión de la linea numérica unidimensional en el cual se añade un eje, el *eje imaginario*, el cual permite representar punto en un plano bidimensional. Estos puntos son números complejos.

### Análisis de Frecuencias

Como se menciona anteriormente, existen ejemplos en los que uno podría ignorar la existencia de los números complejos y resolver los problemas de alguna forma similar o incluso más eficiente. Particularmente, este no es el caso. En esta categoría se muestran ejemplos de aplicación en los que los números complejos definen exactamente las cantidades que queremos manipular y representar para la resolución de un problema dado.

Entre los ejemplos tenemos,

-   Generación de terrenos en un plano tri-dimensional
-   Análisis de Audio
-   entre otros

## Representación de Objetos

### Traslaciones y Rotaciones

Los números complejos forman un **Cuerpo**, por lo que dos números complejos a y b pueden sumarse y multiplicarse. Veremos más adelante en la materia lo que es un **Cuerpo**, pero por ahora quedemonos con el concepto de que la suma y la multiplicación son operaciones definidas en los números complejos, es decir, estan definidas y pueden utilizarse.

Geometricamente hablando, los números complejos se suman como vectores euclideos, aunque también se puede ver como la suma de dos polinomios.
La suma de dos números complejos puede entenderse como la traslacion de un punto en el plano y esto me puede permitir una forma rápida de definir el movimiento de un objeto en el plano complejo.

Por otro lado, la multiplicación de dos números complejos se puede expresar más fácilmente en coordenadas polares:

Sean <img src="svgs/ed9a41f86371c04599f858809297df9b.svg?invert_in_darkmode" align=middle width=214.76392409999994pt height=22.831056599999986pt/> tales que:

-   |<img src="svgs/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode" align=middle width=8.68915409999999pt height=14.15524440000002pt/>| <img src="svgs/442b001a242fceec20d4a8c75239b6cd.svg?invert_in_darkmode" align=middle width=123.25798979999998pt height=24.65753399999998pt/>
-   |<img src="svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode" align=middle width=7.054796099999991pt height=22.831056599999986pt/>| <img src="svgs/03b5060dca839af3223c0ec9049f5a20.svg?invert_in_darkmode" align=middle width=118.92452549999999pt height=24.65753399999998pt/>

Definimos el producto complejo de la siguiente forma:

<p align="center"><img src="svgs/f912fa0d108eaa4945b4f2061199110d.svg?invert_in_darkmode" align=middle width=126.46720349999998pt height=46.2392733pt/></p>
