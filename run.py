from wsgiref.simple_server import make_server

from ns_framework.main import BaseFramework
from urls import routes, fronts

framework = BaseFramework(routes, fronts)

if __name__ == "__main__":
    with make_server('', 8000, framework) as httpserver:
        print("Запуск сервера, порт 8000")
        httpserver.serve_forever()
