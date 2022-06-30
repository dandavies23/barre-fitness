from django.shortcuts import render, redirect, reverse, get_object_or_404
django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import FitnessClass


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """
    classes = FitnessClass.object.all()

    context = {
        'classes': classes,
    }

    return render(request, "classes/classes.html", context)
    