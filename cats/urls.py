from django.conf.urls import url
from cats.views import HomeView, ThanksView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^thanks/', ThanksView.as_view(), name='thanks'),
]
