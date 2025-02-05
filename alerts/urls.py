from django.contrib import admin
from django.urls import path
from .views import IAMRolesDetail, IAMRolesList, alerts_list, alert_detail , get_alert_by_id , IAMUserList , IamUserDetail
urlpatterns = [
    path('alerts/', alerts_list.as_view() , name="alerts_list"),
    path("alerts/<int:pk>", get_alert_by_id.as_view(), name= "get_alert_by_id" ),
    path("alerts/<str:alert_id>" ,  alert_detail.as_view() , name="alert_detail" ),

    #IAM USER
    path("users",  IAMUserList.as_view() , name="IAMUserList"),
    path("users/<int:pk>",  IamUserDetail.as_view() , name="IamUserDetail"),


    #IAM Role
    path("roles",  IAMRolesList.as_view() , name="IAMRolesList"),
    path("roles/<int:pk>",  IAMRolesDetail.as_view() , name="IAMRolesDetail"),
]