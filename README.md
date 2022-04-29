# Mailing Manager App

Mailing manager is a simple app for mass mailings.

The app is written in Python, using Django (DRF).

Celery and Redis are used to implement async tasks.

[[_TOC_]]

## Getting Started

### Messing with settings

`setting.CELERY_BROKER_URL` - defines message broker for async tasks.
`DEFAULT='redis://localhost:6379'`;

`settings.MAILING_REPEAT_TIMEOUT` - controls the timeout period upon the expiration of which app will try to process failed tasks.
`DEFAULT=60 * 10` (10 minutes);

`settings.MESSAGE_SENDER_TOKEN` - token for external API that is responsible for message delivery.

### Starting the app
1. In the current state of the project Redis server has to be launched manually:
    ```
    redis-server start
    ```

2. The app can be launched via:
    ```
    py main.py
    ```
    but that way there will be only one Celery worker. We have to use `--pool=solo` option for compatibility with Windows.
    An alternative option is launching Django, Celery beat and Celery worker manually.
3. Starting Django:
    ```
    py manage.py runserver
    ```

4. Starting beat:
    ```
    celery -A mailing_manager_project beat -l warning --max-interval 60
    ```
    `--max-interval` option controls how often Celery beat will check for new mailings to start. `DEFAULT=60` (1 minute)

5. Starting worker:
    ```
    celery -A mailing_manager_project worker --pool=solo -l warning
    ```
**Up and Running!**


## How it works
Three message states:
- `pending` - message has not been processed yet;
- `success` - message have been sent and shouldn't be processed again;
- `fail` - attempt to send a message have failed. But there may be more.


Three async tasks:
- `start_mailing` - periodically (every minute by default) checks for mailings to start or restart after timeout;
- `send_message` - requests API to send the message and marks it according to response;
- `finish_mailing` - marks expired messages as failed, mailings as finished. So they won't be enqueued again.

## OpenAPI reference
Can be found at `api/v1/docs/` or on [SwaggerHub](https://app.swaggerhub.com/apis/ledorubden/Mailing-manager-app/1.0.0#/statsSummary)
