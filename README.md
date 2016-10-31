# django_payment

Создай БД:  
>create database django_payments character set utf8 collate utf8_general_ci;

Если забыл, то поставь  
>sudo apt-get install python-dev python-pip libmysqlclient-dev mysql-server

Это для Pillow (Ubuntu 14.04)  
>sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
>    liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

Если нужно, то поставь virtualenvwrapper:  
>sudo pip install virtualenvwrapper

Под виртуальным окружением, установи зависимости:  
>pip install -r requirements.txt

Если будет ругаться на что-то, то ЧИТАЙ и гугл в помощь  
  
Пополнение баланса, это тоже транзкция, ведь деньги откуда то беруться.  
В данном случае, тебе их будет переправлять платежная сстема.  
Для этого открой mysql и добавь пару категорий:  
>insert into payments_category (id, title, slug, display, img) values (1, "PaymentSystem", paymentsystem, 0, "media/image/uploads_category/PaymentSystem.jpg");
>insert into payments_category (id, title, slug, display, img) values (2, "Мобильная связь", mobile, 1, "media/image/uploads_category/mobile.png");
>insert into payments_category (id, title, slug, display, img) values (3, "Телевидение", television, 1, "media/image/uploads_category/television.png");
  
и пару провайдеров:  
  
>insert into payments_provider (id, name, img, account, description, display, category_id, manager_id) values (1, "PaymentSystem", "media/image/uploads_provider/PaymentSystem.jpg", 531, "Платежная система", 0, 1, 1);
>insert into payments_provider (id, name, img, account, description, display, category_id, manager_id) values (2, "Beeline", "media/image/uploads_provider/beeline.png", 384, "https://beeline.kg/kg/", 1, 2, 1);
>insert into payments_provider (id, name, img, account, description, display, category_id, manager_id) values (3, "AlaTV", "media/image/uploads_provider/alatv.png", 373, "http://alatv.kg/", 1, 3, 1);

  
Чтобы работала вторизация FaceBook:  
Добавь через аминку возможность регистрироваться в FB и  
раскомментируй 30-ю строчку в файле:  
>/django_payment/profiles/templates/login.html
