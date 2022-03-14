# Run django application with docker
* It use django default web server which is not supposed to be used in a production
  * This web server uses the WSGI application object specified by the WSGI_APPLICATION setting

# How to run
```
docker build -t my-django .
docker run -it -p 8000:8000 --rm my-django
```

## We can also run django project using tmux
```
tmux new-session -d -s "myDjangoSession" "python3 manage.py runserver 0.0.0.0:8000"
```
