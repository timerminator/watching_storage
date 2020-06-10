from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visitors_in_vault = Visit.objects.filter(leaved_at=None)

    non_closed_visits = [
      {"who_entered":visitor.passcard.owner_name,
      "entered_at":localtime(visitor.entered_at),
      "duration":visitor.format_duration()} for visitor in visitors_in_vault]

    context = {
        "non_closed_visits": non_closed_visits
    }
    return render(request, 'storage_information.html', context)
