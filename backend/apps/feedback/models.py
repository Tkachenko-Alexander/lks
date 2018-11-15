from django.db import models
from django.utils.translation import ugettext_lazy as _


class Feedback(models.Model):
    """ Feedback model """
    name = models.CharField(_('Name'), max_length=120)
    email = models.EmailField(_('Email'))
    feedback = models.TextField(_('Feedback'))

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self):
        return self.feedback[:25]