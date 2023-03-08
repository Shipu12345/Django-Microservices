FROM mysql/mysql-server:8.0

COPY ./docker/mysql/init_db.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh
RUN mkdir -p /tmp/mysql-db/mysqld
RUN chmod -R 777 /tmp/mysql-db/mysqld
