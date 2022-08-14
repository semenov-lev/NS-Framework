Способы запуска Not a Serious Framework:

1. Через run.py, используя модуль wsgiref.simple_server (по умолчанию используется порт 8000):
    python3 run.py
    или
    python run.py

2. Через gunicorn:
    gunicorn run:framework
    или
    gunicorn -b 127.0.0.1:8000 run:framework
