# TuhaoChe

This is an tools for tuhaoche

# prepare the dev environment

setup environment

    brew install mysql-connector-c

    mkvirtualenv weibo
    workon weibo

    pip -r requirements.txt

init database

    mysql -u root -e "CREATE DATABASE thc DEFAULT CHARSET utf8 COLLATE utf8_general_ci;"
    mysql -u root -e "CREATE USER 'thc'@'%' IDENTIFIED By 'thc'";
    mysql -u root -e "GRANT ALL PRIVILEGES ON thc.* TO 'thc'@'%' WITH GRANT OPTION";

    python utils/db_init.py

start web server

    python run_app.py
    
#api

oursnews | news
    
    curl http://localhost:5000/api/oursnews/?ordering=score
    curl http://localhost:5000/api/oursnews/1/
    
    curl -u admin:admin -X POST -d data='{"text": "shanghai"}' http://127.0.0.1:5000/api/oursnews/
    curl -u admin:admin -X PUT -d data='{"text": "shanghai"}' http://127.0.0.1:5000/api/oursnews/1/
    curl -u admin:admin -X DELETE http://127.0.0.1:5000/api/oursnews/1/

# Thanks

+ [Flask](http://flask.pocoo.org)
