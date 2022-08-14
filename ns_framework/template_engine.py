import os

from jinja2 import Environment, FileSystemLoader

from ns_framework.settings import PROJECT_PATH

env = Environment(loader=FileSystemLoader(os.path.join(PROJECT_PATH, "templates")))


def render(template_name, **kwargs):
    template = env.get_template(template_name)
    return [bytes(template.render(**kwargs), "utf-8")]
