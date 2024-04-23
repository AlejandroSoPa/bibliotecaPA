from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print(email," ", password)
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            print(user)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("Usuario inactivo.")
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            else:
                raise serializers.ValidationError("Credenciales incorrectas.")
        else:
            raise serializers.ValidationError("Se requieren tanto el correo electrónico como la contraseña.")

