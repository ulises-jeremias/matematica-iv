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

Sean $a = x_1 + y_{1}i, b = x_2 + y_{2}i \in \mathbb{C}$ tales que:

-   \|$a$\| $= r_a, arg(a) = \theta_a$
-   \|$b$\| $= r_b, arg(b) = \theta_b$

Definimos el producto complejo de la siguiente forma:

$$
	\begin{aligned}
		ab &= r_{a}r_{b} \textbf{e}^{i(\theta_a + \theta_b)} \\
			 &= {r_{a}r_{b}}_{(\theta_a + \theta_b)}
	\end{aligned}
$$

Luego, si $r_b = 1$ entonces la multiplicación funciona como rotación.

### Ejemplo Específico

**Movimiento Oscilatorio**

Para este ejemplo, queremos representar la posición de un objeto cuyo movimiento se muestra de la siguiente forma:

![][easy_harmonic_oscillator]

[easy_harmonic_oscillator]: https://github.com/ulises-jeremias/matematica-iv/blob/master/images/easy_harmonic_oscillator.gif

Podemos ver como se comporta el movimiento del objeto en el eje de los reales en la siguiente demostración gráfica.

![][complex_plane_sin]

[complex_plane_sin]: https://github.com/ulises-jeremias/matematica-iv/blob/master/images/complex_plane_sin.gif

Además, observamos en el siguiente gráfico como es el comportamiento del mismo en función de funciones trigonométricas conocidas.

![][complex_plane_cos_sin]

[complex_plane_cos_sin]: https://github.com/ulises-jeremias/matematica-iv/blob/master/images/complex_plane_cos_sin.gif

A partir de la animación anterior podemos observar los siguientes items:

En un caso ideal,

-	la posición en el eje real se comporta como una función *coseno*.
-	recordando los temas vistos en matemática II, sabemos que la razón de cambio de la función *coseno* está dada por la función *seno*.

Es decir, vamos a representar de alguna forma la posición como una función *coseno*, y que tan rápido cambie ese posición estará determinado por la función *seno*.

Pero, **¿a qué llamamos caso ideal?**.

El mundo físico no es ideal, y sabemos que la posición de un objeto cambia a medida que transcurre el tiempo. Necesitamos poder definir la posición del objeto en función del tiempo. La misma se comporta de la siguiente forma:

![][damped_oscillation]

[damped_oscillation]: https://github.com/ulises-jeremias/matematica-iv/blob/master/images/damped_oscillation.jpg

Para esto buscamos la forma de atenuar la función coseno que ya tenemos y vemos una forma de indicar cual será la amplitud inicial de la misma.

#### Amplitud

Para definir la amplitud inicial de la función coseno simplemente multiplicamos la posición del objeto por un número que signifique la amplitud inicial del resorte, *A*.

#### Periodo

Sabemos que la función cos recibe la variable $t$ como argumento en cada iteración. Luego, podemos evaluar como afectaría a la posición del objeto multiplicar ese tiempo $t$ por un valor real $\omega$.

#### Fase

Finalmente, determinamos cuan corrido está el dibujo de la función coseno en base a la fase $\phi$.

* * *

Se puede ver como los conceptos mencionados anteriormente afectan a la gráfica de una función sin en el siguiente [enlace](https://www.geogebra.org/m/KfUX66de).

Juntando todas las definiciones planteadas anteriormente, resumimos la posición del objeto en función del tiempo de la siguiente forma:

-	$x(t) = Acos(\omega t + \phi)$
-	$y(t) = Asin(\omega t + \phi)$

Particularmente, si tomamos la amplitud $A$ como la distancia de la caja al centro del plano es decir, el módulo de la posición, y sea $\theta = \omega t + \phi$, el argumento de la posición a lo largo del tiempo, tenemos la posición representada en **forma trinométrica**,

$r(t) = A (cos(\theta) + i sin(\theta))$

Sabemos a su vez que, si derivamos $x(t)$ ó $y(t)$ respecto de $t$, obtenemos la velocidad a la que se mueve el objeto, quedando la siguiente función de velocidad para cada uno respectivamente:

-	$v_{x}(t) = -A \omega sin(\omega t + \phi)$
-	$v_{y}(t) = A \omega cos(\omega t + \phi)$

## Análisis de Frecuencias

Respecto de este area de aplicaciones vamos a enfocarnos en dos casos de aplicación. A diferencia del ejemplo anterior, no disponemos de los conceptos necesarios para terminar de comprender los fundamentos detras de estos temas pero se espera ir profundizando a medida que transcurre la materia.

El código de los ejemplos que se plantean a continuación se puede encontrar en el siguiente [repositorio](https://github.com/ulises-jeremias/frequency-analysis-with-FFT) de github. En el mismo se puede encontrar una breve descripción de cada uno de los proyectos, objetivos de los mismos y formas de utilización. A continuación se muestra un resumen de los mismos.

### Generación de Terrenos

Como ejemplo tenemos la generación procedural de un terreno tridimensional utilizando **Perlin Noise** y la función [beginShape](https://processing.org/reference/beginShape_.html) de Processing.

### Análisis de Audio

#### ¿Por qué un visualizador de audio?

Mi objetivo principal al construir esto fue aprender más sobre ProcessingJS y Python, así como mostrar cómo funciona la Transformada Rápida de Fourier.

Sin embargo, usarlo en este proyecto me permitió visualizarlo literalmente, lo que lo hizo mucho más fácil de entender. Descubrí que tener un visualizador de música también facilitaba a la clase entender cuándo se presentó este proyecto.

##### ¿Qué es la Transformada Rápida de Fourier?

¡Bien, es una versión más rápida de la Transformada de Fourier! Pero para una respuesta real, una Transformada de Fourier es solo una forma diferente de ver el audio. Piensen en la apariencia de un MP3 cuando lo reproduce en una computadora: ¿pueden ver dónde el sonido se vuelve más alto y más silencioso en función de qué tan grandes son las formas de onda?

Por lo general, vemos música en el dominio del tiempo es decir, vemos cómo el audio cambia a medida que transcurre el tiempo. La Transformada de Fourier muestra el audio en el dominio de la frecuencia, es decir, en su lugar, vemos qué frecuencias están presentes en la canción y sus amplitudes (básicamente, qué tan fuertes o suaves son).

Entonces, si hay muchos graves pesados ​​en la canción, se mostrarán muchas frecuencias más bajas en el gráfico. Si una canción tiene muchos solos agudos de guitarra, la representación gráfica de la canción mostrará frecuencias mucho más altas.

##### ¿Cómo muestra este visualizador eso?

Afortunadamente, al usar la biblioteca P5.js, recibimos una biblioteca de sonidos que hace el trabajo dificil por nosotros, para que podamos entender mejor cómo el visualizador muestra una transformación de Fourier.

En pocas palabras, la forma en que funciona el visualizador es como la canción se reproduce, se ejecuta constantemente a través de una transformada de Fourier y el graficado de la salida. Entonces básicamente toma la canción en pedazos muy pequeños, la analiza con la transformada de Fourier y luego grafica los resultados.

#### Analizador de espectro de audio

En este proyecto, se puede ver cómo se representa gráficamente la función de onda de un audio recibido por micrófono en comparación con el espectro de la misma. Se utiliza `scipy.fftpack` para calcular la FFT y mostrar el espectro de audio en tiempo real usando algunas herramientas de Python.
