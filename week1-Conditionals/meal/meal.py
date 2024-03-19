def main():
    # Variables assigned to meals starting and ending times
    breakfast_start = 7.00
    breakfast_end = 8.00
    lunch_start = 12.00
    lunch_end = 13.00
    dinner_start = 18.00
    dinner_end = 19.00

    #Prompts User to input current time
    time = input("What time is it? ").strip().lower()


    if breakfast_start <= convert(time) <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= convert(time) <= lunch_end:
        print("lunch time")
    elif dinner_start <= convert(time) <= dinner_end:
        print("dinner time")


#Converts inputed time by user in to a float, by spliting hours and minutes, then adds up both numbers and returns that number
def convert(time):

    hours, minutes = time.split(":")

    time_f = float(hours) + (float(minutes) / 60)

    return(time_f)

if __name__ == "__main__":
    main()