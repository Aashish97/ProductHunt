from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    publish_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:200]

    def publish_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')