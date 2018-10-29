import pyrebase
import RPi.GPIO as GPIO
import time
import const

GPIO.setmode(GPIO.BOARD)
GPIO.setup(const.FIRST_ROOM, GPIO.OUT)
GPIO.setup(const.SECOND_ROOM, GPIO.OUT)
GPIO.setup(const.THIRD_ROOM, GPIO.OUT)
GPIO.setup(const.FOURTH_ROOM, GPIO.OUT)

def stream_event_swicth_one(message):
    switch_event(FIRST_ROOM, strtobool(message["data"]))

def stream_event_swicth_two(message):
    switch_event(SECOND_ROOM, strtobool(message["data"]))

def stream_event_swicth_tree(message):
    switch_event(THIRD_ROOM, strtobool(message["data"]))

def stream_event_swicth_four(message):
    switch_event(FOURTH_ROOM, strtobool(message["data"]))

def swicth_event(number_swicth, value):
    GPIO.output(number_swicth, value)


config = {
  "apiKey": "remotetestpi-demo",
  "authDomain": "remotetestpi.main.com.remotetestpi",
  "databaseURL": "https://remotetestpi.firebaseio.com/",
  "storageBucket": "gs://remotetestpi.appspot.com/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
auth.create_user_with_email_and_password("email", "password")
auth.sign_in_with_email_and_password("email", "password")
user = auth.sign_in_with_email_and_password()


db = firebase.database()

db.child("switch/PRIMERA_HABITACION").stream(stream_event_swicth_one)
db.child("switchs/SWITCH_SEGUNDO_CUARTO/estado").stream(stream_event_swicth_two)
db.child("switchs/SWITCH_TERCER_CUARTO/estado").stream(stream_event_swicth_tree)
db.child("switchs/SWITCH_SALA/estado").stream(stream_event_swicth_four)
