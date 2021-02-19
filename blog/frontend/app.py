from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
   db = sqlite3.connect('posts.db')
   cursor = db.cursor()
   #cursor.execute('drop table if exists Posts')
   #cursor.execute('CREATE TABLE Posts(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Post TEXT)')
   #cursor.execute('INSERT INTO Posts(Title, Post) VALUES("title", "post")')
   #db.commit()
   #cursor.execute('delete  from Posts ')
   db.commit()
   cursor.execute('SELECT * FROM Posts')
   data = cursor.fetchall()
   db.close()
   
   
   return render_template("posts.html", data = str(data))

@app.route('/create')   
def create():   
   db = sqlite3.connect('posts.db')
   cursor = db.cursor()
   
   Title = request.args.get('Title')
   Post = request.args.get('Post')
   
   cursor.execute('INSERT INTO Posts(Title, Post) VALUES("%s","%s")' % (Title, Post))
   db.commit()
   print(Title, Post)
   
   return 'title:' + str(Title) + '| post:' + str(Post)
   db.close()
@app.route('/update/<_id>')   
def update(_id):   
   db = sqlite3.connect('posts.db')
   cursor = db.cursor()
   
   Title = request.args.get('Title')
   Post = request.args.get('Post')
   
   cursor.execute('update  Posts set Title = "%s", Post = "%s" where id = %s' % (Title, Post,_id))
   db.commit()
   
   return 'update'
   db.close()  

@app.route('/delete/<_id>')  
def delete(_id):   
   db = sqlite3.connect('posts.db')
   cursor = db.cursor()
   
   cursor.execute('delete from  Posts where id = %s' % (_id))
   db.commit()
   
   return 'delete'
   db.close()     
   
   
@app.route('/show')
def show():
   db = sqlite3.connect('posts.db')
   cursor = db.cursor()
   #cursor.execute('CREATE TABLE Posts(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Post TEXT)')
   #cursor.execute('INSERT INTO Posts(Title, Post) VALUES("title", "post")')
   #db.commit()
   #cursor.execute('delete  from Posts ')
   #db.commit()
   cursor.execute('SELECT * FROM Posts')
   data = cursor.fetchall()
   return str(data)
   
   db.close()
   

   
   
   
   
   
if __name__ == '__main__':
   app.run(debug=True, threaded=True)    
