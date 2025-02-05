from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied

class RoleBasedPermission(BasePermission):
    EMAIL_MAPPING_ROLES = {
        "sa@vcs.com": "admin",
        "test@example.com": "viewer"
    }


    def has_permission(self, request, view):
        auth = JWTAuthentication()
        validated_token = auth.get_validated_token(request.headers.get('Authorization').split()[1])
        
        email = validated_token.get('email', "")
        required_roles = view.required_role
        role = self.EMAIL_MAPPING_ROLES.get(email, "viewer")

        if role  in required_roles:
            return True
        raise PermissionDenied("You do not have the required role.")
