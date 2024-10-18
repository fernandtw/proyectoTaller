# appRecetas/middleware.py
from django.shortcuts import redirect

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and request.path == '/accounts/profile/':
            if request.user.is_staff:
                return redirect('Panel/admin_dashboard.html')
            else:
                return redirect('home')
        return response
