from django.db import models
from contract.models import Status


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    event_date = models.DateField(editable=True, null=True)
    attendees = models.IntegerField(editable=True, null=True)
    note = models.TextField(max_length=250, blank=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=True)
    event_status = models.ForeignKey('contract.Status', to_field='status', on_delete=models.CASCADE, null=True,
                                     default=Status.ACTIVE)

    support_contact = models.ForeignKey(to='user.CustomUser', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.client} ({self.event_date})'
