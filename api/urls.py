from django.urls import path

from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Oldtimers API')

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('documentation/', schema_view),
    path('event-list/', views.event_list, name="event-list"),
    path('event-detail/<str:pk>/', views.event_detail, name="event-detail"),
    path('crew-list/', views.crew_list, name="crew-list"),
    path('crew-detail/<str:pk>/', views.crew_detail, name="crew-detail"),
    path('organizer-list/', views.organizer_list, name="organizer-list"),
    path('organizer-detail/<str:pk>/', views.organizer_detail, name="organizer-detail"),
    path('competition-list/', views.competition_list, name="competition-list"),
    path('competition-detail/<str:pk>/', views.competition_detail, name="competition-detail"),
    path('score-list/', views.score_list, name="score-list"),
    path('score-detail/<str:pk>/', views.score_detail, name="score-detail"),
    path('score-create/', views.score_create, name="score-create"),
    path('crew-scores/<str:pk>/', views.crew_scores, name="crew-scores"),
    path('crew-photo/<str:pk>/', views.crew_photo, name="crew-photo"),
    path('photo-upload/<str:pk>/', views.photo_upload, name="photo-upload"),
]
