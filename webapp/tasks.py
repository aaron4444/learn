from webapp.extensions import celery
@celery.task()
def log(msg):
    return msg


#@celer.task(bind=True)
#def task(self, param):
#    try:
#        some_code
#    except Exception, e:
#        self.retry(exc=e)
@celery.task()
def multiply(x,y):
    return x*y
