'''
Main entry point for the app
'''
from django.http import JsonResponse

from google.cloud import ndb
from models.note import Note

# Initialize NDB client

client = ndb.Client()


def app(request):
    '''Main entry point for the app'''
    if request.method == "GET":
        user = request.user
        notes = list(Note.query(kind="Note").filter(user == user).fetch())
        return JsonResponse([note.to_dict() for note in notes], safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)