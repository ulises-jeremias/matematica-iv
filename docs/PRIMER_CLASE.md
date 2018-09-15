# Primer Clase

## Introducción

En la clase dictada el día 7 de septiembre de 2018 se muestran áreas de aplicación de los números complejos. Para esto se repasan conceptos vistos en la teoría y se muestra la importancia de los mismos en el área del análisis de frecuencias, como pueden ser la generación procedural de terrenos en el plano tridimensional y análisis de audios.

A lo largo de la presentación se hace énfasis en los conceptos de amplitud, frecuencia y fase de una función trigonométrica para comprender así las distintas formas de representación de un número complejo y como es que los mismos se relacionan con las aplicaciones mencionadas.

Se puede ver el código de los ejemplos planteados en el directorio `examples` de este repositorio o en el siguiente [repositorio de github](https://github.com/ulises-jeremias/frequency-analysis-with-FFT).

## Resumen de la clase

Como se menciona anteriormente, el contenido de la clase es aplicaciones de los Números Complejos.

Hablar de aplicaciones de los números complejos es algo dificil debido a que están presentes en muchisimas cosas, más de las que podemos imaginar y preguntarnos para que los utilizamos es equivalente a preguntarnos ¿para qué sirven los números naturales?, ¿para qué utilizamos números reales?. La respuesta a estas preguntas es simple.

Los números naturales los utilizamos para contar, es decir que todo problema que se plantee en el dominio del conteo se va a relacionar con este conjunto de números.

Por otro lado, los números reales surgen como una necesidad para poder representar nuevas cantidades. Para la época en la que surgen estos números ya se tenían en cuenta los racionales, números los cuales se sabía que los egipcios utilizaban para la resolución de problemas prácticos, sin embargo, fue con el desarrollo de la matemática griega cuando se consideró el aspecto filosófico de _número_. Los pitagóricos descubrieron que las relaciones armónicas entre las notas musicales correspondían a cocientes de números enteros, lo que les inspiró a buscar proporciones numéricas en todas las demás cosas, y lo expresaron con la máxima **todo es número**. Posteriormente, se obtiene que no toda cantidad es un número racional y es ahí cuando surge la necesidad de definir una nueva forma de representar las cantidades, y nuevamente, como una necesidad se definen los números reales.

De todo esto, podemos ver que los números surgen a lo largo de la historia como una necesidad para representar cantidades y aspectos del mundo físico y los números complejos no son una excepción. Surgen como una necesidad para resolver la busqueda de raices de determinados polinomios de grado 2 y 3. Por nuestra parte, vamos a evaluar como es que nos sirven los números complejos y como es que nos sirve entender cada uno de los conceptos detras de los mismos.

## Aplicaciones

Como todo conjunto de números, los números complejos son herramientas. Es importante entender que, para algunos de los ejemplos que se plantean a continuación uno podría ignorar la existencia de los números complejos, pero siempre es importante conocer las herramientas de las que uno dispone al momento de resolver un problema y especialmente cuando existe alguna ventaja al momento de utilizarlas.

Para resumir las aplicaciones existente vamos a separar las mismas en dos categorías.

### Representación de objetos en el plano bidimensional

Este es el aspecto de los números complejos es el que pienso primero si tengo que nombrar aplicaciones de los mismos. Como se sabe, los números complejos no solo extienden el conjunto de los números reales desde un punto de vista algebraico, sino tambien desde un punto geometrico. El plano complejo es una extensión de la linea numérica unidimensional en el cual se añade un eje, _imaginario_, el cual permite representar puntos en un plano bidimensional. Estos puntos son números complejos.

### Análisis de Frecuencias

Como se menciona anteriormente, existen ejemplos en los que uno podría ignorar la existencia de los números complejos y resolver los problemas de alguna forma similar o incluso más eficiente. Particularmente, este no es el caso. En esta categoría se muestran ejemplos de aplicación en los que los números complejos definen exactamente las cantidades que queremos manipular y representar para la resolución de un problema dado.

Entre los ejemplos tenemos,

-   Generación de terrenos en un plano tridimensional
-   Análisis de Audio
-   entre otros

## Representación de Objetos

### Traslaciones y Rotaciones

Los números complejos forman un **Cuerpo**, por lo que dos números complejos a y b pueden sumarse y multiplicarse. Veremos más adelante en la materia lo que es un **Cuerpo**, pero por ahora quedemonos con el concepto de que la suma y la multiplicación son operaciones definidas en los números complejos, es decir, estan definidas y pueden utilizarse.

Geometricamente hablando, los números complejos se suman como vectores euclideos, aunque también se puede ver como la suma de dos polinomios.
La suma de dos números complejos puede entenderse como la traslacion de un punto en el plano y esto me puede permitir una forma rápida de definir el movimiento de un objeto en el plano complejo.

Por otro lado, la multiplicación de dos números complejos se puede expresar más fácilmente en coordenadas polares:

Sean <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/ed9a41f86371c04599f858809297df9b.svg" align=middle width=214.76392409999994pt height=22.831056599999986pt/> tales que:

-   \|<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/44bc9d542a92714cac84e01cbbb7fd61.svg" align=middle width=8.68915409999999pt height=14.15524440000002pt/>\| <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/442b001a242fceec20d4a8c75239b6cd.svg" align=middle width=123.25798979999998pt height=24.65753399999998pt/>
-   \|<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg" align=middle width=7.054796099999991pt height=22.831056599999986pt/>\| <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/03b5060dca839af3223c0ec9049f5a20.svg" align=middle width=118.92452549999999pt height=24.65753399999998pt/>

Definimos el producto complejo de la siguiente forma:

<p align="center"><img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/f07be012cb603c3dfbdf3eb5793a1ff5.svg" align=middle width=126.46716225pt height=46.2392733pt/></p>

Luego, si <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/2249583b4d6d09d50a0232b38db9563d.svg" align=middle width=44.15589254999999pt height=21.18721440000001pt/> entonces la multiplicación funciona como rotación.

### Ejemplo Específico

**Movimiento Oscilatorio**

Para este ejemplo, queremos representar la posición de un objeto cuyo movimiento se muestra de la siguiente forma:

![][easy_harmonic_oscillator]

[easy_harmonic_oscillator]: ../images/easy_harmonic_oscillator.gif

Podemos ver como se comporta el movimiento del objeto en el eje de los reales en la siguiente demostración gráfica.

![][complex_plane_sin]

[complex_plane_sin]: ../images/complex_plane_sin.gif

Además, observamos en el siguiente gráfico como es el comportamiento del mismo en función de funciones trigonométricas conocidas.

![][complex_plane_cos_sin]

[complex_plane_cos_sin]: ../images/complex_plane_cos_sin.gif

A partir de la animación anterior podemos observar los siguientes items:

En un caso ideal,

-		la posición en el eje real se comporta como una función *coseno*.
-		recordando los temas vistos en matemática II, sabemos que la razón de cambio de la función *coseno* está dada por la función *seno*.

Es decir, vamos a representar de alguna forma la posición como una función *coseno*, y que tan rápido cambie ese posición estará determinado por la función *seno*.

Pero, **¿a qué llamamos caso ideal?**.

El mundo físico no es ideal, y sabemos que la posición de un objeto cambia a medida que transcurre el tiempo. Necesitamos poder definir la posición del objeto en función del tiempo. La misma se comporta de la siguiente forma:

![][damped_oscillation]

[damped_oscillation]: ../images/damped_oscillation.jpg

Para esto buscamos la forma de atenuar la función coseno que ya tenemos y vemos una forma de indicar cual será la amplitud inicial de la misma.

#### Amplitud

Para definir la amplitud inicial de la función coseno simplemente multiplicamos la posición del objeto por un número que signifique la amplitud inicial del resorte, *A*.

#### Periodo

Sabemos que la función cos recibe la variable <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/4f4f4e395762a3af4575de74c019ebb5.svg" align=middle width=5.936097749999991pt height=20.221802699999984pt/> como argumento en cada iteración. Luego, podemos evaluar como afectaría a la posición del objeto multiplicar ese tiempo <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/4f4f4e395762a3af4575de74c019ebb5.svg" align=middle width=5.936097749999991pt height=20.221802699999984pt/> por un valor real <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/ae4fb5973f393577570881fc24fc2054.svg" align=middle width=10.82192594999999pt height=14.15524440000002pt/>.

#### Fase

Finalmente, determinamos cuan corrido está el dibujo de la función coseno en base a la fase <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/f50853d41be7d55874e952eb0d80c53e.svg" align=middle width=9.794543549999991pt height=22.831056599999986pt/>.

* * *

Se puede ver como los conceptos mencionados anteriormente afectan a la gráfica de una función sin en el siguiente [enlace](https://www.geogebra.org/m/KfUX66de).

Juntando todas las definiciones planteadas anteriormente, resumimos la posición del objeto en función del tiempo de la siguiente forma:

-		<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/849dc24edccc420adbf6be999b851e1d.svg" align=middle width=144.57945479999998pt height=24.65753399999998pt/>
-		<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/bf3bc66e826bcc8648f3e2102dce8206.svg" align=middle width=144.28192019999997pt height=24.65753399999998pt/>


Particularmente, si tomamos la amplitud <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/53d147e7f3fe6e47ee05b88b166bd3f6.svg" align=middle width=12.32879834999999pt height=22.465723500000017pt/> como la distancia de la caja al centro del plano es decir, el módulo de la posición, y sea <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/eb7c10fffd9c39df70d5c92ed11a4239.svg" align=middle width=76.73489669999998pt height=22.831056599999986pt/>, el argumento de la posición a lo largo del tiempo, tenemos la posición representada en **forma trinométrica**,

<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/ec5ba7b70330c68f75052f6c82181193.svg" align=middle width=187.32160424999998pt height=24.65753399999998pt/>

Sabemos a su vez que, si derivamos <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/f92a2fed82f1dacdec6e4d5a05fbbf97.svg" align=middle width=28.11651809999999pt height=24.65753399999998pt/> ó <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/d4378ba898213096600125929214f90a.svg" align=middle width=27.37073789999999pt height=24.65753399999998pt/> respecto de <img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/4f4f4e395762a3af4575de74c019ebb5.svg" align=middle width=5.936097749999991pt height=20.221802699999984pt/>, obtenemos la velocidad a la que se mueve el objeto, quedando la siguiente función de velocidad para cada uno respectivamente:

-		<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/97b3eabab0cd2666843efd89c8022148.svg" align=middle width=175.4843871pt height=24.65753399999998pt/>
-		<img src="https://github.com/ulises-jeremias/matematica-iv/blob/master/docs/svgs/0f241985110624c2d8f15a74c9f2dbe0.svg" align=middle width=161.87594115pt height=24.65753399999998pt/>
