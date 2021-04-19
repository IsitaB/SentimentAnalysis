from tasks import make_celery
from flask import Flask, request

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

@celery.task()
def predict(params):
    return params

@app.route('/api/enqueue')
def enqueue_job():
    pass
