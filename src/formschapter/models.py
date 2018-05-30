from django.db import models
from django.urls import reverse


class ImportantDate(models.Model):
    date = models.DateField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.date, self.desc)

    def get_absolute_url(self):
        return reverse('formschapter:impdate_detail', args=[str(self.pk)])

    class Meta:
        ordering = ('-date',)
