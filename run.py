from wsgiref.simple_server import make_server
import webbrowser


from ns_framework.main import BaseFramework
from urls import routes, fronts

framework = BaseFramework(routes, fronts)

ADDR = "127.0.0.1"
PORT = 8000

if __name__ == "__main__":
    with make_server(ADDR, PORT, framework) as httpserver:
        print(f"Запуск сервера на {ADDR}:{PORT}")
        webbrowser.open(f"http://{ADDR}:{PORT}/")
        httpserver.serve_forever()
