from django.db import models
from . import constants


class AbstractModel(models.Model):
    """
        Abstract model to add common fields to all models.
    """
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
    """
        To allow a ticket to be entered as quickly as possible, only the
        bare minimum fields are required. These basically allow us to
        sort and manage the ticket. The user can always go back and
        enter more information later.

        Note that except summary all fields are optional
        from dashboard we can prompt users to add extra details.
    """
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
