from rest_framework.response import Response
from rest_framework.decorators import api_view
import re
import binascii, hashlib
from lab16.models import *
import django.db.utils

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
    if re.match(pattern, email):
        return True
    return False

def check_fullname(lastname, firstname, patronym):
    pattern = r'[А-Я]{1}[а-я]+'

    FIO = [lastname, firstname, patronym]
    count= 0
    for name in FIO:
       if re.match(pattern, name):
           count += 1

    if count == 3:
       return True
    else: 
        return False

@api_view(['POST'])  #Register user in system
def RegUser(request):
    email = request.data['email']
    lastname = request.data['lastname']
    firstname = request.data['firstname']
    patronym = request.data['patronym']
    password = request.data['password']
    double_password = request.data['double_password']

    if not check_email(email):
        return Response({
            'Incorect_format': 'Inccorect email!'
        })
    
    if not check_fullname(lastname, firstname, patronym):
        return Response({
            'Incorect_format': 'Inccorect lastname, firstname or patronym!'
        })

    if password != double_password:
        return Response({
            'msg': 'Неправильный повторный ввод пароля'
        })
    
    
    password = hashlib.pbkdf2_hmac(hash_name='sha256',
                                   password=password.encode(),
                                   salt=b'bad_salt',
                                    iterations=100000)
    password = str(binascii.hexlify(password))

    try:
        Users.objects.create(
            email = email,
            lastname = lastname,
            firstname = firstname,
            patronym = patronym,
            password = password
        )
    except django.db.utils.IntegrityError:
        return Response({
            'msg': 'Адрес почты уже используется, пожалуйста, используйте другой!'
        })


    return Response({
        'msg': 'Create new user!'
    })



