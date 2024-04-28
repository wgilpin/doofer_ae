from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render


def root(request: HttpRequest):
    '''Main entry point for the app'''
    if request.method == "GET":
        if request.htmx:
            # render the root.html template
            return render(request, "root.html", {"htmx": True, "notes": [{"title" : "first note"}]})
        # render the root.html template
        return render(request, "root.html", {"htmx": False})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
