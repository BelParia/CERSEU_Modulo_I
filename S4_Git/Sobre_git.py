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
- $ git commit -am"mensaje aclaratorio sobre el commit o commits" , así que esto es muy importante ya que informa
qué específicamente se hizo, asi que sé claro y consiso.

- OJO, OJO, OJO, seguramente no te tejará realizar lo anterior, sino que te preguntará "Who are you?" y como que 
te peirá loguearte con un nombre y email, esto es normal porque el git no sabe realmente quien eres y cuál es tu
función, asi que debes loguearte literalmente, procura que sea los mismos datos que usaste para el "Github" o "Githat":
- $ git config --global user.name "Tu Nombre"
- $ git config --global user.email "tu_correo@ejemplo.com"

"""