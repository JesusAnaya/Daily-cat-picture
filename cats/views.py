from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from .forms import SubscriberForm
from .models import Subscriber


class HomeView(FormView):
    template_name = 'index.html'
    form_class = SubscriberForm

    def get_success_url(self):
        return reverse('thanks')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if not Subscriber.objects.filter(email=email).exists():
            form.save()
        return super(HomeView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'
