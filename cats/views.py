from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse
from .forms import SubscriberForm


class HomeView(CreateView):
    template_name = 'index.html'
    form_class = SubscriberForm

    def get_success_url(self):
        return reverse('thanks')


class ThanksView(TemplateView):
    template_name = 'thanks.html'
