from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Employee, JobTitles


def index(request: HttpRequest):

    context = {
        "employees":
            Employee.objects
            .select_related("job")
            .order_by('pk').all()
    }

    return render(request=request, template_name="employees/index.html", context=context)
