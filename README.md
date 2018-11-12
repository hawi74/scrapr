# Scrapr
Scapr is a Django based application that fetches exchange rates from ECB and provides access to them in JSON format via REST API.

# Running Scrapr
The easiest way to run Scrapr is with Docker:
1. Clone the repo
2. `cd` into it
3. Run `docker-compose build`
4. Run `docker-compose run django python manage.py migrate` in order to prepare DB
5. Run `docker-compose up` to run the application :)

# Architecture
Since there is not much logic in Scraper, the code is organized in a traditional Django-style structure, where everything resolves around model. Scrapr uses Docker, PostgreSQL as primary DB, Celery to run periodic tasks, RabbitMQ as a message broker for Celery.

# Tests
In order to run tests, follow `Running Scrapr`, but instead of the last step, run `docker-compose run django python manage.py test`.
