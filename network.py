from datetime import datetime

def get_stats(file_name):
    request_stats = {}
    with open(file_name) as f:
        f = f.readlines()
    for line in f:
        if line.startswith('['):
            #getting date from the log line
            date = line[line.find("[")+1 : line.find("]")]
            #converting that string date to a datetime format
            date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S %z')
            #formatting time for our tracking needs
            request_time = date.strftime('%Y-%m-%d %H:%M')
            if request_time in request_stats:
                request_stats[request_time] = request_stats[request_time]+1
            else:
                request_stats[request_time] = 1    
    print("Time       Request Per/Minute")
    for time, value in request_stats.items():
        print(time ,"    ",value , end=' \n')        
            
file_name  = str(input('Enter file name : '))
get_stats(file_name)