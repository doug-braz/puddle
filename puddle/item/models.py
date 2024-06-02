from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Categories' # Changes the plural name in the Admin page

    def __str__(self):
        return self.name # For correct exhibiting each category name in the Admin page