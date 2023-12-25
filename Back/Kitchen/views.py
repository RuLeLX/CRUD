from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import binascii, hashlib
from lab16.models import *
import lab16.models
from lab16.serializers import *
import jwt
from Kitchen.models import *
import django.db.utils

@api_view(['POST'])  #Auth user in system
def AuthUser(request):
    
    email = request.data['email']
    password = request.data['password']
    password = hashlib.pbkdf2_hmac(hash_name='sha256',
                                    password=password.encode(),
                                    salt=b'bad_salt',
                                        iterations=100000)
    password = str(binascii.hexlify(password))
   
    try:
        user = Users.objects.get(email=email, password=password)
        user = UserSerializer(user)
    except lab16.models.Users.DoesNotExist:
        return Response({
            'msg': 'Некорректный email или пароль!'
        })

    payload = user.data
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response

@api_view(['POST'])
def CreateCooker(request):
    id_cooker = request.data['id_cooker']
    lastname = request.data['lastname']
    firstname = request.data['firstname']
    patronym = request.data['patronym']
    specials = request.data['specials']

    try:
        Cooker.objects.create(
            id_cooker = id_cooker,
            lastname = lastname,
            firstname = firstname,
            patronym = patronym,
            specials = specials
        )
    except django.db.utils.IntegrityError:
        return Response({
            'msg': 'Повар с таким id существует!'
        })
    return Response({
        'msg': 'Add a new cooker!',
        'data_cooker': [
            id_cooker,
            lastname,
            firstname,
            patronym,
            specials
        ]
    })

    