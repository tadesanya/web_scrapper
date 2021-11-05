# Google Web Scrapper

Project to run a google search for 'how to data engineering', scrape the links from the search result page and store the corresponding html for those links in a text file on the project root directory.

## Setup
- Clone this repo and cd into the project root (the folder that contains the README.md)
- Create a virtual environment and install the requirements by running the command `pip install -r requirements.txt`
- In project root directory, create an `.env` file and put in values for:
```bash
DEBUG=True
SECRET_KEY=your-random-django-secret
HOSTS=127.0.0.1,localhost,localhost:8000,127.0.0.1:8000
```

### If you want to run the project locally
- First Install Redis on your local machine via `brew install redis` and start the server with `redis-server`
- Open A command line terminal, activate your virtual environment, CD into the project folder `web_scrapper/web_scraper` (where the manage.py file is) and run `celery -A web_scraper worker -l INFO` to activate the celery worker
- Open another command line terminal, remember to activate your virtual environment, CD into the project root `web_scrapper` (where the README.md file is) and run `python web_scraper/manage.py runserver` to start the django server.
- You can now open `http://127.0.0.1:8000/` in your web browser to see the app running.
- Any result file generated would be stored in the root directory of the project.

### if you want to run the project from docker
- Install docket on your local machine
- In the project root directory, run `docker-compose up --build`
- Open `http://localhost:8000/` in your browser, and you should be able to see the app running.

### To run tests
- CD into the project root directory and activate your virtual environment and run `pytest`