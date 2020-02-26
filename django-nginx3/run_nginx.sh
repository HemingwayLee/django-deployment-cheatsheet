#!/usr/bin/env bash
export DOLLAR='$'
envsubst < /home/nginx.conf.template > /etc/nginx/sites-enabled/default
