from rest_framework import serializers
from .models import EmpNew
from .models import DeptNew
from datetime import date


class EmployeesSerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()
    dept_name = serializers.SerializerMethodField()

    class Meta:
        model = EmpNew
        fields = ('id', 'name', 'dob', 'department_id', 'age', 'dept_name')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return EmpNew.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.department_id = validated_data.get('department_id', instance.title)
        # instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.department_id = validated_data.get('department_id', instance.department_id)
        instance.save()
        return instance

    def get_age(self, obj):
        today = date.today()
        age = today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))
        return age

    def get_dept_name(self, obj):
        dept = DeptNew.objects.get(pk=obj.department_id.id)
        return dept.name


class DepartmentsSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

    class Meta:
        model = DeptNew
        fields = ('id', 'name', 'description',)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return DeptNew.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.department_id = validated_data.get('department_id', instance.title)
        # instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
