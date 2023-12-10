 docker build -t  mysql .
 docker run --name mysql -d -v $PWD/db-5-7:/var/lib/mysql -p 3306:3306 mysql
# docker exec -it mysql bash