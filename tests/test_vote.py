"""Test for vote in django polls."""
import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class IsPublishedTests(TestCase):
    """Class to check question is published or not."""

    def test_is_published(self):
        """The question is published or not."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        question = Question(pub_date=time)
        self.assertIs(question.is_published(), True)


class CanVoteTests(TestCase):
    """Class to check question can vote or not."""

    def test_can_vote(self):
        """The question can vote or not."""
        time = timezone.now() - datetime.timedelta(days=1)
        end_time = timezone.now() + datetime.timedelta(days=1)
        question = Question(pub_date=time, end_date=end_time)
        self.assertIs(question.can_vote(), True)