class CorsMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        response = self.get_response(request)
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Origin'] = '*'  # Update with appropriate origin(s)
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response