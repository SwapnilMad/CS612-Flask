from flask import Flask,redirect, request
from EmployeeService import Service
import json
app=Flask(__name__)
service = Service()

@app.route('/employee/<string:empid>',methods=['GET','DELETE','PUT'])
def get_employee(empid):
    if request.method=='GET':
        return json.dumps(service.get_employee(empid))
    elif request.method=='DELETE':
        service.remove_employee(empid)
    elif request.method=='PUT':
        service.update_employee(empid,request.get_json())
    return 'updated'

@app.route('/employee',methods=['GET','POST'])
def get_employees():
    if request.method=='POST':
        service.add_employee(request.get_json())
    return json.dumps(service.get_employees())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
