import base64

from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.base import ContentFile

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event
from .serializers import *


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/model-list/',
        'Detail View': '/model-detail/<str:pk>/',
        'Create (Score only)': '/score-create/',
        'Photo Upload': '/photo-upload/',
        'Crew Scores': '/crew-scores/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def crew_list(request):
    crews = Crew.objects.all()
    serializer = CrewSerializer(crews, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def crew_detail(request, pk):
    crew = Crew.objects.get(id=pk)
    serializer = CrewSerializer(crew, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def organizer_list(request):
    organizers = Organizer.objects.all()
    serializer = OrganizerSerializer(organizers, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def organizer_detail(request, pk):
    organizer = Organizer.objects.get(id=pk)
    serializer = OrganizerSerializer(organizer, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def competition_list(request):
    competitions = Competition.objects.all()
    serializer = CompetitionSerializer(competitions, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def competition_detail(request, pk):
    competition = Competition.objects.get(id=pk)
    serializer = CompetitionSerializer(competition, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def score_list(request):
    scores = Score.objects.all()
    serializer = ScoreSerializer(scores, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def score_detail(request, pk):
    score = Score.objects.get(id=pk)
    serializer = ScoreSerializer(score, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def crew_scores(request, pk):
    scores = Score.objects.filter(crew=pk)
    serializer = ScoreSerializer(scores, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def score_create(request):
    serializer = ScoreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def crew_photo(request, pk):
    crew = Crew.objects.get(id=pk)
    return Response({"name": crew.photo.name, "file": base64.b64encode(crew.photo.file.read())}, status=200)


@api_view(['POST'])
def photo_upload(request, pk):
    file = request.data.get("file")
    name = request.data.get("name")
    photo = ContentFile(base64.b64decode(file), name)

    crew = Crew.objects.get(id=pk)
    crew.photo = photo

    crew.save()
    return Response()
