from plain.urls import path, RouterBase, register_router
from plain.views import TemplateView, View


class ExampleTemplateView(TemplateView):
    template_name = "example.html"

    def get_template_context(self):
        context = super().get_template_context()
        context["message"] = "Hello World!"
        return context


class ExampleJsonView(View):
    def get(self):
        return {"message": "Hello World!"}


class ExamplePlaintextView(View):
    def get(self):
        return "Hello World!"


@register_router
class Router(RouterBase):
    urls = [
        path("json/", ExampleJsonView),
        path("text/", ExamplePlaintextView),
        path("", ExampleTemplateView),
    ]
