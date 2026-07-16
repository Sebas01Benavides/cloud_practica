Informe de práctica: Docker Compose con Django, Vue, PostgreSQL, Redis, Celery, Flower, Grafana y Loki

Resumen

La práctica quedó montada con backend en Django, frontend en Vue, base de datos PostgreSQL, caché y broker Redis, tareas asíncronas con Celery, monitoreo con Flower y observabilidad con Grafana + Loki. Las capturas muestran el flujo completo: creación del proyecto, build de Docker Compose, migraciones, subida de contenedores y validación de URLs.

Preparación del proyecto

Se instaló Docker Desktop, se organizaron las carpetas del proyecto y se inicializó Django dentro de un contenedor Python 3.11 para generar el proyecto backend y la app app. También se configuró docker-compose.yml en la raíz del proyecto para orquestar todos los servicios requeridos por la práctica.

Construcción y arranque

Primero se ejecutó docker compose build para construir las imágenes. Después se levantaron PostgreSQL y Redis con docker compose up -d postgres redis, se verificó el estado con docker compose ps, se ejecutó la migración con docker compose run django python manage.py migrate y finalmente se levantó todo el stack con docker compose up.

Validación del backend

Django respondió correctamente en http://localhost:8000/api/hello/, lo que confirma que las rutas backend.urls y app.urls quedaron bien conectadas. También se probó http://localhost:8000/api/cache/ para validar la caché con Redis desde Django.

Validación del frontend

Vue quedó accesible desde http://localhost:8081 porque el puerto 8080 estaba ocupado por XAMPP. La estructura correcta del frontend fue importante: index.html en la carpeta principal de frontend y src/ dentro de frontend/, no fuera de ella.

Monitoreo y observabilidad

Flower quedó disponible en http://localhost:5555 para monitorear Celery. Grafana quedó disponible en http://localhost:3000; al iniciar sesión, pidió cambio de contraseña por defecto y luego se conectó Loki como data source con la URL http://loki:3100.

Logs y verificación final

Se documentaron también las capturas de docker compose logs -f y de Docker Desktop mostrando los contenedores activos. Las capturas finales confirman que el entorno quedó funcionando y que los servicios se integran como una nube privada de desarrollo para backend, frontend, mensajería, monitoreo y logging.

Conclusión

La práctica cumplió con el objetivo, que era levantar un entorno funcional con Django, Vue, PostgreSQL, Redis, Celery, Flower, Grafana y Loki, todo administrado con Docker Compose. Las capturas  respaldan las etapas del proceso y permiten demostrar la configuración realizada.