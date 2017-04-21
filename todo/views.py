from django.views.generic import TemplateView


class Home(TemplateView):
    # the view template
    template_name = 'index.html'
