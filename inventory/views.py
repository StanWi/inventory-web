from django.shortcuts import render

def post_list(request):
    return render(request, 'inventory/post_list.html', {})

