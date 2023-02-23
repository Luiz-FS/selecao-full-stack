define setup_env
	$(eval ENV_FILE := $(1))
	@echo " - setup env $(ENV_FILE)"
    $(eval include $(1))
    $(eval export)
endef

migrate: run-dependecies
	docker-compose exec api python manage.py migrate --noinput
	docker-compose exec authenticator python manage.py migrate --noinput

	docker-compose exec api python manage.py loaddata fixtures/dump.json --app coin --app auth.user
	docker-compose exec authenticator python manage.py loaddata fixtures/dump.json --app auth.user

fill-quotations:
	$(call setup_env, api/realtimequote/.env_prod)
	bash fill_quotations.sh

test: run-dependecies
	bash test_runner.sh

run-api-local:
	$(call setup_env, api/realtimequote/.env_prod)
	cd api/realtimequote && python manage.py runserver

run-authenticator-local:
	cd authenticator/authenticator && python manage.py runserver 8001

run-celery-worker-local:
	$(call setup_env, api/realtimequote/.env_prod)
	cd api/realtimequote && celery -A realtimequote worker -l INFO

run-celery-beat-local:
	$(call setup_env, api/realtimequote/.env_prod)
	cd api/realtimequote && celery -A realtimequote beat -l INFO

run-dependecies:
	docker-compose -f docker-compose-dependecies.yml up -d

run-celery:
	docker-compose -f docker-compose-celery.yml up -d

run: run-dependecies run-celery
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

down-dependecies:
	docker-compose -f docker-compose-dependecies.yml down

down-celery:
	docker-compose -f docker-compose-celery.yml down
