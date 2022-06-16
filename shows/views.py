import django
django.setup()
import uuid, datetime
from multiprocessing import Pool
from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from rest_framework import generics, response
from django.contrib.auth.models import User
from django.views import View
from rest_framework.views import APIView
from shows.serializers import UserSerializer, ScreensSerializer, BookingsSerializer, BookingsSerializerPost
from shows.models import Screens, Bookings
from shows.smtpgateway import sendmailoversmtp

# Create your views here.

def index(request):
    "the default page for the app"
    return render(request, "index.html", {})


class UsersAPI(generics.ListAPIView):
    "to display list of users available"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShowsAPI(generics.ListAPIView):
    "to display list of available shows"
    queryset = Screens.objects.all()
    serializer_class = ScreensSerializer

class BookingsAPI(generics.ListAPIView):
    "to display list of bookings made"
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

class NewScreenAPI(generics.CreateAPIView):
    "to create new data for movie screens"
    queryset = Screens.objects.all()
    serializer_class = ScreensSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) 

def create_booking(user, email, mobile, show_booked):
    booking_id = uuid.uuid4()
    book = Bookings(
        booking_id = booking_id,
        user = user,
        email = email,
        mobile = mobile,
        show_booked_id = show_booked
    )
    book.save()

def send_email(email):
    sendmailoversmtp(email,"Show Booked","Your show has been booked")     


class NewBooking(APIView):
    "to create a new booking for a movie show" 
    queryset = Bookings.objects.values('email','mobile','show_booked')
    serializer_class = BookingsSerializerPost
    def get(self, request):
        return JsonResponse({'message':'only POST method supported'})
    def post(self, request):
        user = request.user
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        show_booked = request.POST.get('show_booked')
        if user is None:
            user = email
        create_booking(user, email, mobile, show_booked)
        return JsonResponse({'message':'Booking created successfully'})


class BookingForm(View):
    "to display booking form"
    def get(self, request):
        movies = Screens.objects.values('id', 'multiplex', 'movie_name', 'show_timing', 'city')
        return render(request, "bookingform.html", {'movies':movies})
    def post(self, request):
        user = request.user
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        show_booked = request.POST.get('show_booked')
        if user is None:
            user = email
        create_booking(user, email, mobile, show_booked)
        return JsonResponse({'message':'Booking created successfully'}) 


class SendEmailAPI(View):
    "to send email who have booked the shows" 
    def get(self, request):
        today = datetime.datetime.now()
        book = Bookings.objects.filter(time_booked__lte=today).values('email')
        emails_list = []
        for x in book:
            emails_list += [x['email']]
        print(emails_list) 
        try:   
            pool = Pool(processes=4)
            pool.map(send_email, emails_list)
        except:
            pass    
        return JsonResponse({'message':'Emails sent successfully'})

            


    

