#安装需求(待补充)
请按顺序进行
##安装mysql
sudo apt-get install mysql-server
##设置mysql
1. 创建mysql-server的root用户(应该在安装时候就建立好了)
2. 用root用户登录mysql-server: mysql -u root -p password
3. 建立数据库: create database django_trustclassProject default charset=utf8;
4. 建立新用户: create user 'tc'@'localhost' indentified by '12345678';
5. 为tc授权: grant all on django_trustclassProject.\* to tc;

##安装Django Simple Captcha
- https://github.com/mbi/django-simple-captcha
- sudo pip install django-simple-captcha

##安装python3-dev
sudo apt-get install python3-dev

##安装libmysqlclient-dev
sudo apt-get install libmysqlclient-dev

##安装mysqlclient
sudo pip3 install mysqlclient

##进入trustclassProject文件夹
1. python3 manage.py migrate
2. python3 manage.py createsuperuser 名字什么的你自己随意, 要用这个登录网站
3. python3 manage.py runserver 这会让服务器在localhost:8000跑起来
4. 访问localhost:8000/init
5. 访问localhost:8000 使用你的superuser登录
