from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ScrapeRequestForm
from .task import create_filename, google_search


def index(request):
    return render(request, 'web_scraper/index.html')


def web_scraper(request):
    if request.method == 'POST':
        form = ScrapeRequestForm(request.POST)
        if form.is_valid():
            result_size = form.cleaned_data['result_size']

            filename = create_filename()
            google_search.delay(filename, result_size)

            return HttpResponseRedirect(reverse('confirmation'))
    else:
        form = ScrapeRequestForm()

    return render(request, 'web_scraper/scrape.html', {'form': form})


def confirmation(request):
    return render(request, 'web_scraper/confirmation.html', {})
