from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Vendor

def post_list(request):
    vendors = Vendor.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inventory/post_list.html', {'vendors': vendors})

def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'inventory/vendor_detail.html', {'vendor': vendor})
