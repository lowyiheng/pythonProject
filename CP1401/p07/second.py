MINUTES_TO_SECONDS = 60
def main():
    for seconds in range (0 ,3175 + 1 ,635) :
        print(f"{seconds} seconds is {calculate_minute(seconds)}m {calculate_second(seconds)}s ")
    duration_in_second()

def duration_in_second():
    get_seconds = int(input("Favourite duration in seconds :"))
    print(f"You love {calculate_minute(get_seconds)}m {calculate_second(get_seconds)}s ")

def calculate_minute(seconds):
    minutes = seconds // MINUTES_TO_SECONDS
    return minutes

def calculate_second(seconds):
    seconds = seconds % MINUTES_TO_SECONDS
    return seconds

main()


