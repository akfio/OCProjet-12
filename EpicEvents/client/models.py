from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    sales_contact = models.ForeignKey(to='user.CustomUser', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company