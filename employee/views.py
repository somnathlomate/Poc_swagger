from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin


class MyOwnViewSet(GenericViewSet, RetrieveModelMixin, DestroyModelMixin):
    pass


from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny


class EmployeeOperations(ModelViewSet):  # EmployeeOperations -->`create()`, `retrieve()`, `update()`,`partial_update()`, `destroy()` and `list()`
    permission_classes = (AllowAny,)  # all 6 methods are open
    queryset = Employee.objects.all()  # to retrive all the records
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.action in ["list"]:  # out of which --> list,create --> requires --> token  --> only list-->
            self.permission_classes = (IsAuthenticated,)
        # else:
        #    return super().get_permissions()
        return super().get_permissions()


# class EmployeeOperations(ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get_permissions(self):
#         if self.action in ['create','destroy']:
#             self.permission_classes = (IsAuthenticated,)
#         return super().get_permissions()


'''
class EmployeeOperations(ModelViewSet):
    queryset = Employee.objects.all() # to retrive all the records
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        print('----',request.data,'----')
        # if type(request.data) == list:
        #     for empdata in request.data:
        return super().create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        print('-----------Custom Patch Method--------------------')
        print(kwargs,args,request)
        print(request.data)
       #kwargs['partial'] = True
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.role = request.data.get("role")
        instance.save()
        return self.update(request, *args, **kwargs)
        return HttpResponse("Employee Record Partially Updated..!")
'''
