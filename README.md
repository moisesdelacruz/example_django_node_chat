# Photopublishings
### It's a application for publishings photos more a description.
### Builded in Django and Nodejs.
### It has Unit Tests on Django.

## Install Node server
```sh
git clone https://github.com/moisesdelacruz/photopublishings_node.git

cd photopublishings_node/

docker build -t moisesdelacruz/photopublishings .
```

## Install Django server
```sh
  git clone https://github.com/moisesdelacruz/photopublishings.git

  cd photopublishings/

  touch .env
```
* `.env` file content
```sh
SECRET_KEY=-c77ykal!%=0nbr#8po380!j@0)sonvk_)7)ajtog84bmwwb!p

# Data Base Postgres
POSTGRES_DB=photo
POSTGRES_USER=photo_user
POSTGRES_PASSWORD=photo_password
```
* build project
```sh
docker-compose build
```
* Run project
```sh
$ docker-compose up
# migrate
$ docker-compose run web python manage.py migrate
# create superuser
$ docker-compose run web python manage.py createsuperuser
```

## Extra commands
```sh
$ docker-compose run web python manage.py makemigrations

$ docker-compose run web python manage.py migrate

$ docker-compose run web python manage.py shell

$ docker-compose run web python manage.py createsuperuser
```
