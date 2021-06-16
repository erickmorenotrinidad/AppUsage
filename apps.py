import time
import random
apps_usages = {}
app_limits = {'calculator': 2, 'phone': 3, 'messages': 1, 'facebook': 3, 'youtube': 4, 'whatsapp': 2}


def password():


def display_total_time():
    print(apps_usages)

def helper(aplications):
    try:
        apps_usages[applications] = apps_usages[applications] + total_time
    except:
        apps_usages.update({applications: total_time})


def limiting(aplications):
    limit_reached = app_limits[applications] < apps_usages.get(applications, 0)
    if limit_reached:
        print('You have reached your time limit')
        return
    else:
        start_timer = time.perf_counter()
        time.sleep(random.randint(1, 10) / 100)
        end_timer = time.perf_counter()
        total_time = end_timer - start_timer
        total_time = round(total_time, 2)


def calculate_and_track_time(applications):
    limiting()
    helper()

def calculator():
    calculate_and_track_time('calculator')


def phone():
    calculate_and_track_time('phone')


def messages():
    calculate_and_track_time('messages')


def facebook():
    calculate_and_track_time('facebook')


def youtube():
    calculate_and_track_time('youtube')


def whatsapp():
    calculate_and_track_time('whatsapp')
