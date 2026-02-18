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

from django.contrib import admin
from django.urls import path, include

import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


# Helper to build full API URLs using $CODESPACE_NAME
def get_base_url():
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        return f"https://{codespace_name}-8000.app.github.dev"
    return "http://localhost:8000"

@api_view(['GET'])
def api_root(request, format=None):
    base_url = get_base_url()
    return Response({
        'users': f"{base_url}{reverse('user-list', request=request, format=format)}",
        'teams': f"{base_url}{reverse('team-list', request=request, format=format)}",
        'activities': f"{base_url}{reverse('activity-list', request=request, format=format)}",
        'workouts': f"{base_url}{reverse('workout-list', request=request, format=format)}",
        'leaderboard': f"{base_url}{reverse('leaderboard-list', request=request, format=format)}",
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
    path('', api_root, name='api-root'),
]
