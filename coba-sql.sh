docker exec "mysql" mysql -u "root" -ptoor -e "SELECT DISTINCT User from mysql.user"

# kalau tidak pakai docker:
# mysql -u "root" -ptoor -e "SELECT DISTINCT User from mysql.user"