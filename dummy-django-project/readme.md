# How to use
```
docker build -t my-django .
docker run -it -p 8000:8000 --rm my-django
```

# Run django project using tmux
```
tmux new-session -d -s "myDjangoSession" "python3 manage.py runserver 0.0.0.0:8000"
```