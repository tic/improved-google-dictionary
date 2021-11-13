from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question, User, Authenticator
from .forms import CreateUserForm
from mysite import settings
from datetime import datetime
import random
import hmac
import os

def paper_s(request):
    return render(request,'experiment/paper_s.html')


def welcome(request):
    # if user is already authenticated redirect to sample paper page
    if request.COOKIES.get('auth'):
        return HttpResponseRedirect(reverse('experiment:consent_form'))

    if request.method == 'POST':
        # validate form
        form = CreateUserForm(request.POST)

        # if form is valid
        if form.is_valid():
            authenticator = None

            # sanitize participant id
            particpant_id = form.cleaned_data['participant_id']

            # attempt to create new user in db
            try:
                User.objects.create(user_email=particpant_id, user_exten1=random.randint(0,1), user_t1 = datetime.now()).save()
                user = User.objects.get(user_email=particpant_id)

                # generate new authenticator
                authenticator = hmac.new(
                    key = settings.SECRET_KEY.encode('utf-8'),
                    msg = os.urandom(32),
                    digestmod = 'sha256',
                ).hexdigest()

                # create a new authenticator for the new user
                Authenticator.objects.create(user_id=user, authenticator=authenticator).save()
            except Exception as e:
                if 'authenticator' in str(e):
                    form.add_error(field=None, error="Internal error. Try again.")
                else:
                    form.add_error(field=None, error='Particpant ID: ' + str(particpant_id) + ' already exists.')
                return render(request, 'experiment/welcome.html', {'form': form})

            # if succussful, set auth cookie w/ 2 hour ttl
            response = HttpResponseRedirect(reverse('experiment:consent_form'))
            response.set_cookie('auth', authenticator, max_age=3600)
            return response
        else:
            return render(request, 'experiment/welcome.html', {'form': form})

    return render(request, 'experiment/welcome.html', {'form': CreateUserForm()})

def consent_form(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    context = {
        'participant_id' : authenticator.user_id.user_email
    }

    return render(request,'experiment/consent_form.html', context)

def demographics_survey(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    context = {
        'participant_id' : authenticator.user_id.user_email
    }

    return render(request, 'experiment/surveys/demographics_survey.html', context)

def paper_sample(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    context = {
        'participant_id' : authenticator.user_id.user_email
    }

    return render(request, 'experiment/paper_sample.html', context)

def quiz_sample(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    context = {
        'participant_id' : authenticator.user_id.user_email
    }

    return render(request,'experiment/quizzes/quiz_sample.html', context)

def switch_extensions(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))


    authenticator = Authenticator.objects.get(authenticator=auth)
    user = authenticator.user_id


    context = {
        'participant_id' : user.user_email
    }

    context['paper_1'] = False if user.user_t2 else True

    if not user.user_exten1 and user.user_t2 or user.user_exten1 and not user.user_t2:
        return render(request,'experiment/holder_exten_0.html', context)
    else:
        return render(request,'experiment/holder_exten_1.html', context)


def paper_1(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    user = authenticator.user_id
    user.user_t1 = datetime.now()
    user.save()

    context = {
        'participant_id' : user.user_email
    }

    return render(request,'experiment/paper_1.html',context)

def paper_2(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    user = authenticator.user_id
    user.user_t3 = datetime.now()
    user.save()

    context = {
        'participant_id' : user.user_email
    }

    return render(request,'experiment/paper_2.html',context)

def quiz_s(request):
    return render(request,'experiment/quiz_s.html')

def quiz_1(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    user = authenticator.user_id
    user.user_t2 = datetime.now()
    user.save()

    context = {
        'participant_id' : user.user_email
    }

    return render(request,'experiment/quizzes/quiz_1.html', context)

def quiz_2(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    user = authenticator.user_id
    user.user_t4 = datetime.now()
    user.save()

    context = {
        'participant_id' : user.user_email
    }

    return render(request,'experiment/quizzes/quiz_2.html', context)

def exit_survey(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    user = authenticator.user_id
    user.user_t5 = datetime.now()
    user.save()

    context = {
        'participant_id' : user.user_email
    }

    return render(request, 'experiment/surveys/exit_survey.html', context)

def finish(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    authenticator = Authenticator.objects.get(authenticator=auth)
    context = {
        'participant_id' : authenticator.user_id.user_email
    }

    return render(request, 'experiment/finish.html', context)

def logout(request):
    # try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # if the authenticator cookie wasn't set...
    if not auth:
        # send user to welcome page
        return HttpResponseRedirect(reverse('experiment:welcome'))

    # remove user's authenticator
    Authenticator.objects.get(authenticator=auth).delete()

    # remove 'auth' cookie and send to welcome page
    response = HttpResponseRedirect(reverse('experiment:welcome'))
    response.delete_cookie('auth')
    return response



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

    page_order = ['', 'experiment:paper_1', 'experiment:quiz_1', 'experiment:paper_2', 'experiment:quiz_2', 'experiment:exit_survey']
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
