from django.http import HttpRequest
from django.shortcuts import render
from .models import Order


def index(request: HttpRequest):
    context = {
        "orders":
            Order.objects
            #.select_related("job")
            .prefetch_related("worker")
            .order_by('pk').all()
    }

    return render(request=request, template_name="orders/index.html", context=context)
