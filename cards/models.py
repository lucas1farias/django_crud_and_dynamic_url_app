

from django.db import models
from django.utils.text import slugify
from datetime import datetime
from uuid import uuid4


def mock_name(instance, filename):
    extension = [*str(filename).split('.')]
    print(extension)
    print(extension[0])
    return datetime.now().strftime('%Y-%m-%d-%H-%M-') + f'{extension[0]}-{uuid4()}.{extension[1]}'


class Base(models.Model):
    created = models.DateTimeField('Date of creation', auto_now_add=True)
    updated = models.DateTimeField('Last update', auto_now=True)

    class Meta:
        abstract = True


class PoEDivinationCard(Base):
    # Campos que serão criados pelo desenvolvedor/usuário
    name = models.CharField('Name of the card', help_text='characters limit = 50', max_length=50)
    description = models.TextField('Description of the card', help_text='characters limit = 200', max_length=200)
    stack_size = models.IntegerField('Amount of cards required', help_text='insert an integer number only')
    image = models.ImageField('Image of the divination card', blank=True, null=True, upload_to=mock_name)

    # Campo que receberá um valor dinamicamente via "save" através do que é passado em "self.name"
    slug = models.SlugField('Dynamic url', help_text='no need to fill it', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PoE card'
        verbose_name_plural = 'PoE cards'

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
