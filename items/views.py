from django.shortcuts import render, redirect
from .models import ItemPost
from .forms import FoundItemForm


def found_items_list(request):
    items = ItemPost.objects.filter(post_type='found', resolved=False)
    return render(request, 'items/found_list.html', {'items': items})


def create_found_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.post_type = 'found'
            item.user = request.user
            item.save()
            return redirect('found_list')
    else:
        form = FoundItemForm()

    return render(request, 'items/create_found.html', {'form': form})