# What is `uWSGI`
* It is a fast, self-healing and developer/sysadmin-friendly application container server coded in pure C
* It can be installed by `pip`
* It runs on the foreground
* It can be run with/without Django

# How to use

```
docker build -t my-ud .
docker run -it -p 8000:8000 --rm my-ud
```

# Details

Use the following command to run the server
```
uwsgi --http :8000 --wsgi-file test.py
```

