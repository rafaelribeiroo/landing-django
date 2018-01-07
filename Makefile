clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -name "*.pyc" -exec rm -rf {} \;i

run:
	python manage.py runserver 127.0.0.1:8000

migrate:
	python manage.py migrate
	python manage.py migrate newsletter

migrations:
	python manage.py makemigrations
	python manage.py makemigrations newsletter

user:
	python manage.py createsuperuser

test:
	python manage.py test
	python manage.py test newsletter

shell:
	python manage.py shell

staticfiles:
	python manage.py collectstatic
