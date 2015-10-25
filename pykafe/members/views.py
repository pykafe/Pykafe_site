from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'members/index.html'
