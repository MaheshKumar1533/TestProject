from django.shortcuts import render

import random
from otpauth.models import OTP
from django.http import JsonResponse

def send_otp(request):
    phone_number = request.POST.get('phone_number')
    otp_code = str(random.randint(100000, 999999))

    # Save OTP in the database
    OTP.objects.create(phone_number=phone_number, otp_code=otp_code)

    # Send OTP to the phone number (e.g., via SMS)

    return JsonResponse({'message': 'OTP sent successfully'})

def verify_otp(request):
    phone_number = request.POST.get('phone_number')
    entered_otp = request.POST.get('otp')

    otp = OTP.objects.filter(phone_number=phone_number, otp_code=entered_otp).first()

    if otp:
        # OTP is valid
        # Perform your authentication logic here
        return JsonResponse({'message': 'OTP verified successfully'})
    else:
        # Invalid OTP
        return JsonResponse({'message': 'Invalid OTP'})

