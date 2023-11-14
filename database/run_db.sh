 docker build -t mysql_miku .
 docker run --name mysql_miku -d -v $PWD/db-5-7:/var/lib/mysql -p 3306:3306 mysql_miku
# docker exec -it mysql_miku bash