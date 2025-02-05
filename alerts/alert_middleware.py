# Struture of a , middleware
# Class()
# __init__(self, get_response): Called once when the server starts. Here, you can perform one-time configuration.

# __call__(self, request): Called on each request. This method must return a response. 
#Run to ALL request. SHould use when needing to log or scrape or doing something all people can do

# process_view(self, request, view_func, view_args, view_kwargs): 
# Called just before the view is called. You can modify the request or abort the request by returning None.

# process_exception(self, request, exception): Called when a view raises an exception.

# process_template_response(self, request, response): Called just after the view is called if the response has a render() method.

from django.http import JsonResponse


class RequestMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("Middleware is working")
    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        print("calling request")
        response = self.get_response(request)
        # # Code to be executed for each request/response after the view is called.
        # if not request.user.is_authenticated:
        #     return JsonResponse({"error": "Authentication required"}, status=401)
        return response    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Called just before the view is called.
        print("processing view")
        

        return None