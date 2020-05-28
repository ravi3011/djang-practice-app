from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def emp_data_view(request):
    emp_data = {
        'eno':100,
        'ename':'Sunny',
        'esal':1000,
        'eaddr':'Mumbai',
    }
    resp = 'Employee Number:{}Employee Name:{}Employee Salary:{}Employee Address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json

def emp_data_jsonview(request):
    emp_data = {
        'eno':100,
        'ename':'Sunny',
        'esal':1000,
        'eaddr':'Mumbai',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')
