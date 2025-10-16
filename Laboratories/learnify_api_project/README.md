## 🔗 Enlace a la Demostración de la API

[Ver el video de validación CRUD en YouTube](https://www.youtube.com/watch?v=bNS4gms-2hQ)

# 🎓 Learnify API: Gestor de Cursos Online

`learnify_api` es una API REST desarrollada con Django y Django REST Framework que permite gestionar cursos online y sus respectivos instructores. A través de sus endpoints, se puede realizar un CRUD completo (Crear, Leer, Actualizar, Eliminar) para ambas entidades, así como realizar búsquedas filtradas.

---

## 🛠️ Tecnologías Usadas

* **Python 3.x**
* **Django 4.x**
* **Django REST Framework**
* **SQLite3** (Base de datos por defecto de Django para desarrollo)

---

## 🚀 Instrucciones para Ejecutar el Servidor

Sigue estos pasos para clonar el repositorio y poner en marcha el servidor de desarrollo localmente.

1.  **Clona el repositorio:**
    ```bash
    git clone 
    cd learnify_api
    ```

2.  **Crea y activa un entorno virtual:**
    * **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Instala las dependencias:**
    *(Nota: Primero, crea el archivo `requirements.txt` en tu terminal con `pip freeze > requirements.txt`)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones a la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La API estará disponible en `http://1227.0.0.1:8000/api/`.

---

## 🌐 Endpoints Disponibles

A continuación se detallan los endpoints de la API y ejemplos de cómo interactuar con ellos usando `curl`.

### Entidad: Instructores (`/api/instructores/`)

| Método | Endpoint                    | Descripción                        |
| :----- | :-------------------------- | :--------------------------------- |
| `GET`  | `/api/instructores/`        | Lista todos los instructores.      |
| `POST` | `/api/instructores/`        | Crea un nuevo instructor.          |
| `GET`  | `/api/instructores/{id}/`   | Obtiene los detalles de un instructor. |
| `PUT`  | `/api/instructores/{id}/`   | Actualiza completamente un instructor. |
| `DELETE`| `/api/instructores/{id}/`   | Elimina un instructor.             |

#### Ejemplos `curl` para Instructores

* **Listar todos los instructores:**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/instructores/](http://127.0.0.1:8000/api/instructores/)
    ```

* **Crear un nuevo instructor:**
    ```bash
    curl -X POST [http://127.0.0.1:8000/api/instructores/](http://127.0.0.1:8000/api/instructores/) \
    -H "Content-Type: application/json" \
    -d '{"nombre": "Guido van Rossum", "especialidad": "Python"}'
    ```

* **Actualizar un instructor (ID=1):**
    ```bash
    curl -X PUT [http://127.0.0.1:8000/api/instructores/1/](http://127.0.0.1:8000/api/instructores/1/) \
    -H "Content-Type: application/json" \
    -d '{"nombre": "Guido van Rossum", "especialidad": "Core Python Developer"}'
    ```

* **Eliminar un instructor (ID=1):**
    ```bash
    curl -X DELETE [http://127.0.0.1:8000/api/instructores/1/](http://127.0.0.1:8000/api/instructores/1/)
    ```

### Entidad: Cursos (`/api/cursos/`)

| Método | Endpoint                | Descripción                             |
| :----- | :---------------------- | :-------------------------------------- |
| `GET`  | `/api/cursos/`          | Lista todos los cursos.                 |
| `POST` | `/api/cursos/`          | Crea un nuevo curso.                    |
| `GET`  | `/api/cursos/{id}/`     | Obtiene los detalles de un curso.       |
| `PUT`  | `/api/cursos/{id}/`     | Actualiza completamente un curso.       |
| `DELETE`| `/api/cursos/{id}/`     | Elimina un curso.                       |
| `GET`  | `/api/cursos/?search=`  | Busca cursos por nombre o nivel.        |

#### Ejemplos `curl` para Cursos

* **Listar todos los cursos:**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/cursos/](http://127.0.0.1:8000/api/cursos/)
    ```

* **Crear un nuevo curso (asumiendo que el instructor con ID=2 existe):**
    ```bash
    curl -X POST [http://127.0.0.1:8000/api/cursos/](http://127.0.0.1:8000/api/cursos/) \
    -H "Content-Type: application/json" \
    -d '{"nombre": "Introducción a Django REST", "duracion": 40, "nivel": "Intermedio", "instructor": 2}'
    ```

* **Obtener detalles de un curso (ID=1):**
    ```bash
    curl -X GET [http://127.0.0.1:8000/api/cursos/1/](http://127.0.0.1:8000/api/cursos/1/)
    ```
    *Respuesta de ejemplo mostrando la relación:*
    ```json
    {
        "id": 1,
        "nombre": "Introducción a Django REST",
        "duracion": 40,
        "nivel": "Intermedio",
        "instructor": 2,
        "instructor_nombre": "Guido van Rossum"
    }
    ```
* **Buscar cursos por nombre:**
    ```bash
    curl -X GET "[http://127.0.0.1:8000/api/cursos/?search=Django](http://127.0.0.1:8000/api/cursos/?search=Django)"
    ```

* **Buscar cursos por nivel:**
    ```bash
    curl -X GET "[http://127.0.0.1:8000/api/cursos/?search=Avanzado](http://127.0.0.1:8000/api/cursos/?search=Avanzado)"
    ```

* **Eliminar un curso (ID=1):**
    ```bash
    curl -X DELETE [http://127.0.0.1:8000/api/cursos/1/](http://127.0.0.1:8000/api/cursos/1/)
    ```