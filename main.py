import random

from Collector import *

"""
# This is a simple test code that can be easily adjusted
data_encoder("phone","phone_call_in","11:45:14")
data_encoder("tv","tv_volume_turn_down","11:45:30")
"""

info = """
pyMind Tester
It will randomly write the operation records of smart devices.
The content includes noise and randomly occurring habits
(The interval between two operations should not be less than 30 seconds, 
and these two operations should appear together multiple times)
"""

print(info)
operate = [{'phone': 'phone_call_in'}, {'tv': 'tv_volume_turn_down'}, {'tv': 'tv_volume_turn_up'},
           {'light': 'light_off'}, {'light': 'light_on'}, {'music': 'music_play'}]

time_used = [0, 0, 0]


def get_nth_element(dictionary, n, require):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    if n < len(keys):
        key = keys[n]
        value = values[n]
        if require == 0:
            return key
        elif require == 1:
            return value
        else:
            return key, value
    else:
        return None


def random_data():
    global hours
    if hours[0] != hours[1]:
        m = random.randint(0, 59)
    else:
        time_used[0] = hours [1]
        m = random.randint(time_used[1], 59)
    if m != time_used[1]:
        s = random.randint(0, 59)
    else:
        s = random.randint(time_used[2], 59)
    time_random = [hours[1], m, s]
    hours.pop(0)
    return time_random


hours = []
times = random.randint(50, 60)

for j in range(times + 1):
    hours.append(random.randint(0, 23))
    hours.sort()

for i in range(times):
    data = operate[random.randint(0, len(operate) - 1)]
    if_habit = random.randint(1, 6)
    if if_habit > 2:
        time_random = random_data()
        data_encoder(get_nth_element(data, 0, 0), get_nth_element(data, 0, 1),
                     f"{time_random[0]}:{time_random[1]}:{time_random[2]}")
        time_used = time_random
    elif if_habit == 2:
        # Habit: "Condition": "phone_call_in", "Condition_Device": "phone",
        # "Todo": "tv_volume_turn_down", "Todo_Device": "tv"
        time_random = random_data()
        data_encoder(get_nth_element(operate[0], 0, 0), get_nth_element(operate[0], 0, 1),
                     f"{time_random[0]}:{time_random[1]}:{time_random[2]}")
        time_random_time = datetime.datetime.strptime(f"{time_random[0]}:{time_random[1]}:{time_random[2]}", "%H:%M:%S")
        time_random_time_next = time_random_time + datetime.timedelta(seconds=random.randint(1, 29))
        data_encoder(get_nth_element(operate[1], 0, 0), get_nth_element(operate[1], 0, 1),
                     time_random_time_next.strftime("%H:%M:%S"))

    elif if_habit == 1:
        # "Condition": "phone_call_in","Condition_Device": "phone",
        # "Todo": "tv_volume_turn_down","Todo_Device": "tv"
        time_random = random_data()
        data_encoder(get_nth_element(operate[4], 0, 0), get_nth_element(operate[4], 0, 1),
                     f"{time_random[0]}:{time_random[1]}:{time_random[2]}")
        time_random_time = datetime.datetime.strptime(f"{time_random[0]}:{time_random[1]}:{time_random[2]}", "%H:%M:%S")
        time_random_time_next = time_random_time + datetime.timedelta(seconds=random.randint(1, 29))
        data_encoder(get_nth_element(operate[5], 0, 0), get_nth_element(operate[5], 0, 1),
                     time_random_time_next.strftime("%H:%M:%S"))
