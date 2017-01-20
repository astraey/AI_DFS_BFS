jonathan.ferrer@upf.edu
enviar mail

# Artificial-Intelligence-UPF

http://inst.eecs.berkeley.edu/~cs188/pacman/search.html

compilador: pycharm community edition

- Depth-First Search: 
Usa un Stack. Expande lo mas profunfo posible primero

pseudocodigo dfs:
1  procedure DFS-iterative(G,v):
2      let S be a stack
3      S.push(v)
4      while S is not empty
5          v = S.pop()
6          if v is not labeled as discovered:
7              label v as discovered
8              for all edges from v to w in G.adjacentEdges(v) do
9                  S.push(w)

- Breathe-First Search
Usa una Cola

- Uniform Cost
usar priority queue

f(n) = s(n)
El coste para llegar a un nodo es el coste acumulado hasta llegar a ese nodo

- A*

usar priority queue

f(n) = g(n) + h(n)
Aqui usamos heursticas, una aproximación a una solución. Por ejemplo, tenemos un conjunto de ciudades, con barcelona y madrid y queremos una ruta optima. En linea recta habra 400Km, por tanto la H de la ruta sea 400. Esto nos está diciendo un coste aproximado. Una función heurstica es simplemente una aproximanción del coste. En el pacman por ejemplo, usaremos la distancia entre los dos puntos como heurística.
La estructura de datos en A* es la cola con prioridad. La prioridad de la cola es lo que nos interesa expandir primero. Lo que nos interesa expandir es lo que tenga un coste menor. 
Funcion de evaluación es lo que hemos invertido en llegar hasta ella + su eurística. Así se decide para que lado ir. Ojo que hay que volver a expandir nodos que ya hayas pasado, porque puede que sea mas corto. MIRAR FOTO 20 JAN 2017.

Si empata con la heurística, se pilla directamente. 

-Habiendo implementado A*, como sacamos uniform cost? lo mismo pero sin la heurística.

Para no volver a expandir un nodo, se puede guardar el elemento en una lista de nodos ya expandidos. La cosa va asi: Si pillamos un nodo y no lo hemos visitado y no es goal, lo expandimos. Adems, lo ponemos en un a lista de nodos ya expandidos para no volverlo a expandir. (Si, solo para el DFS, BFS). Esto no se hace con el uniform Cost y el A* porque nos interesa saber si para llegar a un nodo se puede llegar por 2 caminos.


Adimisble heuristic:
la heuristica que utilitzem te que ser igual o menor que la heuristica optima
h <= h* (h* => heuristica optima)

Heuristica consistent:

cost per arribar de un node n a un node n' (siguen n' el seu fill) + heurisitca de n' <= heuristica node pare.

Heuristica no trivial:

no 0 -> no serveix de re
heuristica que computi el cost total -> petara en temps.+


fer exercicis 1 a 6
7 i 8 opcionals (15% mes de nota)


entrega:
grups de 2
no copiar plz

entregar en un zip o tar formato P1_NIA1_NIA2
debe contener:
search.py
searchAgents.py

hay que indicar en la entrega:
que funciona 
que no funciona 
que problemas encontramos
breu resposa a les preguntes que fan a ala web

entrega dijous 2 febrer  23:55


VIP USAR Pila, cua y cua prioritat

un nodo tiene el estado el coste la accion y el nodo padre
un estado tiene la posicion

->>linux si es cau xord editar linia 217 de graphicUtils.py 
