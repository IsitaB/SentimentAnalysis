from celery import Celery

import numpy as np
import tensorflow as tf
import tensorflowjs as tfjs
from tensorflow.keras.utils import get_file

# model = tfjs.converters.load_keras_model('./model.json')
# model._make_predict_function()    # Some bug in Keras necessitates this line

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
