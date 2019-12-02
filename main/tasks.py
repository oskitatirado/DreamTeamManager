from __future__ import absolute_import
import datetime
from celery.task.base import periodic_task
from main.utils import prueba_task


@periodic_task(run_every=datetime.timedelta(seconds=30))
def test():
    prueba_task()
