# Git

"""
Git es un sistema de control de versiones que permite llevar un historial completo de los cambios en tus proyectos.
En lugar de trabajar con copias separadas de los archivos, Git organiza tod0 en un repositorio y registra qué se
agregó, modificó o eliminó, junto con la fecha y el autor del cambio. Esto facilita volver atrás si algo sale mal,
comparar versiones anteriores o trabajar en diferentes ramas (versiones paralelas del proyecto) sin perder información.

Además, Git está diseñado para el trabajo colaborativo. Con él puedes compartir tu repositorio en plataformas como
GitHub, GitLab o Bitbucket, lo que permite que varias personas trabajen sobre el mismo proyecto al mismo tiempo sin
pisarse los cambios. Gracias a esto, es una herramienta clave en programación, pero también puede usarse en otros
ámbitos: desde escribir documentos hasta gestionar imágenes, siempre que quieras mantener un control ordenado de
versiones.
"""

## Pasos y códigos
"""
- En una carpeta, la que quieras, y la que presentes avance alguno e interes sobre la misma debes abrir
un Bash en esa carpeta, con click derecho y ahí dice "open Git Bash here".

- $ git init : te permite abrir o inicializar un repositorio en base a esa carpeta elegida -> respositorio master
- $ git status : te permite ver cómo esta el repositorio (master) dentro, si tiene o no carpetas y notará si hubo
alguna actualización, por lo que te pedrá que añadas esos cambios (o "commits"), sea cual sea, con 'git add'
- $ git add . : te permite añadir los commits que realizaste al repositorio master.
- $ git add archivo.py(u otros tipos) : te permite añadir solamente un archivo (tambien es un commit) nuevo específico
- $ git commit -am "mensaje aclaratorio sobre el commit o commits" , así que esto es muy importante ya que informa
qué específicamente se hizo, asi que sé claro y consiso.

- OJO, OJO, OJO, seguramente no te tejará realizar lo anterior, sino que te preguntará "Who are you?" y como que 
te peirá loguearte con un nombre y email, esto es normal porque el git no sabe realmente quien eres y cuál es tu
función, asi que debes loguearte literalmente, procura que sea los mismos datos que usaste para el "Github" o "Githat":
- $ git config --global user.name "Tu Nombre"
- $ git config --global user.email "tu_correo@ejemplo.com"

- $ git log: te muestra el historial de los commits
- $ git branch: verifica en qué rama te encuentras. La rama principal es master, pero según indican los programadores
es mejor que lleve el nombre de "main", ya que ese mismo nombre lo consideran en GitHub.
- $ git branch -M main : ello cambiará el nombre de la rama actual a 'main', para mi caso pasará de 'master' a 'main'

"""
### Crear un nuevo repositorio
"""
Una vez iniciado el 'git init' en el repositorio master, ve a GitHub y crear un nuevo repositorio, basta con el nombre
y si quieres le agregas la descripción, lo demás por defecto. Una vez creado ello, te aparecerán líneas de comando
donde indica cómo se puede crear un repositorio por comandos, pero hay uno que si importa para VINCULAR tu repositorio
local con el de GitHub, y es algo similar a este -->
- $ git remote add origin https://github.com/BelParia/CERSEU_Modulo_I.git  , A TI TE GENERARÁ OTRO dX
Con esto puedes vincularlos y con ello ya estaría listo tu repositorio, se guardará localmente y vincluará con el GitHub.
- $ git remote -v : para verificar el repositorio remote en GitHub

- $ git push -u origin main : con GitHub ya reconocerá main como tu rama principal, y naturalmente se actualizará el
repositorio. Pero te pedirá una cuenta de GitHub, la cosa es que si no estasvinculado, tienes que hacerlo. Lo que hice
fue crear un tTokens (classic), con opción repo activa, y el Github te da un Token, ese es como tu contraseña,
te recomiendo preguntar a Chtgpt, o a mi Obsidian, ya que por aquí no te puedo llegar a guiar completamente.
OJO,OJO,OJO, una vez que todo esta vinculado, puedes ejecutar los comando de GIT en la misma terminal de Pycharm Dx.
Pero debes estar en la carpeta que posee el .git (este esta oculto en el master)
-git push origin main: actaulizará todos los commits, pero verifica mi obsidian, ya que tiene su orden y sus
características. Siendo que el 'git push' es para únicamente subir aquello que localmente se tiene historiado 
hacia el GitHub.

"""

## Crear ramas
"""
- `$ git branch` : verifica en que rama estas, si no creaste nunca antes o estas en master o en main, según defecto.
- `$ git branch nombre-rama` : te permite crear una nueva rama, puedes poner el nombre que quieras, pero evita usar 
espacios, además trata de que sea el título de todo lo que se desarrollará en esa rama. Pero no te moveras a esa 
nueva rama.
- `$ git checkout nombre-rama` : cambias de rama a nombre-rama
- `$ git checkout -b nueva-rama` : creas una nueva rama y directamente te cambias a esta, no necesitas los 2 codigos 
anteriores, es como un 'atajo'.
- `$ git branch -d nombre-rama` : si quieres eliminar una rama. Pero ojo, esto puede que solo llegue a eliminarse 
localmente, pero no lo hará en el GitHub, frente a esto es que debes aplicar lo siguiente:
- `$ git push origin --delete nombre-rama`
"""

## Clonar una rama
"""
- `$ git clone https://github.com/BelParia/CERSEU_Modulo_I.git` : este tiene por defecto la rama main, no cree otra 
pero cuando te pidan clonar algún repositorio, siempre habrá una rama específica, así que simplemente vas al GitHub 
ubicas el repostorio con su rama respectiva y en **<>Code** presionas para copiar el enlace HTTPS.
"""