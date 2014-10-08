# Homepage for UsBeatIT

## Setup

This project requires the Python programming language and [git](http://git-scm.com/) to be installed in the system. Also make sure you have [pip](https://pypi.python.org/pypi/pip) and is highly recommended to have [virtualenv](http://virtualenv.readthedocs.org/en/latest/) installed as well.

1) Clone the repo:
```
> git clone git@github.com:netogallo/beatit.git
```

2) Create & activate a virtual environment:
```
> cd beatit
> virtualenv env
> source env/bin/activate
```

3) Install the requirements
```
> pip install -r requirements.txt
```

4) Create a local settings file:
```
cp usbeatit/usbeatit/settings_local.py.example usbeatit/usbeatit/settings_local.py
```

5) Go to the project directory
```
cd usbeatit
```

6) Initalize/Sync the database
```
python manage.py migrate usbeatit.settings_local
```

7) Run the server:
```
python manage.py runserver --settings usbeatit.settings_local
```