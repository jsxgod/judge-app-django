from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import *


class ViewsTestCase(APITestCase):

    def setUp(self):
        self.organizer = Organizer.objects.create(name='test', email='test@test', phone='123456789', description='test description')
        self.event = Event.objects.create(organizer=self.organizer, localization='test localization', description='test description', judge_qr='test_judge_qr')

        self.crew1 = Crew.objects.create(event=self.event, number=1, car='test car 1', year_of_production='1991', driver_name='test driver name 1', qr='test crew 1', description='test description 1')
        self.crew2 = Crew.objects.create(event=self.event, number=2, car='test car 2', year_of_production='1992', driver_name='test driver name 2', qr='test crew 2', description='test description 2')

        self.score = Score.objects.create(competition="R", crew=self.crew1, score="1", event=self.event)

    def test_organizer_list_retrieve(self):
        response = self.client.get(reverse("organizer-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_organizer_detail_retrieve(self):
        response = self.client.get(reverse("organizer-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test')

    def test_event_list_retrieve(self):
        response = self.client.get(reverse("event-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_detail_retrieve(self):
        response = self.client.get(reverse("event-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['organizer'], 1)

    def test_crew_list_retrieve(self):
        response = self.client.get(reverse("crew-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_crew_detail_retrieve(self):
        response = self.client.get(reverse("crew-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number'], 1)

        response = self.client.get(reverse("crew-detail", kwargs={"pk": 2}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number'], 2)

    def test_score_post(self):
        response = self.client.get(reverse("score-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.post(reverse("score-create"), data={"competition": "R", "crew": self.crew1.id, "score": 1, "event": self.event.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse("score-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_score_list_retrieve(self):
        response = self.client.get(reverse("score-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_score_detail_retrieve(self):
        response = self.client.get(reverse("score-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)

    def test_crew_scores_retrieve(self):
        response = self.client.get(reverse("crew-scores", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data[0]['id'], 1)
