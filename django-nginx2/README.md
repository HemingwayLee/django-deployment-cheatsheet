# Run django with nginx
* A public-facing nginx server (listening to port 80) routes requests to django application (listening to port 8000)
  * `upstream` is used in `default`

# How to run
```
docker build -t my-udn .
docker run -it -p 80:80 --rm my-udn
```
