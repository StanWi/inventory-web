from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Vendor, Country
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    vendors = Vendor.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inventory/post_list.html', {'vendors': vendors})

def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'inventory/vendor_detail.html', {'vendor': vendor})

def vendor_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.author = request.user
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = PostForm()
        return render(request, 'inventory/vendor_edit.html', {'form': form})

def vendor_edit(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.author = request.user
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = PostForm(instance=vendor)
        return render(request, 'inventory/vendor_edit.html', {'form': form})
