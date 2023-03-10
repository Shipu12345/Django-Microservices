#! /bin/sh

cd auth && docker-compose -f docker/docker-compose.dev.yml up -d
cd ../business && docker-compose -f docker/docker-compose.dev.yml up -d