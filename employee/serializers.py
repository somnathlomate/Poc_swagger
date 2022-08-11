from rest_framework.serializers import ModelSerializer
from employee.models import Employee
#from rest_framework import serializers

class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'          # all fields will be serialized     [JSON madhe]
        #include = ('id','name','age')   # only mentioned fields will be serialized[JSON madhe]
        #exclude = ('id','name','age')   # excluding these fields all other fields from that model will be serialized
