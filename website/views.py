from django.shortcuts import HttpResponse, render_to_response
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings


@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'department':
            create_department(request)
        elif request.POST.get('type') == 'department_edit':
            edit_department(request)
        elif request.POST.get('type') == 'employee_edit':
            edit_employee(request)
        elif request.POST.get('type') == 'employee':
            create_employee(request)
        return HttpResponseRedirect(request.path_info)

    emp = get_employees()
    dep = get_departments()

    return render_to_response("website/index.html", {'employees': emp, 'departments': dep})


def edit_department(request):
    _rest_url = settings.REST_URL
    dep = get_dept_by_name(request.POST.get("dept_name"))
    url = f"{_rest_url}/departments/{dep['id']}?format=json"
    params = {"name": request.POST.get("dept_name"), "description": request.POST.get("dept_description"), "id": dep['id']}

    r = requests.put(url, params)
    return HttpResponse(status=201)


def create_department(request):
    _rest_url = settings.REST_URL
    url = f'{_rest_url}/departments/?format=json'
    params = {"name": request.POST.get("dept_name"), "description": request.POST.get("dept_description")}
    r = requests.post(url, json=params)
    return HttpResponse(status=201)


@csrf_exempt
def delete_department(request):
    _rest_url = settings.REST_URL
    dep_id = request.POST.get('dept_id')
    url = f'{_rest_url}/departments/{dep_id}?format=json'
    requests.delete(url)
    return JsonResponse({"status":"Success"})

@csrf_exempt
def delete_employee(request):
    _rest_url = settings.REST_URL
    emp_id = request.POST.get('emp_id')
    url = f'{_rest_url}/employees/{emp_id}?format=json'
    requests.delete(url)
    return JsonResponse({"status": "Success"})


def edit_employee(request):
    _rest_url = settings.REST_URL
    emp = get_emp_by_name(request.POST.get("emp_name"))
    dep = get_dept_by_name(request.POST.get("emp_dept_name"))
    url = f"{_rest_url}/employees/{emp['id']}?format=json"
    params = {"name": request.POST.get("emp_name"), "dob": request.POST.get("emp_dob"),
              "id": emp['id'], "department_id": dep["id"]}

    r = requests.put(url, params)

    return HttpResponse(status=201)


def create_employee(request):
    _rest_url = settings.REST_URL
    url = f'{_rest_url}/employees/?format=json'

    dept = get_dept_by_name(request.POST.get("emp_dept_name"))

    params = {"name": request.POST.get("emp_name"), "dob": request.POST.get("emp_dob"), "department_id": dept["id"]}
    r = requests.post(url, json=params)
    return HttpResponse(status=201)


def get_dept_by_name(name):
    _rest_url = settings.REST_URL
    url = f'{_rest_url}/departments/?format=json&name={name}'
    r = requests.get(url)
    return r.json()


def get_emp_by_name(name):
    _rest_url = settings.REST_URL
    url = f'{_rest_url}/employees/?format=json&name={name}'
    r = requests.get(url)
    return r.json()


def get_departments():
    _rest_url = settings.REST_URL
    url = f'{_rest_url}/departments/?format=json'
    params = None
    r = requests.get(url, params=params)
    return r.json()


def get_employees():
    _rest_url = settings.REST_URL
    url = f'{_rest_url}/employees/?format=json'
    params = None
    r = requests.get(url, params=params)
    return r.json()

