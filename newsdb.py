#!/usr/bin/env python3
import psycopg2
dbname = 'news'
# this function returns out the top 3 popular articles


def popular_articles():
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    n = c.execute('''
    select title , count(*) as views
    from articles a,log l
    where a.slug = substring (l.path,10)
    group by title
    order by views desc
    limit 3
    ''')
    r = {}
    r = c.fetchall()
    for row in r:
        print('"', row[0], '"', row[1], 'views')
    db.close()

# returns the authors with the most


def popular_authors():
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    n = c.execute('''
    select name, count(*) as views
    from authors, articles , log
    where authors.id= articles.author
    and articles.slug = substring (log.path,10)
    group by name
    order by views desc
    ''')
    output1 = {}
    output1 = c.fetchall()
    for row in output1:
        print('"', row[0], '",', row[1], 'views')
    db.close()
# note I created views  for this quary check
# the README.md file for more details.


def avrage_error():
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    n = c.execute('''
    select d1.d,round((d1.count*100.0/d2.count),3)as percentage from d1, d2
    where d1.d=d2.d
    order by percentage desc
    limit 1''')
    o = c.fetchall()
    print(o)
    db.close()


print('the most popular articles :')
popular_articles()
print('-----------------------------')
print('most popular article authors')
popular_authors()
print('-----------------------------')
print('days did more than 1 percent of requests lead to errors')
avrage_error()
