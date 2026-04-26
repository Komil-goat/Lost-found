from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemPost
from .forms import FoundItemForm, LostItemForm
from django.contrib.auth.decorators import login_required

@login_required
def item_list(request, post_type):
    items = ItemPost.objects.filter(post_type=post_type, resolved=False)
    return render(request, 'items/list_item.html', {
        'items': items,
        'post_type': post_type
    })

@login_required
def create_item(request, post_type):
    form_class = FoundItemForm if post_type == 'found' else LostItemForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.post_type = post_type
            item.user = request.user
            item.save()
            return redirect(f'{post_type}_list')
    else:
        form = form_class()

    return render(request, 'items/create_item.html', {
        'form': form,
        'post_type': post_type
    })




@login_required
def claim_item(request, item_id):
    item = get_object_or_404(ItemPost, id=item_id)
    item.claimed = True
    item.save()
    return redirect('found_list')


@login_required
def confirmations(request):
    items = ItemPost.objects.filter(
        user=request.user,
        claimed=True,
        resolved=False
    )

    return render(request, 'items/confirmations.html', {
        'items': items
    })

@login_required
def resolve_item(request, item_id):
    item = get_object_or_404(ItemPost, id=item_id)

    if item.user == request.user:
        item.delete()

    return redirect('confirmations')