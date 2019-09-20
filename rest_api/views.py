from rest_framework.views import APIView
from .models import EmpNew
from .models import DeptNew
from .serializer import DepartmentsSerializer
from .serializer import EmployeesSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class DepartmentsNewList(APIView):

    def get_object(self, pk):
        try:
            return DeptNew.objects.get(pk=pk)
        except DeptNew.DoesNotExist:
            raise Http404

    def get(self, request):
        name = request.GET.get("name")
        if name is not None:
            dep = DeptNew.objects.get(name=name)
            ser = DepartmentsSerializer(dep)
        else:
            # emp = EmployeesNew.objects.all()
            dep = DeptNew.objects.all()
            ser = DepartmentsSerializer(dep, many=True)
        return Response(ser.data)

    def post(self, request):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        dept = self.get_object(pk)

        serializer = DepartmentsSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dept = self.get_object(pk)
        dept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesNewList(APIView):

    def get_object(self, pk):
        try:
            return EmpNew.objects.get(pk=pk)
        except EmpNew.DoesNotExist:
            raise Http404

    def get(self, request):
        # emp = EmployeesNew.objects.all()

        name = request.GET.get("name")
        if name is not None:
            emp = EmpNew.objects.get(name=name)
            ser = EmployeesSerializer(emp)
        else:
            # emp = EmployeesNew.objects.all()
            emp = EmpNew.objects.all()
            ser = EmployeesSerializer(emp, many=True)
        return Response(ser.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        emp = self.get_object(pk)
        serializer = EmployeesSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = self.get_object(pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

