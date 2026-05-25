from plain.http import JsonResponse
from plain.templates.views import TemplateView
from plain.urls import path, Router
from plain.views import View


class ExampleTemplateView(TemplateView):
    template_name = "example.html"

    def get_template_context(self):
        context = super().get_template_context()
        context["message"] = "Hello World!"
        return context


class ExampleJsonView(View):
    def get(self):
        return JsonResponse({"message": "Hello World!"})


class AppRouter(Router):
    namespace = ""
    urls = [
        path("json", ExampleJsonView),
        path("", ExampleTemplateView),
    ]
