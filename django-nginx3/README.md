# What

Nginx doesn't support using environment variables inside most configuration blocks.

But `envsubst` can be used as a workaround if you need to generate your nginx configuration dynamically before nginx starts.

# How 
```
docker build -t my-udn .
docker run -it -p 80:80 --rm my-udn
```
