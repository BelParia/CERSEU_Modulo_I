print("*** Entornos virtuales ***")

# Entornos virtuales
"""Mira, este punto es muy importante, ya que como sabrás los entornos virtuales son muy personalizables
porque le puedes instalar las librerías que tu quieras, no hay límite.

RECUERDA: siempre antes de realizar tus trabajos/proyectos no olvides revisar el entorno en el que 
estas trabajando, sino te caerá más funa que el MR.Funas. OJO"""

## Librerías
"""-Para INSTALAR LIBRERÍAS simplemente ve al 'sanguchito'>'Setings', aquí buscas tu Entorno virtual, fíjate 
en el nomnbre, cuidado lo instales para otro entorno Dx. Luego hay un simbolo '+', y ahí estan todas las
librerías que existen, asi que simplemente buscas, seleccionas e instalas.
-Revisa si esa librería es la original, casi siempre tienen una dirección github, que no te metan la rata
-Yo, hasta este momento, instalé: 
(i) pandas -> maneja de bases de datos complejas, pero es un tanto lento
(ii) pdf-maker -> permite crear 'pdfs' de los que 
(iii) django -> creo que es para crear aplicaiones, o algo así
(iv) pyspark -> manejo de bases de datos complejas y es mucho más rápida que 'pandas'. Mucho mejor
(v) cada vez que instales una librería, existe la posibilidad de que se instalen otras, son propiamente dependencias

- Tambien puedes Instalar Librerías, manualmente, en base a COMANDOS, como los siguientes:"""
### pip install django , como notas no tiene la versión, ya que ese te instala la última versión que encuentre
### pip install django==5.01 , así puedes instalar la versión específica que deseas
### pip unistall django , desintalará la librería con ese nombre, no importa la versión
### pip freeze , por consola (tipo local) te permite verificar todos las librerías que ya instalaste
"""pip es el 'gestor de paquetes de Python', como pasa con otros lenguajes o SO, asi que te permite instalar, 
verificar, actualizar, desinstalar, y una u otra cosa más. Actualiza siempre su 'pip' con :"""
### python.exe -m pip install --upgrade pip

## Instalar conjunto de librerías
### pip freeze > ./requirements.txt , esto genera un .txt with nombres de todas tus libreías que instalaste
"""Con justo ese archivo es que puedes instalar todas las librerías que lleva dentro a un NUEVO entorno virtual"""
### pip install -r requirements.txt , instalas todas las librerías que lleva requirements.txt



