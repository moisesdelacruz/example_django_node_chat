# Example: comments real time with django and nodejs.

## Install
```sh
  git clone https://github.com/moisesdelacruz/example_django_node_chat.git

  cd example_django_node_chat/

  pip install -r requirements.txt

  npm install

```

## Config entorno variables
```sh
  export PHOTOPUBLISHINGS_SECRET_KEY="ze@h+z8ixafva*et%q7e6=gf2cy58&i4(e+%ewj*#ikvra6czp"
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

  python manage.py createsuperuser

  python manage.py runserver

  npm start

  npm run server
```
