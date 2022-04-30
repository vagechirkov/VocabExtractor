from django.shortcuts import render
from django import forms
from extractor.models import Word

class TestForm(forms.Form):
    text_area = forms.CharField(max_length=1000, widget=forms.Textarea)


def index(request):
    form = TestForm()
    return render(request, "extractor_form.html", {"form": form})


def extract(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            text_area = form.cleaned_data["text_area"]

            # extract words from the text_area
            words = text_area.split()
            # remove punctuation
            words = [word.strip(".,!?;:") for word in words]
            # remove empty words
            words = [word for word in words if word]

            # add words to the database
            for word in words:
                Word.objects.get_or_create(word=word)

            # render the page with the words from the database
            return render(
                request, "new_words.html", {"words": Word.objects.all()})
