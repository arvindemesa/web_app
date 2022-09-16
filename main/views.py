import requests
from django.http import JsonResponse
from django.shortcuts import render

from main.methods import get_processes_info


def view_dashboard(request):

    processes = get_processes_info()

    url = 'https://api.stackexchange.com/2.2/search?intitle=grafana&site=stackoverflow'
    response = requests.get(url).json()
    top10_views = sorted(response['items'], key=lambda d: d['view_count'], reverse=True)[:10]

    context = {
        'processes': processes,
        'top10_views': top10_views
    }

    return render(request, 'view_dashboard.html', context)

def refresh_cpu(request):

    processes = get_processes_info()
    data = {
        'processes': processes
    }
    return JsonResponse(data)