# How to run Odoo with this Compose file ?

- First, create a `.env` file where you'll set the environment variables that will be used by both the odoo and the postgres containers ;
- Run `docker compose up -d` and head to **127.0.0.1: < whatever you set the port to>** in your browser.

> An exemple of the **.env** file

```
# Odoo env variables

HOST=db  // The address of the postgres server. If you used a postgres container, set to the name of the container. Defaults to db.
USER=odoo  // The postgres role with which Odoo will connect. If you used a postgres container, set to the same value as POSTGRES_USER. Defaults to odoo.
PASSWORD=odoo  // The password of the postgres role with which Odoo will connect. If you used a postgres container, set to the same value as POSTGRES_PASSWORD. Defaults to odoo.

# Postgres env variables
POSTGRES_DB=postgres
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo

```
