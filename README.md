# Todo items CRUD in Fast API
This is a simple CRUD example creating Todo list item with title and description , developed in Fast API connecting with PostgreSQL.

## Installation and setup
This is installable through docker, please make sure that you have docker installed and you can run docker and docker-compose on your machine.

To install through docker, you just need to download the code and then
- First build it using
`docker-compose build`

- then run it using
`docker-compose up`

please note that you probably need to use `sudo` , depends on your docker installation.

Once it is up and running, please run it through your browser: http://localhost

## API Docs:
Here you can find API Docs at http://localhost/docs to see all the endpoints you can execute.

## Futher Maintenance:
Right now this code doesn't include any test cases, so before proceeding further it is always better to write tests. However, if one want to change the DB connection then database.py is the file to change DB connection, while one can always add dependencies through requirements.txt file.
