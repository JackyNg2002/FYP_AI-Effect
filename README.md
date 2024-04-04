# FYP_AI-Effect

build:

docker build -f docker/dockerfile -t {name} .


run:

docker compose up --scale fyp_effect={number of ai effect web server}