from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question, User

def consent_form(request):
    return render(request,'experiment/consent_form.html')

def paper_s(request):
    return render(request,'experiment/paper_s.html')

class PaperView(generic.TemplateView):
    model = User
    template_name = 'experiment/paper_1.html'

    def get_current_user(self):
        """
        Return the last published user
        """
        return User.objects.filter(
            user_t1__lte=timezone.now()
        ).order_by('-pub_date')[:1]

def paper_2(request):
    return render(request,'experiment/paper_2.html')

def quiz_s(request):
    return render(request,'experiment/quiz_s.html')

def quiz_1(request):
    return render(request,'experiment/quiz_1.html')

def quiz_2(request):
    return render(request,'experiment/quiz_2.html')

def ux_form(request):
    return render(request,'experiment/ux.html')

def thanks(request):
    return render(request,'experiment/thanks.html')



class IndexView(generic.ListView):
    template_name = 'experiment/old_stuff/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'experiment/old_stuff/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'experiment/old_stuff/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'experiment/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('experiment:results', args=(question.id,)))


def set_time(request, t):
    time = timezone.now()
    u  = User.objects.filter(user_t1__lte=timezone.now()).order_by('user_t1')[0]

    page_order = ['', 'experiment:paper_1', 'experiment:quiz_1', 'experiment:paper_2', 'experiment:quiz_2', 'experiment:ux']
    if t == 1:
        u.user_t1 = time

    elif t == 2:
        u.user_t2 = time

    elif t == 3:
        u.user_t3 = time

    elif t == 4:
        u.user_t4 = time

    elif t == 5:
        u.user_t5 = time

    u.save()
    return HttpResponseRedirect(reverse(page_order[t], args=()))
