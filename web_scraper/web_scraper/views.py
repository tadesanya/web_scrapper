from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ScrapeRequestForm


def index(request):
    return render(request, 'web_scraper/index.html')


def web_scraper(request):
    if request.method == 'POST':
        form = ScrapeRequestForm(request.POST)
        if form.is_valid():
            # call web scraping process
            return HttpResponseRedirect(reverse('confirmation'))
    else:
        form = ScrapeRequestForm()

    return render(request, 'web_scraper/scrape.html', {'form': form})


def confirmation(request):
    return render(request, 'web_scraper/confirmation.html', {})
