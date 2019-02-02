# Tips

## Django comes with a lightweight web server. Do not use it in production environment

* Security reasons
* It is single thread

https://stackoverflow.com/questions/4867793/using-djangos-built-in-web-server-in-a-production-environment


## Don't put virtualenv directory into git repo
* Use `requirements.txt`

https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository


## Don't commit `migrations` folder to git
* it will create conflicts
* just run `python manage.py makemigrations` and `python manage.py migrate` on the server