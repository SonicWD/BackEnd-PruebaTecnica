# Gestión de Clientes - Backend

## Descripción

Este es el backend para la aplicación de Gestión de Clientes. Proporciona una API RESTful para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en registros de clientes.

## Tecnologías Utilizadas

- Python 3
- FastAPI
- PostgreSQL
- Pydantic para validación de datos
- SQLAlchemy para ORM

## Estructura del Proyecto

```plaintext
backend/
│
├── app/
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── database.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Configuración y Ejecución para Local

### Requisitos Previos

- Python 3

### Pasos para Ejecutar

1. Clonar el repositorio:
    ```plaintext
    git clone https://github.com/SonicWD/BackEnd-PruebaTecnica
    cd BackEnd-PruebaTecnica

    
    ```
3. Rama DEV para ejecutar LOCAL

    ```plaintext
    git checkout dev
    ```
2. Crear y activar un entorno virtual:
    ```plaintext
    python -m venv venv
    source venv/bin/activate  
    # En Windows use `venv\Scripts\activate`
    ```

3. Instalar dependencias:
    ```plaintext
    pip install -r requirements.txt
    ```

4. Iniciar el servidor:
    ```plaintext
    uvicorn app.main:app --reload
    ```

El servidor estará ejecutándose en `http://localhost:8000`.

## API Endpoints

- `GET /`: Saludo
- `POST /create_client`: Crear un nuevo cliente
- `GET /list_clients`: Listar todos los clientes
- `PUT /update_client/{cliente_id}`: Actualizar un cliente
- `GET /get_client/{cliente_id}`: Obtener un cliente por ID
- `DELETE /delete_client/{cliente_id}`: Eliminar un cliente

Para más detalles, visite la documentación automática de la API en `http://localhost:8000/docs` después de iniciar el servidor.


## Despliegue

El backend está configurado para ser desplegado en Render. La rama de producción se despliega automáticamente.