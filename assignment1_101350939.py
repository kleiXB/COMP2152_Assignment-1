"""
Author: <YOUR REAL FIRST AND LAST NAME>
Assignment: #1
"""

# Variable: String
gym_member = "Alex Alliton"

# Variable: Float
preferred_weight_kg = 20.5

# Variable: Integer
highest_reps = 25

# Variable: Boolean
membership_active = True

# Dictionary: key-value pairs with string keys and tuple values (containing integers)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 30),
    "Taylor": (40, 35, 25)
}

# Calculate total workout minutes for each friend and add to dictionary
for friend in list(workout_stats.keys()):
    if not friend.endswith("_Total"):
        total_minutes = sum(workout_stats[friend])
        workout_stats[f"{friend}_Total"] = total_minutes

# 2-dimensional list (nested list): list containing lists of integers
workout_list = []
for friend in ["Alex", "Jamie", "Taylor"]:
    workout_list.append(list(workout_stats[friend]))

print("=== Workout List (2D nested list) ===")
print(workout_list)
print()

# Slice workout_list: yoga and running for all friends (columns 0 and 1)
yoga_running = [row[0:2] for row in workout_list]
print("Yoga and Running minutes for all friends:")
print(yoga_running)
print()

# Slice workout_list: weightlifting for last two friends (column 2, rows 1 and 2)
weightlifting_last_two = [row[2] for row in workout_list[1:3]]
print("Weightlifting minutes for last two friends:")
print(weightlifting_last_two)
print()

# Check if any friend's total workout minutes >= 120
print("=== Activity Check ===")
for friend in ["Alex", "Jamie", "Taylor"]:
    total_key = f"{friend}_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")
print()

# User input for friend's name lookup
print("=== Friend Lookup ===")
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    activities = workout_stats[friend_name]
    total_key = f"{friend_name}_Total"
    total = workout_stats[total_key]
    print(f"\nWorkout details for {friend_name}:")
    print(f"  Yoga: {activities[0]} minutes")
    print(f"  Running: {activities[1]} minutes")
    print(f"  Weightlifting: {activities[2]} minutes")
    print(f"  Total: {total} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")

print()

# Find friend with highest and lowest total workout minutes
print("=== Summary Statistics ===")
totals = {}
for friend in ["Alex", "Jamie", "Taylor"]:
    total_key = f"{friend}_Total"
    totals[friend] = workout_stats[total_key]

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Friend with highest total workout minutes: {highest_friend} ({totals[highest_friend]} minutes)")
print(f"Friend with lowest total workout minutes: {lowest_friend} ({totals[lowest_friend]} minutes)")