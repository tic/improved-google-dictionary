from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'experiment'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('consent_form', views.consent_form, name='consent_form'),
    path('paper_1', views.PaperView.as_view(), name='paper_1'),
    path('quiz_1', views.quiz_1, name='quiz_1'),
    path('paper_2', views.paper_2, name='paper_2'),
    path('quiz_2', views.quiz_2, name='quiz_2'),
    path('<int:t>set_time', views.set_time, name='set_time'),
]
