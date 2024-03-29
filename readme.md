# django (production) deployment cheatsheet

* Django comes with a lightweight web server (e.g., in [this](https://github.com/HemingwayLee/django-deployment-cheatsheet/tree/master/dummy-django-project) example). Do not use it in production environment, [ref](https://stackoverflow.com/questions/4867793/using-djangos-built-in-web-server-in-a-production-environment
)
  * Security reasons
  * It is single thread

## Solution
* Setting up Django with uWSGI and nginx

# Other tips
## Don't put virtualenv directory into git repo, [ref](https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository)
* Use `requirements.txt`

## Commit `migrations` folder to git
* it will create conflicts
* just run `python manage.py makemigrations` and `python manage.py migrate` on the server

