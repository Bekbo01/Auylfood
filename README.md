# Auylfood
Бұл Auylfood серверін Ubuntu ОЖ-де орнату, іске қосу және орналастыру туралы нұсқаулық.
Жобаны орнату және іске қосу үшін сізге қажет:
 • python3
 • pip
 • виртуалды орта
 Орнату үшін:
   sudo apt-get update
   sudo apt-get install python3
   sudo apt-get install python-pip
   pip install virtualenv
 Орнату
 Клон репозиторийі:
         	  git clone bekbo@repo
Auylfood қалтасына өтіп, виртуалды орта жасаңыз:
  cd Auylfood
 virtualenv -p /usr/bin/python3.5 venv
Виртуалды ортаны қолдануды бастау үшін оны қосу қажет:
 	  source venv/bin/activate
Керекті модульдерді виртуалды ортаға орнатыңыз:
              pip install -r requirements.txt
Django модельдерін көшіру:
      python manage.py makemigrations
      python manage.py migrate
Жоба бойынша жоба DEBUG = True және SQLite мәліметтер базасымен жұмыс істейді. Жобаны жергілікті деңгейде іске қосамыз:
     python manage.py runserver
Сервер localhost: 8000-де жұмыс істеуі керек
