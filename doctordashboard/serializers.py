# from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from doctordashboard.models import Patient, Appointment, Operation, Room, Visit, Form, Employee

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
        
    # def create(self, validated_data):
    #     return Patient.objects.create(validated_data)
    
    
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
  
  
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'      
        

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']
        
        
    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

      
      

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id',  'email', 'username', 'password', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
    
        
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
        
        
        
class VisitSerializer(serializers.ModelSerializer):
    # patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    room = serializers.StringRelatedField()
    operation = serializers.StringRelatedField()
    class Meta:
        model = Visit
        fields = '__all__'
        
# class PatientListView(generics.ListAPIView):
#     serializer_class = VisitSerializer

#     def get_queryset(self):
#         patient = self.kwargs['patient']
#         return Visit.objects.filter(patient=patient)
        
# class PaymentJournalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentJournal
#         fields = '__all__'
        


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Operation
        fields = '__all__'
            

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Room
        fields = '__all__'
        

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Form
        fields = '__all__'
        
        
        
        
# api/serializer.py

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
