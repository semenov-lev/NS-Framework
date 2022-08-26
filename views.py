from ns_framework.template_engine import render


class Index:
    def __call__(self, request):
        return "200 OK", render("index.html", date=request["date"], title="Дед, пей таблетки!", path=request["path"])


class Contacts:
    def __call__(self, request):
        return "200 OK", render("contacts.html", title="Где внучок?", path=request["path"])


class NotFoundPage:
    def __call__(self, request):
        return "404 Not Found", render("404.html")
