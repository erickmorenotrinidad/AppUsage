import time
import random
apps_usages = {}
app_limits = {'calculator': .1, 'phone': .1, 'messages': .1, 'facebook': .1, 'youtube': .1, 'whatsapp': .1}
default_password = 123


def password(aplication):
    user_response = input(f'You have reached the time limit of {aplication}.To reset enter a passcode.')
    if default_password == int(user_response):
        apps_usages[aplication] = 0
    else:
        print('incorect password, no changes made')


def update_total_time(aplications, total_time):
    try:
        apps_usages[aplications] = apps_usages[aplications] + total_time
    except:
        apps_usages.update({aplications: total_time})


def limiting(aplications):
    limit_reached = app_limits[aplications] < apps_usages.get(aplications, 0)
    if limit_reached:
        password(aplications)
        return 0
    else:
        start_timer = time.perf_counter()
        time.sleep(random.randint(1, 10) / 100)
        end_timer = time.perf_counter()
        total_time = end_timer - start_timer
        return round(total_time, 2)


def calculate_and_track_time(applications):
    total_time = limiting(applications)
    update_total_time(applications, total_time)

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
