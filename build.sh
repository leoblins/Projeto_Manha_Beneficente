#!/usr/bin/env bash
# Instala os pacotes
pip install -r requirements.txt
# Executa as migrações e coleta os arquivos estáticos automaticamente
python manage.py migrate
python manage.py collectstatic --noinput
