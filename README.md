# API de Gestión de Usuarios

Este proyecto es un sistema de gestión de usuarios que permite la creación, edición, activación, desactivación y eliminación de usuarios (CRUD). El sistema requiere autenticación de usuarios utilizando un token fijo para un servicio de autenticación que devuelve los datos del usuario y un token de sesión que se utilizará para los diferentes métodos que componen el CRUD según el estándar OAuth 2.0.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/cgaviria92/proyecto1.git
    cd proyecto1
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa: env\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno en el archivo `.env`:

    ```
    DATABASE_URL=sqlite:///./test.db
    GOOGLE_API_KEY=COLOCA UNA KEY AQUI
    SECRET_KEY=CARLOSgAVIRIA
    ```

5. Inicia el servidor de desarrollo:

    ```bash
    uvicorn app.main:app --reload
    ```

## Uso

### Documentación de la API

Puedes ver la documentación de la API en `http://127.0.0.1:8000/docs`.

### Puedes interactuar con la API, con el siguiente archivo para postamn:
proyecto1.postman_collection.json

#### Autenticación

- **POST /api/v1/auth/token**

  Autentica al usuario y devuelve un token JWT.

#### Usuarios

- **POST /api/v1/users/comprador**

  Crea un nuevo usuario comprador.

- **POST /api/v1/users/vendedor**

  Crea un nuevo usuario vendedor.

- **GET /api/v1/users**

  Devuelve una lista de todos los usuarios.

- **GET /api/v1/users/{user_id}**

  Devuelve los detalles de un usuario específico.

- **DELETE /api/v1/users/{user_id}**

  Elimina un usuario.

#### Geocodificación

- **GET /api/v1/geocode/geocodificar_base**

  Geocodifica usuarios y actualiza su latitud y longitud. Se puede usar solo una vez cada 24 horas.

#### auth

- **POST /api/v1/auth/token**

  Autenticación de usuarios para obtener el token tiene 2 horas de vigencia, por defecte se encuentra un usuario **admin admin**

- **POST /api/v1/auth/users**

  Creacion de usuarios para autenticarse en el sistema.

se realizo encriptación de contraseña en la base de datos y se uso outh2 

## Pruebas

### Pruebas unitarias

Para ejecutar las pruebas unitarias, asegúrate de que la aplicación esté ejecutándose y luego ejecuta:

```bash
pytest

