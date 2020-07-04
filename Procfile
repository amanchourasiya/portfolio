release: python3 portfolio/manage.py makemigrations
release: python3 portfolio/manage.py migrate
web: gunicorn -b 0.0.0.0:$PORT --chdir portfolio/ portfolio.wsgi --log-file -
