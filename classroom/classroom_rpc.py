###
# Classroom RPC Services

from nameko.rpc import rpc
import sqlite3


class DBConnection:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cursor = self.con.cursor()

    def __del__(self):
        self.con.close()


class ClassroomService:
    name = "classroom_service"
    db = DBConnection("classroom.db")

    @rpc
    def get_dates(self):
        query = "SELECT DISTINCT date FROM classroom;"
        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()
        return [r[0] for r in results]

    @rpc
    def get_attendence(self, date):
        query = "SELECT * FROM classroom WHERE date=?"
        self.db.cursor.execute(query, (date,) )
        results = self.db.cursor.fetchall()
        return results

