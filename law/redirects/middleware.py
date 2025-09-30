from django.http.response import HttpResponsePermanentRedirect

from .models import Redirects



class URLRedirectsMiddleware:

    "Redirect from legacy urls to updated ones"


    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_response(request, response)

    def process_response(self, request, response):
        if response.status_code != 404:
            return response

        try:
            redirect = Redirects.objects.get(from_url=request.path)
            return HttpResponsePermanentRedirect(redirect.to_url)
        except Redirects.DoesNotExist:
            return response
