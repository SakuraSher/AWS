import time

def cpu_consumption(duration=30, cpu_percentage=80):
    start_time = time.time()
    #calculate the number of iterations
    target_percent = cpu_percentage/100
    total_iteration = int(target_percent * 1000000)

    for _ in range(total_iteration):
        result =0
        for i in range(1,100):
            result +=1
        
    elapsed_time = time.time() - start_time
    time_remaining = duration - elapsed_time
    if time_remaining > 0:
        time.sleep(time_remaining)

    print(f"CPU consumption completed in {duration} seconds")

if __name__ ==   "__main__":
    cpu_consumption(duration=30, cpu_percentage=80)
    