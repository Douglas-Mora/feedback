from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView

#from .models import Review

class ReviewView(View):
    def get(self, request):
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
        })


# Create your views here.
# This next function was replaced by the class ReviewView:
"""def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            #These commented lines correspond to a previous version, using the Review class without the Form class.
            #user_name = form.cleaned_data['user_name'],
            #review_text=form.cleaned_data['review_text'],
            #rating=form.cleaned_data['rating']
            #)
            #review.save()
            form.save()
            #print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })"""


class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
