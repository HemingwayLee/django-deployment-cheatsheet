# What is `uWSGI`
* It is a fast, self-healing and developer/sysadmin-friendly application container server coded in pure C
* It can be installed by `pip`
* It runs on the foreground
* It can be run with/without Django

## Without Django

Use the following command to run the server
```
uwsgi --http :8000 --wsgi-file test.py
```

## With Django
```
uwsgi --http :8000 --module mysite.wsgi
```

## With nginx
```
uwsgi --socket :8001 --module mysite.wsgi
```

