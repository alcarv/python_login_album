from django.http import JsonResponse

def login(request):
    if request.method == 'GET':
        auth = {'id': 1, 'email': 'Alefe@Junior', 'password': 'XPTO'}
        return JsonResponse(auth)
# Create your views here.
