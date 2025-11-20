from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "ok"})


class NotesCrudTests(APITestCase):
    def test_create_list_retrieve_update_delete_note(self):
        # Create
        create_url = reverse('note-list-create')
        payload = {"title": "First Note", "content": "Hello world"}
        create_resp = self.client.post(create_url, data=payload, format='json')
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        note_id = create_resp.data["id"]

        # List
        list_resp = self.client.get(create_url)
        self.assertEqual(list_resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any(n["id"] == note_id for n in list_resp.data))

        # Retrieve
        detail_url = reverse('note-detail', kwargs={"pk": note_id})
        retrieve_resp = self.client.get(detail_url)
        self.assertEqual(retrieve_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_resp.data["title"], "First Note")

        # Update (PATCH)
        patch_resp = self.client.patch(detail_url, data={"title": "Updated"}, format='json')
        self.assertEqual(patch_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_resp.data["title"], "Updated")

        # Delete
        delete_resp = self.client.delete(detail_url)
        self.assertEqual(delete_resp.status_code, status.HTTP_204_NO_CONTENT)

        # Confirm deleted
        get_after_delete = self.client.get(detail_url)
        self.assertEqual(get_after_delete.status_code, status.HTTP_404_NOT_FOUND)
