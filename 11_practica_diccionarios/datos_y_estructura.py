menu = (
"""----------------------------------------------------------
         Programa escuela
----------------------------------------------------------
1-Listar los estudiantes por orden ascendente.
2-Mostrar el promedio de notas para cada estudiante.
3-Listar datos de los estudiantes que cursan el programa de “Ingenieria en Informatica”. 
4-Mostrar el promedio de edad de los estudiantes.
5-Mostrar nombre y apellido del alumno con mayor pomedio de notas. 
6-Listar a los estudiantes que forman el grupo “Club de Informática”, con sus respectivos promedios. 
7-Listar a los estudiantes más jóvenes (debajo de la edad promedio), con su respectivo programa.
8-Finalizar programa.
----------------------------------------------------------""")
comprobar = ('''----------------------------------------------------------
¿Está seguro que desea finalizar el programa?
(s/n):''')
estudiantes=[{
  "legajo": 1,
  "nombre": "Juan",
  "apellido": "Linarez",
  "edad": 21,
  "notas": [    8,    9,    6  ],
  "programa": { "nombre": "Ingenieria en Informatica", "nivel": "pregrado" },
  "grupos": [    {"nombre": "Club de Ajedrez","descripcion": "Grupo de jugadores de Ajedrez"},
    			{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia"}]
},
{
  "legajo": 2,
  "nombre": "Carla",
  "apellido": "Salas",
  "edad": 18,
  "notas": [    7,    5  ],
  "programa": {"nombre": "Medicina","nivel": "pregrado"},
  "grupos": [ {"nombre": "Club de Volleyball","descripcion": "Equipo de Volleyball de la universidad."} ]
},
{
  "legajo": 3,
  "nombre": "Jorge",
  "apellido": "Rodriguez",
  "edad": 31,
  "notas": [    4,    9,    6  ],
  "programa": {"nombre": "Ingenieria Civil","nivel": "postgrado"}
},
{
  "legajo": 4,
  "nombre": "Maria",
  "apellido": "Sandoval",
  "edad": 24,
  "notas": [   6,    7,    6,    5  ],
  "programa": {"nombre": "Ingenieria en Informatica","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia" }]
},
{
  "legajo": 5,
  "nombre": "William",
  "apellido": "Smith",
  "edad": 25,
  "notas": [    6,    5,    8  ],
  "programa": {"nombre": "Bachiller","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de PS4","descripcion": "Grupo de jugadores de Playstation 4"}]
},
{
  "legajo": 6,
  "nombre": "Juan",
  "apellido": "Gomez",
  "edad": 21,
  "notas": [   8,    9,    6  ],
  "programa": {"nombre": "Ingenieria en Informatica","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Ajedrez","descripcion": "Grupo de jugadores de Ajedrez"},
  			{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia"} ]
},
{
  "legajo": 7,
  "nombre": "Maria",
  "apellido": "Cadenas",
  "edad": 18,
  "notas": [    5,    4  ],
  "programa": {"nombre": "Medicina","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Volleyball","descripcion": "Equipo d eVolleyball de la universidad."}]
},
{
  "legajo": 8,
  "nombre": "Jorge",
  "apellido": "Ayala",
  "edad": 31,
  "notas": [    4,    9,    6  ],
  "programa": {"nombre": "Ingenieria Civil","nivel": "postgrado"}
},
{
  "legajo": 9,
  "nombre": "Luis",
  "apellido": "Sandoval",
  "edad": 24,
  "notas": [    5,    7,    6,    4  ],
  "programa": {"nombre": "Ingenieria en Informatica","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia" }]
},
{
  "legajo": 10,
  "nombre": "Marcos",
  "apellido": "Rojo",
  "edad": 29,
  "notas": [    6,    8,    7  ],
  "programa": {"nombre": "Bachiller","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de PS4","descripcion": "Grupo de jugadores de Playstation 4"}]
}
]