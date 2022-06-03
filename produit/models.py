from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_location(instance, filename):
    file_path = 'produits/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)
    return file_path


class Product(models.Model):
    Nom_Produit = models.CharField(max_length=50)
    Prix = models.IntegerField(default=0)
    Quantite = models.IntegerField()
    Image = models.ImageField(upload_to='', blank=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom_Produit


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.Image.delete(False)
