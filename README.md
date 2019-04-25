# Uniqlo

Crawl Uniqlo online store, provide api for further analysis.

## Installation
### spider
Use Scrapy to crawl data.

1. Go to `spider` folder, install dependencies.

```bash
pipenv install
```

2. Set up Postgres, create database.

```bash
psql -U uniqlo -d uniqlo -a -f spider/spider/db/init_db.sql
```

3. Run scrapy.

```bash
scrapy crawl uniqlo_ca
```



## backend

- Use Spring Boot to provide database access and REST api support.
- Use Shiro for authentication and authorization support.

Go to `backend` folder, run the application with following command:

```bash
./mvnw spring-boot:run
```



## Database Design

![uniqlo_db](/Users/joy/Documents/personal_workpace/uniqlo/uniqlo_db.png)