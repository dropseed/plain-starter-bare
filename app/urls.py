from plain.urls import path, Router
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


class AppRouter(Router):
    namespace = ""
    urls = [
        path("json/", ExampleJsonView),
        path("", ExampleTemplateView),
    ]
