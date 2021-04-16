from apscheduler.schedulers.background import BackgroundScheduler


def start():
    from api.Repository.PayRepository import PayRepository
    scheduler = BackgroundScheduler()
    scheduler.add_job("hello waiting", 'interval', minutes=1)
    scheduler.start()
