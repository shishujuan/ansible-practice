from __future__ import unicode_literals
import multiprocessing
import os

bind = "0.0.0.0:{}".format(os.environ.get("GUNICORN_PORT", 8000))
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = "error"
errorlog = "/var/log/gunicorn-error.log"
accesslog = "/var/log/gunicorn-access.log"

proc_name = "mezzanine"
