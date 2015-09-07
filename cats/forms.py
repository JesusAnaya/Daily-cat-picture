from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    name = forms.CharField(label='Full name (optional)', required=False)

    class Meta:
        model = Subscriber
        exclude = ('id',)
