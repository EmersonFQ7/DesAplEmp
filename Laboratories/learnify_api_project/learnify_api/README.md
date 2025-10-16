🎓 Learnify API: Gestor de Cursos Onlinelearnify_api es una API REST desarrollada con Django y Django REST Framework que permite gestionar cursos online y sus respectivos instructores. A través de sus endpoints, se puede realizar un CRUD completo (Crear, Leer, Actualizar, Eliminar) para ambas entidades, así como realizar búsquedas filtradas.🛠️ Tecnologías UsadasPython 3.xDjango 4.xDjango REST FrameworkSQLite3 (Base de datos por defecto de Django para desarrollo)🚀 Instrucciones para Ejecutar el ServidorSigue estos pasos para clonar el repositorio y poner en marcha el servidor de desarrollo localmente.Clona el repositorio:Bashgit clone https://github.com/tu_usuario/learnify_api.git
cd learnify_api
Crea y activa un entorno virtual:macOS/Linux:Bashpython3 -m venv venv
source venv/bin/activate
Windows:Bashpython -m venv venv
venv\Scripts\activate
Instala las dependencias:Bashpip install -r requirements.txt
(Nota: Asegúrate de tener un archivo requirements.txt. Puedes crearlo con pip freeze > requirements.txt)Aplica las migraciones a la base de datos:Bashpython manage.py migrate
Inicia el servidor de desarrollo:Bashpython manage.py runserver
La API estará disponible en http://127.0.0.1:8000/api/.🌐 Endpoints DisponiblesA continuación se detallan los endpoints de la API y ejemplos de cómo interactuar con ellos usando curl.Entidad: Instructores (/api/instructores/)MétodoEndpointDescripciónGET/api/instructores/Lista todos los instructores.POST/api/instructores/Crea un nuevo instructor.GET/api/instructores/{id}/Obtiene los detalles de un instructor.PUT/api/instructores/{id}/Actualiza completamente un instructor.DELETE/api/instructores/{id}/Elimina un instructor.Ejemplos curl para InstructoresListar todos los instructores:Bashcurl -X GET http://127.0.0.1:8000/api/instructores/
Crear un nuevo instructor:Bashcurl -X POST http://127.0.0.1:8000/api/instructores/ \
-H "Content-Type: application/json" \
-d '{"nombre": "Guido van Rossum", "especialidad": "Python"}'
Actualizar un instructor (ID=1):Bashcurl -X PUT http://127.0.0.1:8000/api/instructores/1/ \
-H "Content-Type: application/json" \
-d '{"nombre": "Guido van Rossum", "especialidad": "Core Python Developer"}'
Eliminar un instructor (ID=1):Bashcurl -X DELETE http://127.0.0.1:8000/api/instructores/1/
Entidad: Cursos (/api/cursos/)MétodoEndpointDescripciónGET/api/cursos/Lista todos los cursos.POST/api/cursos/Crea un nuevo curso.GET/api/cursos/{id}/Obtiene los detalles de un curso.PUT/api/cursos/{id}/Actualiza completamente un curso.DELETE/api/cursos/{id}/Elimina un curso.GET/api/cursos/?search=Busca cursos por nombre o nivel.Ejemplos curl para CursosListar todos los cursos:Bashcurl -X GET http://127.0.0.1:8000/api/cursos/
Crear un nuevo curso (asumiendo que el instructor con ID=2 existe):Bashcurl -X POST http://127.0.0.1:8000/api/cursos/ \
-H "Content-Type: application/json" \
-d '{"nombre": "Introducción a Django REST", "duracion": 40, "nivel": "Intermedio", "instructor": 2}'
Obtener detalles de un curso (ID=1):Bashcurl -X GET http://127.0.0.1:8000/api/cursos/1/
Respuesta de ejemplo mostrando la relación:JSON{
    "id": 1,
    "nombre": "Introducción a Django REST",
    "duracion": 40,
    "nivel": "Intermedio",
    "instructor": 2,
    "instructor_nombre": "Guido van Rossum"
}
Buscar cursos por nombre:Bashcurl -X GET "http://127.0.0.1:8000/api/cursos/?search=Django"
Buscar cursos por nivel:Bashcurl -X GET "http://127.0.0.1:8000/api/cursos/?search=Avanzado"
Eliminar un curso (ID=1):Bashcurl -X DELETE http://127.0.0.1:8000/api/cursos/1/