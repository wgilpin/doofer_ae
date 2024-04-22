'''
Main entry point for the app
'''
from django.http import JsonResponse
from django.http.request import HttpRequest

from google.cloud import ndb
from models.note import Note

# Initialize NDB client

client = ndb.Client()


def app(request: HttpRequest) -> JsonResponse:
    '''Main entry point for the app'''
    if request.method == "GET":
        user = request.user
        notes: list[Note] = list(Note.query(kind="Note").filter(user == user).fetch())
        return JsonResponse([note.to_dict() for note in notes], safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)