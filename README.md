# Photopublishings
### It's a application for publishings photos more a description.
### Builded in Django and Nodejs.
### It has Unit Tests on Django.

## Install
```sh
  git clone https://github.com/moisesdelacruz/photopublishings.git

  cd example_django_node_chat/

  pip install -r requirements.txt

  npm install

```

## Config entorno variables
```sh
  export PHOTOPUBLISHINGS_SECRET_KEY="-c77ykal!%=0nbr#8po380!j@0)sonvk_)7)ajtog84bmwwb!p"
  export PHOTOPUBLISHINGS_DB_NAME="<name databases>"
  export PHOTOPUBLISHINGS_DB_USER="<username of postgres>"
  export PHOTOPUBLISHINGS_DB_PASSWORD="<possword of postgres user>"
  export PHOTOPUBLISHINGS_DB_HOST="localhost"
```

## Additional
- Install and run redis server

## Run servers
```sh
  python manage.py migrate

  python manage.py test

  python manage.py createsuperuser

  python manage.py runserver

  npm start

  npm run server
```
