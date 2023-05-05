from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review

#from .models import Review

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    # Next function was no longer needed when switched from FromView class..
    # ... to the CreateView class.
    """def form_valid(self, form):
        form.save()
        return super().form_valid(form)"""
    

    #The next two functions worked when using the View class.
    """def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form":form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form":form
        })"""


# Create your views here.

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    

class ReviewsListView(ListView):
     template_name = "reviews/review_list.html"
     model = Review
     context_object_name = "reviews"

     def get_queryset(self):
         # This is just to filter the data, by selecting reviews
         # with a rating (for example) greater than 3.
         base_query = super().get_queryset()
         data = base_query.filter(rating__gt=3)
         return data
        

     
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review