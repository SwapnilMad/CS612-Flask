from tinydb import TinyDB, Query,where

db = TinyDB('db.json')
emp = Query()

class Service:

    def get_employee(self,empid):
        return db.search(emp.id==empid)

    def get_employees(self):
        return db.all()

    def add_employee(self,data):
        db.insert(data)

    def remove_employee(self,empid):
        db.remove(emp.id==empid)

    def update_employee(self,empid,data):
        db.update(data,where('id')==empid)