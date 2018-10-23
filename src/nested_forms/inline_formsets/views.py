from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChildrenFormset
from .models import  Parent

def home(request):
    pass


def manage_children(request, parent_id):
    """Edit children and their addresses for a single parent."""

    parent = get_object_or_404(Parent, id=parent_id)

    if request.method == 'POST':
        formset = ChildrenFormset(request.POST, instance=parent)
        if formset.is_valid():
            formset.save()
            return redirect('parent_view', parent_id=parent.id)
    else:
        formset = ChildrenFormset(instance=parent)

    return render(request, 'inline_formsets/manage_children.html', {
                  'parent':parent,
                  'children_formset':formset})
