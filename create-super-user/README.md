## How to use
```
docker build -t my-django .
docker run -it -p 8000:8000 --rm my-django
```

## We can also run django project using tmux
```
tmux new-session -d -s "myDjangoSession" "python3 manage.py runserver 0.0.0.0:8000"
```



## Ref
https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django

