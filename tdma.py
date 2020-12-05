from typing import List

number_of_users: int = int(input("Enter the number of users in the system?\n"))
user_delay: List[int] = []
is_channel_allocated: List[int] = []

for index, _ in enumerate(range(number_of_users)):
    delay: int = int(input(f"Enter delay for user {index+1}:\t"))
    user_delay.append(delay)
    is_channel_allocated.append(False)

# num_cycles is chosen at random. Run for absolutely as many cycles as you like.
current_cycle: int = 1
num_cycles: int = 2

# 10 here is arbitrarily decided cycle time. Change as you wish.
cycle_time: int = 10

while current_cycle <= num_cycles:
    print(f"Cycle {current_cycle} is active now:")

    time_elapsed: int = 0
    time_slot_size: int = 400

    for index, user in enumerate(range(number_of_users)):

        if user_delay[index] < cycle_time and not is_channel_allocated[index]:
            is_channel_allocated[index] = True
            print(
                f"\tChannel {index} is allocated slot {time_elapsed} to {time_elapsed+time_slot_size} ")
            time_elapsed = time_elapsed + time_slot_size
        else:
            print(f"\tChannel {index} is idle")
            user_delay[index] = user_delay[index] % cycle_time
    print(f"Cycle {current_cycle} has completed")
    current_cycle += 1
