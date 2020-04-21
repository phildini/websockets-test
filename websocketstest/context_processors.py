from django.conf import settings


def webpack_env(request):

    return {"WEBPACK_ENV": settings.WEBPACK_ENV}
