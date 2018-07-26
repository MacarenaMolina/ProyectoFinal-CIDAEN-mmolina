# ProyectoFinal-CIDAEN-mmolina
En este repositorio se encuentra el proyecto final realizado por Macarena Molina Gallardo para el Curso de Especialista CIDAEN de la UCLM.

El proyecto consiste en la realización de una aplicación interactiva que obtiene los datos a partir de un bucket de S3 en Amazon Web Services y su posterior despliegue con Docker.

Para poder levantar la aplicación es necesario seguir los siguientes pasos en la terminal de Docker:
- Crear un bucket de S3 donde donde almacenaremos unos datos de prueba. Esto se puede realizar escribiendo en la terminal lo siguiente:
```ssh
aws s3 mb mybucket
aws cp datos.csv s3://mybucket/
```
donde mybucket es el nombre que queremos que tenga el bucket de S3 que vamos a crear.

- Crear un rol de IAM con permisos de acceso de lectura al bucket de S3 que hemos creado para poder ejecutar la aplicación.

- Crear la imagen Docker a partir de la Dockerfile. Para ello hacemos:
```ssh
docker build -t python-app-cidaen-mmolina .
```

- Finalmente ya podemos levantar la aplicación ejecutando lo siguiente:
```ssh
docker run --rm -p 8050:8050 -e BUCKET_NAME=mybucket -e AWS_ACCESS_KEY=clave-acceso -e AWS_SECRET_ACCESS_KEY=clave-secreta python-app-cidaen-mmolina
```
donde mybucket es el nombre del bucket que hemos creado antes y clave-acceso y clave-secreta son los credenciales del rol que hemos obtenido anteriormente.
