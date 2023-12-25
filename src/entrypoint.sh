#!/bin/sh

UID="${FLASK_UID:-0}"
GID="${FLASK_GID:-0}"
PORT="${GUNICORN_PORT:-0}"

usermod -u $UID app
groupmod -g $GID app

gunicorn application.app:app --bind 0.0.0.0:$PORT