#!/usr/bin/env bash
# Inicia o servidor
gunicorn core.wsgi:application
