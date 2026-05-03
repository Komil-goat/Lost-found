from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemPost, Tag
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import JsonResponse

@login_required
def item_list(request, post_type):
    items = ItemPost.objects.filter(post_type=post_type)

    tag_slugs = request.GET.getlist('tag')

    selected_tags = []
    if tag_slugs:
        matching_tags = [
            tag for tag in Tag.objects.all()
            if slugify(tag.name) in tag_slugs
        ]
        selected_tags = [tag.id for tag in matching_tags]
        items = items.filter(tags__id__in=selected_tags).distinct()

    tags = Tag.objects.all()
    
    return render(request, 'items/list_item.html', {
        'items': items,
        'post_type': post_type,
        'tags': tags,
        'selected_tags': selected_tags,
        'selected_slugs': tag_slugs
    })

@login_required
def create_item(request, post_type):
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.post_type = post_type
            item.user = request.user
            item.save()
            form.save_m2m()
            return redirect(f'{post_type}_list')
    else:
        form = form_class()

    return render(request, 'items/create_item.html', {
    'form': form,
    'post_type': post_type,
    'is_edit': False
    })




@login_required
def claim_item(request, item_id):
    item = get_object_or_404(ItemPost, id=item_id)
    item.claimed = True
    item.save()
    if item.post_type == "found":
        return redirect("found_list")
    else:
        return redirect("lost_list")


@login_required
def confirmations(request):
    items = ItemPost.objects.filter(
        user=request.user,
        claimed=True
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

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(ItemPost, id=item_id)

    if item.user != request.user:
        return redirect(f'{item.post_type}_list')

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(f'{item.post_type}_list')
    else:
        form = ItemForm(instance=item)

    return render(request, 'items/create_item.html', {
        'form': form,
        'post_type': item.post_type,
        'is_edit': True
    })

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(ItemPost, id=item_id)

    if item.user == request.user:
        post_type = item.post_type
        item.delete()
        return redirect(f'{post_type}_list')

    return redirect('found_list')

@login_required
def item_detail(request, item_id):
    item = get_object_or_404(ItemPost, id=item_id)

    request.session['last_list_url'] = request.META.get('HTTP_REFERER')

    return render(request, 'items/item_detail.html', {
        'item': item
    })

@login_required
def match_items(request):
    query = request.GET.get('q', '').strip()
    post_type = request.GET.get('type')

    opposite_type = 'found' if post_type == 'lost' else 'lost'

    results = []

    if query:
        items = ItemPost.objects.filter(
            post_type=opposite_type,
            title__icontains=query,
            claimed=False
        )[:5]

        for item in items:
            results.append({
                'id': item.id,
                'title': item.title,
                'location': item.location,
                'date': item.date.strftime('%Y-%m-%d'),
            })

    return JsonResponse({'results': results})