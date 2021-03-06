"""Views file of the polls."""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Choice, Question, Vote
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_client_ip(request):
    """Get the visitor’s IP address using request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class IndexView(generic.ListView):
    """Index view page class."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).\
            order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Detial view page class."""

    model = Question
    template_name = 'polls/detail.html'

    def get(self, request, **kwargs):
        """Error hanling from the polls."""
        try:
            question = get_object_or_404(Question, pk=kwargs['pk'])
            if not question.can_vote():
                return HttpResponseRedirect(reverse('polls:index'),
                                            messages.error(request, "\
                                                Poll is out of date"))

        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('polls:index'),
                                        messages.error(request, "\
                                            Poll does not exist."))
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data
                                       (object=self.get_object()))

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """Class that show the result of the vote."""

    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    """Do this function used to vote from the polls."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        user = request.user
        vote = get_vote_for_user(question, user)
        if not vote:
            vote = selected_choice.vote_set.create(user=user, question=question)
        else:
            vote.choice = selected_choice
        vote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))


def get_vote_for_user(question, user):
    """Return vote of the user from the question."""
    try:
        votes = Vote.objects.filter(user=user).filter(choice__question=question)
        if votes.count() == 0:
            return None
        else:
            return votes[0]
    except Vote.DoesNotExist:
        return None
