from views import Index
from datetime import date


def data_front(request):
    request["date"] = date.today()


fronts = [data_front]

routes = {
    "/": Index()
}
