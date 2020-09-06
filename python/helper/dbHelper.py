class SQLCRUD:

	def create(self, db_connection, query_str):
		try:
			db_connection.execute("create table")
			db_connection.commit()
		except Exception as e:
			return None

	def read(self, db_connection, query_str, query_body=None):
		try:
			if query_body:
				res = db_connection.execute(query_str, [f"%{query_body}%"],)
				return res
			else:
				res = db_connection.execute(query_str)
				return res
		except Exception as e:
			return None

	def update(self, db_connection, query_str):
		try:
			db_connection.execute("insert into db")
			db_connection.commit()
		except Exception as e:
			return None

	def delete(self, db_connection, query_str):
		try:
			db_connection.execute("delete into db")
			db_connection.commit()
		except Exception as e:
			return None





