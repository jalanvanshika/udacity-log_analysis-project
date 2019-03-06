# Log-Analysis

### Project Overview
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### PreRequisites
- [Python]
- [PostgreSQL]
- [Vagrant]
- [Virtual Machine]
- [Knowledge on HTTP status]
 

### Views
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
select to_char(date(time) ,'Mon DD,YYYY'), (100*sum(case when log.status='200 OK' then 0 else 1 end)/count(log.status)) as "percent error" from log group by date(time) order by "percent error" desc;
````

| Column | Type | 
| ------ | ---- |
| to_char       | text   |
| percent error | bigint |

