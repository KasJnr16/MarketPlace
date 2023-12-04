from django.db import models
from django.contrib.auth.models import(
    User,

)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    # making the name plural
    # basically config for model
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6 ,decimal_places=2)
    image = models.ImageField(upload_to="item_images", blank=True, null=True) #install Pillow to handle pics
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
