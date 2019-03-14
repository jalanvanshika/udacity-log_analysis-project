import psycopg2

DBNAME = "news"

ques1 = "What are the most popular 3 articles?"
query1 = "select title, views from view_count order by views desc limit 3;"

ques2 = "Who are the most popular authors of all time?"
query2 = "select authors.name, sum(view_count.views) as views from authors join view_count on authors.id=view_count.author group by  authors.name order by views desc;"

ques3 = "Days when more than 1% of requests lead to errors are?"
query3 = "select * from error where \"percent error\">1;"

"""Connecing databasewith Python DB-API to get the results by defining get_result method"""

print 


def connect(DBNAME):
    try:
        db = psycopg2.connect("dbname={}".format(DBNAME))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to the database"
        sys.exit(1)


def get_result(query):
    db, c = connect(DBNAME)
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


""" Methods to print the query result"""


def print_result(result):
    for i in result:
        print("%s --> %d" % (i[0], i[1]) + ' views')
    print

def print_error(result):
    for i in result3:
        print(str(i[0]) + " --> " + str(i[1]) + ' %')




if __name__ == '__main__':
    """ Calling get_result method and storing the results of respective queries"""

    result1 = get_result(query1)
    result2 = get_result(query2)
    result3 = get_result(query3)

    """Printing the results by calling print_result method"""
    print(ques1)
    print_result(result1)

    print(ques2)
    print_result(result2)

    print(ques3)
    print_error(result3)
