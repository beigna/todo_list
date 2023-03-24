# TODO List
Es un pequeño proyecto para administrar tareas. Está implementado con Django e Intercooler.js

---
## Puesta en funcionamiento
Tras clonar el repositorio hay una serie de comandos a ejecutar para su funcionamiento (con django runserver).

- `$ make docker-build-dev` crea la imagen de Docker
- `$ make docker-build-db` corre las migraciones de la DB e instala fixtures
- `$ make docker-start` inicia el contenedor y expone el servicio

Para navegar el sitio hay que ingresar en http://localhost:8000/tasks/
Los usuarios por defecto son `admin:admin`, `adrian:adrian` e `ignacio:ignacio`

Para correr los test hay que ejecutar:
- `$ make docker-test`

## Detalles constructivos
Se optó por utilizar un services y selectors para acceder al modelo Task. Esto centraliza la lógica de creación/edición y acceso, evitando replicar funcionalidad en las views, management commands, signals, etc etc.

Para loggear los cambios del modelo Task usaría https://django-simple-history.readthedocs.io/ pero por cuestiones de tiempo utilicé logging dentro del service de Task.
Otra opción es utilizar las signasl de django escuchando a dicho modelo y loggeando en consecuencia.

Por otro lado no se utilizan ModelForms por falta de tiempo y porque el modelo es muy simple.

Para los tests no usé FactoryBoy ni Faker por cuestiones de tiempo.
