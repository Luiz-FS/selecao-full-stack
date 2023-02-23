python3 -m virtualenv env
source env/bin/activate

cd api && pip install -r requirements/requirements.txt
cd realtimequote && python manage.py fill_quotation_history