from plain.urls import path
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


urlpatterns = [
    path("json/", ExampleJsonView),
    path("text/", ExamplePlaintextView),
    path("", ExampleTemplateView),
]
