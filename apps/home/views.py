from django.views.generic import TemplateView


class HomeIndexView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reception"
        context["hero_title"] = "Django starter"
        context["hero_slogan"] = "Start all projects with ease"
        context["connect"] = "Connect"
        return context
