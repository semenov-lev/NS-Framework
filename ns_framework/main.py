from views import NotFoundPage


class BaseFramework:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts
        self.clients = []

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """
        request = {}

        path = environ["PATH_INFO"]
        client_ip = environ["REMOTE_ADDR"]

        if not path.endswith("/"):
            path += "/"

        if client_ip not in self.clients:
            self.clients.append(client_ip)
            print(f"Запросов с уникальных IP: {len(self.clients)}")

        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFoundPage()

        for front in self.fronts:
            front(request)

        code, body = view(request)

        start_response(code, [("Content-Type", "text/html")])
        return body
