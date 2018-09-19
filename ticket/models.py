from django.db import models
from . import constants


class AbstractModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Tag(AbstractModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class User(AbstractModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ticket(AbstractModel):
    summary = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=2,
        choices=constants.PRIORITY_CHOICES,
        default=constants.NORMAL)
    tag = models.ForeignKey(Tag, blank=True,
        null=True, on_delete=models.SET_NULL)
    assignee = models.ForeignKey(User, blank=True,
        null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} - {}".format(self.id, self.summary)

    class Meta:
        ordering = ["-created"]
