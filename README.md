# PowerMeter service

## Enviroment variables

* `DEBUG`: `True` or `False`
* `ALLOWED_HOSTS`: for local development this should be `localhost,127.0.0.1,*`
* `SECRET_KEY`: Something that persists

## Development

First copy `.env_template` to `.env` and modify it to match all the
needed configuration. You should ask for an example `.env` to a buddy
to setup this.

Afterwards just run the following command:

```sh
docker-compose up api
```

This will ensure to pull all dependencies and build the project in development mode.

### Running commands inside the container

If you use the `docker-compose` command, use `docker-compose run api <command>` to replace
the command that you need to run. For example, you'll need to run
`docker-compose run api ./manage.py makemigrations` in replace of `./manage makemigrations`.

## Api documentation

The api documentation is specified with the [OpenAPI specification](https://swagger.io/specification/).
The documentation is in http://localhost:8000/doc

