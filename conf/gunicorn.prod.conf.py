import os

bind = "127.0.0.1:8887"
logfile = "/var/www/vhosts/twy_production/logs/gunicorn.log"
max_requests = 1000
workers = 2
proc_name = 'gunicorn_twy_production'
