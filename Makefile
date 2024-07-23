# Variables
COUNTRY=US
STATE=California
LOCATION=San Francisco
ORGANIZATION=Kamath
SSL_DAYS=365

# Functions
define clean_dir
	@echo "Cleaning $(1)..."
	@find $(1) -mindepth 1 -not -name '.gitkeep' -delete
endef

# Commands
refresh:
	@echo "Refreshing the project..."
	$(call clean_dir,./meta/config)
	$(call clean_dir,./meta/logs)
	$(call clean_dir,./meta/data)
	$(call clean_dir,./meta/ssl)

create-ssl:
	@echo "Creating SSL certificates..."
	@if [ ! -d "./meta/ssl" ]; then echo "Creating directory ./meta/ssl..."; mkdir -p ./meta/ssl; fi
	@openssl req -x509 -nodes -days ${SSL_DAYS} -newkey rsa:2048 -keyout ./meta/ssl/gitlab.kamath.work.key -out ./meta/ssl/gitlab.kamath.work.crt -subj "/C=${COUNTRY}/ST=${STATE}/L=${LOCATION}/O=${ORGANIZATION}"

docker-up:
	@echo "Starting the docker containers..."
	@docker compose up -d

docker-down:
	@echo "Stopping the docker containers..."
	@docker compose down

docker-stop:
	@echo "Stopping the docker containers..."
	@docker compose stop

docker-start:
	@echo "Starting the docker containers..."
	@docker compose start

docker-watch:
	@echo "Watching the docker containers..."
	@docker compose logs -f

init: docker-down refresh create-ssl docker-up
	@echo "Project initialized successfully!"