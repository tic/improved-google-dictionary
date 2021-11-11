from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'experiment'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home', views.IndexView.as_view(), name='home'),
    path('welcome', views.welcome, name='welcome'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('consent_form', views.consent_form, name='consent_form'),
    path('demographics_survey', views.demographics_survey, name='demographics_survey'),
    path('paper_sample', views.paper_sample, name='paper_sample'),
    path('quiz_sample', views.quiz_sample, name='quiz_sample'),
    path('paper_1', views.paper_1, name='paper_1'),
    path('quiz_1', views.quiz_1, name='quiz_1'),
    path('paper_2', views.paper_2, name='paper_2'),
    path('quiz_2', views.quiz_2, name='quiz_2'),
    path('exit_survey', views.exit_survey, name='exit_survey'),
    path('finish', views.finish, name='finish'),
    path('logout', views.logout, name='logout'),
    path('<int:t>set_time', views.set_time, name='set_time'),
]
