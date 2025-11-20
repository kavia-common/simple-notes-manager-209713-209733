from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def health(request):
    """
    Health check endpoint.

    Returns a simple JSON payload indicating the server status.

    Response:
        200 OK: {"status": "ok"}
    """
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


class NoteListCreateView(ListCreateAPIView):
    """
    List and create notes.

    - GET /api/notes/: Returns a list of notes ordered by updated_at desc by default.
    - POST /api/notes/: Creates a new note with 'title' and optional 'content'.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single note by ID.

    - GET /api/notes/{id}/
    - PUT/PATCH /api/notes/{id}/
    - DELETE /api/notes/{id}/
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
