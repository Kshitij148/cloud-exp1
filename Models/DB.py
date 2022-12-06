from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import time
import datetime



class DB(object):
	"""Initialize mysql database """
	host = "localhost"
	user = "root"
	password = "YES"
	db = "lms"
	table = ""

	def __init__(self, app):
		app.config["MYSQL_DATABASE_HOST"] = self.host;
		app.config["MYSQL_DATABASE_USER"] = self.user;
		app.config["MYSQL_DATABASE_PASSWORD"] = self.password;
		app.config["MYSQL_DATABASE_DB"] = self.db;

		self.mysql = MySQL(app, cursorclass=DictCursor)

	def cur(self):
		return self.mysql.get_db().cursor()

	def query(self, q):

		print(q)
		h = self.cur()
	
		if (len(self.table)>0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def query_new(self,name,email,password):
		
		h = self.cur()
		mob=''
		lock=0
		bio='dummy bio'
		id=23
		ts = time.time()
		timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		
		h.execute("insert into users values (%s,%s,%s,%s,%s,%s,%s,%s);",(id,name,email,password,mob,lock,bio,timestamp))

		return h


	def commit(self):
		self.query("COMMIT;")