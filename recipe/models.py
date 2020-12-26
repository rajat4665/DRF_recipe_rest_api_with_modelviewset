import os, uuid
from django.db import models
# Create your models here.

class BaseCreateUpdateTimeStampModel(models.Model):
    """ base class for time stamp on creation and updation"""
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class Tag(BaseCreateUpdateTimeStampModel, models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient(BaseCreateUpdateTimeStampModel, models.Model):
    """Ingredient to be used in a recipe"""
    name = models.CharField(max_length=255)
    grams = models.IntegerField()

    def __str__(self):
        return self.name + ' ' +str(self.grams) + 'grams'


class Recipe(BaseCreateUpdateTimeStampModel, models.Model):
    """Main Recipe table """
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title
