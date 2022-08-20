from views import NotFoundPage
import urllib.parse


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

        # Проверка на слэш в конце адреса
        if not path.endswith("/"):
            path += "/"

        # Список IP с запросами
        if client_ip not in self.clients:
            self.clients.append(client_ip)
            print(f"Новый клиент: {client_ip}")

        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFoundPage()

        for front in self.fronts:
            front(request)

        # Получение параметров запроса
        input_data = self.get_input_data(environ)
        request["request_params"] = input_data
        print(f"Input data: {input_data}")

        code, body = view(request)

        start_response(code, [("Content-Type", "text/html")])
        return body

    @staticmethod
    def get_input_data(env) -> dict:
        """
        Функция получает словарь данных от сервера,
        возвращает декодированный словарь с параметрами запроса
        :param env:
        :return:
        """
        result = {}
        request_method = env["REQUEST_METHOD"]
        print(f"Request method: {request_method}")

        if request_method == "GET":
            result = urllib.parse.parse_qs(env.get("QUERY_STRING", ""))

        elif request_method == "POST":
            content_length = int(env.get("CONTENT_LENGTH", 0))
            if content_length:
                raw_data = env["wsgi.input"].read(content_length)
                decoded_data = raw_data.decode(encoding="utf-8")
                result = urllib.parse.parse_qs(decoded_data)

        return result
