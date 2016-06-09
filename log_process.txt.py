import datetime
with open('log.txt', 'r') as log_file:
    for line in log_file:
        print(datetime.datetime.now() - datetime.datetime.strptime(line[0:19],'%m/%d/%Y-%H:%M:%S'))