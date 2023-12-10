FROM mysql:8.2.0

#ENV MYSQL_ROOT_PASSWORD goma
#ENV MYSQL_DATABASE pr_commit_db
#ENV MYSQL_USER me
#ENV MYSQL_PASSWORD goma

COPY ./my.conf /etc/mysql/conf.d/my.cnf

# docker build -t mysql_miku .
# docker run --name mysql_miku -d -v $PWD/db-5-7:/var/lib/mysql -p 3306:3306 mysql_miku
# docker exec -it mysql_miku bash