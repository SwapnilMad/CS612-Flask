from flask import redirect,Flask, render_template, request
import requests

app = Flask(__name__)
url='http://localhost:8000'
@app.route('/')
def get_employee_list():
    data = requests.get(url=url+'/employee').json()
    return render_template('/employee.html',result=data)

@app.route('/add',methods = ['POST', 'GET'])
def result():
   if request.method == 'GET':
      return render_template("AddEmp.html")
   else:
       data = request.form
       requests.post(url=url+'/employee',json={"id":data['id'],"Name":data['name'],"Salary":data['salary'],"City":data['city']})
       return redirect('/')

@app.route('/delete/<string:empid>')
def remove(empid):
    requests.delete(url=url+'/employee/'+empid)
    return redirect('/')

@app.route('/update',methods=['POST'])
def update():
    data=request.form
    requests.put(url=url+'/employee/'+data['id'],json={"id":data['id'],"Name":data['name'],"Salary":data['salary'],"City":data['city']})
    return redirect('/')

@app.route('/employee/<string:empid>')
def get_employee(empid):
    data = requests.get(url=url + '/employee/'+empid).json()
    return render_template('/update.html',result=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)