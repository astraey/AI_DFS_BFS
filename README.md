# Artificial-Intelligence-UPF


- Depth-First Search: 
Usa un Stack. Expande lo mas profunfo posible primero

- Breathe-First Search
Usa una Cola

- Uniform Cost
f(n) = s(n)
El coste para llegar a un nodo es el coste acumulado hasta llegar a ese nodo

- A*
f(n) = g(n) + h(n)
Aqui usamos heursticas, una aproximación a una solución. Por ejemplo, tenemos un conjunto de ciudades, con barcelona y madrid y queremos una ruta optima. En linea recta habra 400Km, por tanto la H de la ruta sea 400. Esto nos está diciendo un coste aproximado. Una función heurstica es simplemente una aproximanción del coste. En el pacman por ejemplo, usaremos la distancia entre los dos puntos como heurística.
La estructura de datos en A* es la cola con prioridad. La prioridad de la cola es lo que nos interesa expandir primero. Lo que nos interesa expandir es lo que tenga un coste menor. 
Funcion de evaluación es lo que hemos invertido en llegar hasta ella + su eurística. Así se decide para que lado ir. Ojo que hay que volver a expandir nodos que ya hayas pasado, porque puede que sea mas corto. MIRAR FOTO 20 JAN 2017.

Si empata con la heurística, se pilla directamente. 

-Habiendo implementado A*, como sacamos uniform cost? lo mismo pero sin la heurística.

Para no volver a expandir un nodo, se puede guardar el elemento en una lista de nodos ya expandidos. La cosa va asi: Si pillamos un nodo y no lo hemos visitado y no es goal, lo expandimos. Adems, lo ponemos en un a lista de nodos ya expandidos para no volverlo a expandir. (Creo que esto es para el DFS, BFS). 
