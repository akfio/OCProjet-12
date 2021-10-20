from django.db import models


class Status(models.Model):
    id = models.AutoField(primary_key=True)

    ACTIVE = 'Active'
    TERMINATE = 'Terminate'
    STATUS_CHOICE = {
        (ACTIVE, 'Active'),
        (TERMINATE, 'Terminate')
    }
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Active', unique=True)

    def __str__(self):
        return self.status


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    amount = models.FloatField(editable=True, null=True)
    payment_due = models.DateField(editable=True, blank=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(to='Status', to_field='status', on_delete=models.CASCADE, null=True,
                               default=Status.ACTIVE)
    sales_contact = models.ForeignKey(to='user.CustomUser', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.status)
