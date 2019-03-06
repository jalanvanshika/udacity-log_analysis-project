# Log-Analysis
    This is the first project under udacity full stack web development nanodegree  course.
### Project Overview
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### Software Requirements
- [Python](https://www.python.org/)
- [Vagrant](https://www.vagrantup.com/)
- [Virtual Machine](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Git](https://git-scm.com/downloads)

### Tech Stack
- Python
    1. Writing code with DB-API
- PostgreSQL
    1. Joining Tables
    2.  Views
    3. SQL string functions
- Knowledge on HTTP handler


### Set-Up
**1. Launch the  Vagrant Virtual Machine inside the vagrant sub-directory by       using:**
 ```sh
$ vagrant up
```
**2. Log into your vm by using:**
```sh
$ vagrant ssh
```
**3. Change directory to /vagrant by using:**
```sh
$ cd /vagrant
```
**4. Load the database by using:**
```sh
psql -d news -f newsdata.sql
```
**5. Connect to database by using:**
```sh
psql -d news
```
**6. Explore the data\tables by using:**
```
\dt+ (or)
\d table
```
**7. Create Views**
1. Creating first view which is used to get the required output for first two questions.
```sh
create view view_count as
select articles.title,articles.author,count(log.path) as views
from articles, log where log.path like concat('%',articles.slug)
group  by articles.title, articles.author;
````

 | Column |  Type   | 
 | --------|--------|
 | title  | text    |
 | author | integer |
 |views  | bigint  |

2. Creating second view which is used to get required output for the third question.
```sh
create view error as
select to_char(date(time) ,'Mon DD,YYYY'), (100*sum(case when log.status='200 OK' then 0 else 1 end)/count(log.status)) 
   as "percent error" from log group by date(time) 
   order by "percent error" desc;
````

| Column | Type | 
| ------ | ---- |
| to_char       | text   |
| percent error | bigint |

**Running the program**
    1. cd into the folder having log_analysis.py file and run:
    ```sh
    $ python log_analysis.py
    ```
