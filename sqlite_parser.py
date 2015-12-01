import sqlite3
import sys
import os


#USAGE: Run code on cmd line with filename argument

class sqlite_parser:
	
	file_location = 'C:\\YOUR\\PATH\\HERE\\'
	filepath = ''
	table_name = ''


	def __init__(self, filename = 'reading_sqlite', table_name = 'reading_information'):
		self.filepath = "%s%s.sqlite" % (self.file_location, filename)
		self.table_name = table_name
		print "Reading file: %s" % (self.filepath)

	def create_connection(self): 


		if(os.path.exists(self.filepath)) :
			conn = sqlite3.connect(self.filepath);

			with conn: 
				cur = conn.cursor();
				cur.execute("SELECT * FROM %s" % (self.table_name))
				rows = cur.fetchall()
				for row in rows:
					print row
		else: 
			print "Path not exist"



if __name__ == "__main__":
	parser = sqlite_parser(sys.argv[1])
	parser.create_connection()