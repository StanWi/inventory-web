from django.shortcuts import render
from django.utils import timezone
from .models import Vendor

def post_list(request):
    vendors = Vendor.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inventory/post_list.html', {'vendors': vendors})

