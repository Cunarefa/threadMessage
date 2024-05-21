# Chat app

Simple chat application based on interaction between Users, Threads and Messages.

## Mac

Creating the environment:

```
python3 -m venv venv  # create the python virtual environment
source venv/bin/activate  # activate the python virtual environment
pip install -r requirements.txt  # install our python dependencies
```

### Getting started

Run the following command to run the latest migrations:

```bash
python manage.py migrate
```

Run the following command to populate database with data from dump file:

```bash
python manage.py create_random_users
python manage.py create_random_threads
python manage.py create_random_messages
```

To run application server run the following command:

```bash
python manage.py runserver
```