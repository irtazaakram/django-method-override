from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse


settings.configure(
    DEBUG=True,
    ROOT_URLCONF='tests.django_app',
    SECRET_KEY='secret',
    MIDDLEWARE=(
        'method_override.middleware.MethodOverrideMiddleware',
    ),
)


def index_view(request):
    return HttpResponse('OK')


urlpatterns = (url(r'', index_view), )
