import sqlite3
import os 

conn = sqlite3.connect("reviews.sqlite")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS review_db")
c.execute("CREATE TABLE review_db (review TEXT, sentiment INTEGER, date TEXT)")

example1 = "I love this place"
c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME('now'))",(example1,5))

example2 = "I dont like this place much not recommended"
c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME('now'))",(example1,1))

conn.commit()
conn.close()

conn = sqlite3.connect("reviews.sqlite")
c = conn.cursor()

c.execute("SELECT * FROM review_db WHERE date BETWEEN '2020-01-01 10:10:10' AND DATETIME('now')")
results = c.fetchall()

conn.close()

print(results)