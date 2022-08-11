"""Settings for Gunicorn.

http://docs.gunicorn.org/en/stable/settings.html
"""

accesslog = "-"  # '-' means log to stdout.
bind="0.0.0.0:8000"
graceful_timeout=60
max_requests_jitter=500
max_requests=5000
worker_class="uvicorn.workers.UvicornWorker"
workers=4
