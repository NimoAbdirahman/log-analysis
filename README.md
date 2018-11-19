            Logs Analysis Project

This log analysis project internal reporitng system to news POSTGRESQL database. It contains three mothods the popular_articles, popular_authors and the avrage_error.

popular_articles selects the title  and counts the number of views, groups the articles title by comparing the slug column in the articles table  and path column in the log table ignoring the first 10 charector and then orders it by desc.


popular_authors selects the name of the outhor and counts the articles each author has written and number of it views.

	avrage_error method
first I created a two VIEWS TABLES :
1 .create view d2 as (select split_part(time::text,' ',1)d, count(*)  from log group by d);

 which uses split_part to split time column in the log table and tooks only the date of the day and then counts all the status group by day.

2 . create view d1 as (select split_part(time::text,' ',1)d, count(*)  from log where status != '200 OK'  group by d;)

which counts status that is not 200 OK in each day.

secound I calculated the avrage by dividing the d1.count column to d2.count and multiplying it with 100 .



