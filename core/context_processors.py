from django.conf import settings


def empresa(request):
    return { 'empresa': settings.EMPRESA }
