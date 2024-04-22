from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render


def root(request: HttpRequest):
    '''Main entry point for the app'''
    if request.method == "GET":
        # render the root.html template
        return render(request, "root.html")
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
