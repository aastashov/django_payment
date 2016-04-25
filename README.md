# django_payment

Как начать работу:

Установить все что нужно для джанги:
sudo apt-get install python-dev python-pip libmysqlclient-dev mysql-server virtualenv

Это для Pillow:
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
     libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

Создать виртуальное окружение:
virtualenv name_env

Зайти в виртульное окружение:
source name_env/bin/activated

Установить нужные пакеты для этого проекта:
pip install -r requirements.txt

Если будет ругаться на что-то вроде "Command "python setup.py egg_info" failed with error code 1....",
то попробуй:
pip install --upgrade setuptools
и заново:
pip install -r requirements.txt
