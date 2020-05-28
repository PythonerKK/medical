from django import forms

from medical.queueup.models import Queue


class QueueForm(forms.ModelForm):

    class Meta:
        model = Queue
        exclude = ('user', )
