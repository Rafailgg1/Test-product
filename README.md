Windows:
    run `app/scripts/initialize.bat`
    run `venv\Scripts\activate`

Linux:
1. `source scripts/initialize.sh`
2. `source venv\bin\activate`

Next:
1. `cd app`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`