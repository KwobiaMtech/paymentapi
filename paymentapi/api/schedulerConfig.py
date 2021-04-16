from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from .Repository.PayRepository import PayRepository as rep
        scheduler = BackgroundScheduler()
        scheduler.add_job(rep.updateAllTransactions, 'interval', minutes=1)
        scheduler.start()

