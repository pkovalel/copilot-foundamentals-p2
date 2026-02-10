"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def api_root(request):
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base_url = f"https://{codespace}-8000.app.github.dev/api/"
    else:
        base_url = "http://localhost:8000/api/"
    return JsonResponse({
        "activities": base_url + "activities/",
        "users": base_url + "users/",
        "teams": base_url + "teams/",
        "workouts": base_url + "workouts/",
        "leaderboard": base_url + "leaderboard/",
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
]
