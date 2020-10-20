
from django.conf import settings
from django.db import models




User = settings.AUTH_USER_MODEL
# Create your models here.
class Product(models.Model):
    # id = models.AutoField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  #  image = models.ImageField(upload_to='products/', null=True, blank=True)
  #  video_link = models.TextField(blank=True, null=True)
   # media = models.FileField(storage=ProtectedStorage, upload_to='products/', null=True, blank=True)
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # 9.99
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def has_inventory(self):
        return self.inventory > 0 # True or False
