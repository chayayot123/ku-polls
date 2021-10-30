"""Django test for detail view."""
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from polls.models import Question


def create_question(question_text, days):
    """
    Create a question with the given `question_text`.

    Published the given number of `days` offset to now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionDetailViewTests(TestCase):
    """Class of the detial view check that can vote properly in time."""

    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future.

        Returns a 302 not found.
        """
        future_question = create_question(question_text='Future question.',
                                          days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)