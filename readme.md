# django (production) deployment cheatsheet

* Django comes with a lightweight web server. Do not use it in production environment [ref](https://stackoverflow.com/questions/4867793/using-djangos-built-in-web-server-in-a-production-environment
)
  * Security reasons
  * It is single thread

# Other tips
## Don't put virtualenv directory into git repo, [ref](https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository)
* Use `requirements.txt`

## Don't commit `migrations` folder to git
* it will create conflicts
* just run `python manage.py makemigrations` and `python manage.py migrate` on the server

