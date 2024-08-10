import json

from lib import *

global memory1
global memory2
global condition
global todo
global habit_like_extent

info = """
           ...::::::::::...                       
       .:::...          ......                    
    .:::.         .::-----------:.                
  .::.       .:====--:::....:::-==-:.             
 .::.     .-===:.        ..::---=++++=-.          
.::.    .-==:       :-+****+++====+*****+:.       
:::    :==-      :=***=:.         .::..=**#+-.    
:::   .===     :+**-.             .::   -=+***=.  
 ::.  -==:    +**-                ::.   :==:.+**: 
  ::: -==:   +**:               .::.    :==-  +**:
   .:::===  :**+              .::.      ===.  .***
     ..-==- -**=           .:::.       -==:   .***
        .-===***:.....:::::..        :==-.    -**=
          .-=+*#+:..             .:===-.     -**+ 
             .-+#*=-::.::::::--====-.      .+**=  
                :+***+=-----:::.        .-***=.   
                  .-+**+=-:..   ...:-=+***=:      
                      .-=+**********++-:.         

pyMind
Developed By Lyu (2279fc8e)
Version: CONCEPT 1.0.0
"""

logDir = 'Mind'
print(info)


def Mind():
    global memory1
    global memory2
    global condition
    global todo
    global habit_like_extent

    condition = ''
    todo = ''
    habit_like_extent = 0

    opened_json = open(f"./Habit/habits.json", mode="r", encoding="utf-8")
    context = opened_json.read()
    habits_founded = []
    if context != '':
        habits = json.loads(context)
        for i in habits:
            habits_founded += [[i['Condition_Device'], i['Condition'], i['Todo_Device'], i['Todo']]]

    if_finished = 0
    finished_a_habit = 0

    log('pyMind start finding habits...', logDir)
    data_file_list = json_files()
    while True:
        if finished_a_habit == 1:
            finished_a_habit = 0
            if_finished = 0
        for i in data_file_list:
            opened_json = open(f"./Data/{i}", mode="r", encoding="utf-8")
            context = opened_json.read()
            data_context = json.loads(context)
            log(data_context, logDir)
            for j in range(len(data_context)):
                if j == len(data_context) - 1:
                    continue
                memory1 = data_context[j]
                memory2 = data_context[j+1]
                # Format Time
                time1 = datetime.datetime.strptime(memory1['Time'], '%H:%M:%S')
                time2 = datetime.datetime.strptime(memory2['Time'], '%H:%M:%S')
                # Compare whether the time difference between two actions is less than 30 seconds.
                time_difference = time2 - time1
                if time_difference.total_seconds() <= 30:
                    if condition == '' and todo == '':
                        if [memory1['Device'], memory1['Kind']]+[memory2['Device'], memory2['Kind']] in habits_founded:
                            pass
                        else:
                            condition = [memory1['Device'], memory1['Kind']]
                            todo = [memory2['Device'], memory2['Kind']]
                            habit_like_extent = 0
                            if_finished = 1
                            habits_founded += [condition + todo]
                            print([condition + todo])
                            print(habits_founded)
                    elif (condition == [memory1['Device'], memory1['Kind']] and
                          todo == [memory2['Device'], memory2['Kind']]):
                        habit_like_extent += 1
                    if habit_like_extent >= 5:
                        log(f'Found a habit. Condition: {condition}, Todo: {todo}.', logDir)
                        data = json.dumps({'Condition_Device': condition[0], 'Condition': condition[1],
                                           'Todo_Device': todo[0], 'Todo': todo[1]}, sort_keys=True, indent=4,
                                          separators=(',', ': '))
                        make_json(data, "./Habit/habits.json")
                        condition = ''
                        todo = ''
                        habit_like_extent = 0
        condition = ''
        todo = ''
        habit_like_extent = 0
        finished_a_habit = 1
        if if_finished == 0:
            break
