Initial Setup
-------------

To read this document in html, `CMD + Shift + P` > `Markdown: Open Preview`.

* Create the virtual environment: `python3 -m venv .pyenv`
* Activate the virtual environment: `source commands/activate`
* Install dependencies: `pip install -r requirements.txt`
* Create migrations: `python3 whcccode/manage.py makemigrations`
* Run migrations: `python3 whcccode/manage.py migrate`

To Run the Project
------------------

`python3 whcccode/manage.py runserver 0.0.0.0:8042`