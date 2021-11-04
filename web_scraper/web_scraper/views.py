from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ScrapeRequestForm

from .utils import scrape_google, create_filename


def index(request):
    return render(request, 'web_scraper/index.html')


def web_scraper(request):
    if request.method == 'POST':
        form = ScrapeRequestForm(request.POST)
        if form.is_valid():
            result_size = form.cleaned_data['result_size']

            filename = create_filename()
            with open(filename, 'w+') as f:
                for link_list in scrape_google("how to data engineering", result_size):
                    for a_tag in link_list:
                        f.write(a_tag.raw_html.decode('utf-8'))
                        f.write('\n')

            return HttpResponseRedirect(reverse('confirmation'))
    else:
        form = ScrapeRequestForm()

    return render(request, 'web_scraper/scrape.html', {'form': form})


def confirmation(request):
    return render(request, 'web_scraper/confirmation.html', {})
