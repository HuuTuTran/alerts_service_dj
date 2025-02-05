from rest_framework import generics

from backend.cache import get_or_set_cache
from .pagination import CustomPagination
from .models import IAMRoles, alerts , IAMUsers
from .serializers import AlertSerializer, IAMRolesSerializer, IamUsersSerializer , CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from .authorization import RoleBasedPermission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response

# ListAPIView:
# Use Case: To retrieve a list of objects.
# Methods: Supports GET requests.
# Example: Use when you want to return a collection of items, like a list of books.

# CreateAPIView:
# Use Case: To create a new object.
# Methods: Supports POST requests.
# Example: Use when you want to allow clients to create new book entries.

# RetrieveAPIView:
# Use Case: To retrieve a single object by its ID.
# Methods: Supports GET requests.
# Example: Use when you want to get details of a specific book.

# UpdateAPIView:
# Use Case: To update an existing object.
# Methods: Supports PUT and PATCH requests.
# Example: Use when you want to allow updates to book details.

# DestroyAPIView:
# Use Case: To delete an object.
# Methods: Supports DELETE requests.
# Example: Use when you want to allow the deletion of a book entry.

# ListCreateAPIView:
# Use Case: To retrieve a list of objects and create a new object in the same view.
# Methods: Supports both GET and POST requests.
# Example: Use when you want to return a list of books and also allow creating new books in the same endpoint.

# RetrieveUpdateDestroyAPIView:
# Use Case: To retrieve, update, or delete a single object.
# Methods: Supports GET, PUT, PATCH, and DELETE requests.
# Example: Use when you want to manage a specific book entry with a single view.


class custom_jwt_token(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class alerts_list(generics.ListCreateAPIView):
    try:
        queryset = alerts.objects.all()
        serializer_class = AlertSerializer 
        pagination_class = CustomPagination
        required_role = ["admin"] 
        #IsAuthenticated check if the user is authenticated or not
        #RoleBasedPermission check if the user has the required role or not
        permission_classes = [IsAuthenticated,RoleBasedPermission] 

        def get(self, request):
            # Define a cache key
            cache_key = "alerts_list"
            page  = int(request.query_params.get("page", 1)) 
            limit = int(request.query_params.get("limit", 10))    
            # Function to fetch data from the database
            def fetch_books():
                books = alerts.objects.all()[page * limit: (page + 1) * limit]      
                return AlertSerializer(books, many=True).data

            # Get cached data or fetch and cache it
            data = get_or_set_cache(cache_key, fetch_books, timeout=600)
            
            return Response(data)        
    except Exception as e:
        raise Response("Error in fetching data")


    
class alert_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = alerts.objects.all()
    serializer_class = AlertSerializer 
    lookup_field = "alert_id"
    permission_classes = [IsAuthenticated] 

class get_alert_by_id(generics.RetrieveUpdateDestroyAPIView):
    queryset = alerts.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated] 


class IAMUserList(generics.ListCreateAPIView):
    # queryset = IAMUsers.objects.select_related("role")
    serializer_class = IamUsersSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return IAMUsers.objects.select_related("role")

    

class IamUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IAMUsers.objects.all()
    serializer_class = IamUsersSerializer
    permission_classes = [IsAuthenticated]



class IAMRolesList(generics.ListCreateAPIView):
    queryset = IAMRoles.objects.all()
    serializer_class = IAMRolesSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    
class IAMRolesDetail(generics.RetrieveUpdateDestroyAPIView):            
    queryset = IAMRoles.objects.all()
    serializer_class = IAMRolesSerializer
    # lookup_field = "_id"
    permission_classes = [IsAuthenticated]