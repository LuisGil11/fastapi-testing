## Pasos para iniciar el proyecto

1. iniciar el ambiente virtual
   ```
   venv\Scripts\activate
   ```
2. Instalar las dependencias
   ```
   pip install -r requirements.txt
   ```
## Para correr el servidor
```
uvicorn main:app --reload
```

## Para ejecutar los tests
```
pytest
```

## Para inicializar el docker 

```
docker compose build
```
```
docker compose up
```
