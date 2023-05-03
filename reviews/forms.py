from django import forms
from .models import Review

""" class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Your name", required=True, error_messages={
        "required": "This field is required",
        "max_length": "Please enter a name no longer than 100 characters long."
                                                                                                  })
    review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
     """


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "required": "This field is required",
            "max_length": "Please enter a name no longer than 100 characters long."
        }
