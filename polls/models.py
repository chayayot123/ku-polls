"""Check and return the question of the polls."""

import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Object of the class question."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date time ended', null=True)

    def __str__(self):
        """Return the question text."""
        return self.question_text

    def was_published_recently(self):
        """Question is published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Question is published or not."""
        now = timezone.now()
        return self.pub_date <= now

    def can_vote(self):
        """Question could vote or not."""
        now = timezone.now()
        return self.pub_date <= now <= self.end_date

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):
    """Class for the choice of the question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return the choice text."""
        return self.choice_text


class Vote(models.Model):
    """Vote model in each poll question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=0)

    def __str__(self):
        """Return the representation of vote.
        Returns:
            str: question text
        """
        return f"{self.question} has been voted with {self.choice}"
