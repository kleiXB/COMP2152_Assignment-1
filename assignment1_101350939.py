"""
Author: <klei mehilli>
Assignment: #1
"""
# Step b: Create 4 variables
gym_member = "Klei Mehilli"
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True
# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (35, 42, 20),
    "Bob": (23, 51, 37),
    "Klei": (48, 35, 60)
}
# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    if not friend.endswith("_Total"):
        total_minutes = sum(workout_stats[friend])
        workout_stats[f"{friend}_Total"] = total_minutes
# Step e: Create a 2D nested list called workout_list
workout_list = []
for friend in ["Alex", "Bob", "Klei"]:
    workout_list.append(list(workout_stats[friend]))
# Step f: Slice the workout_list
yoga_running = [row[0:2] for row in workout_list]
print("Yoga and Running minutes for all friends:")
print(yoga_running)
print()
weightlifting_last_two = [row[2] for row in workout_list[1:3]]
print("Weightlifting minutes for last two friends:")
print(weightlifting_last_two)
print()

# Step g: Check if any friend's total >= 120
print("=== Activity Check ===")
for friend in ["Alex", "Bob", "Klei"]:
    total_key = f"{friend}_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")
print()

# Step h: User input to look up a friend
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

# Step i: Friend with highest and lowest total workout minutes
print("=== Summary Statistics ===")
totals = {}
for friend in ["Alex", "Bob", "Klei"]:
    total_key = f"{friend}_Total"
    totals[friend] = workout_stats[total_key]

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Friend with highest total workout time: {highest_friend} ({totals[highest_friend]} minutes)")
print(f"Friend with lowest total workout time: {lowest_friend} ({totals[lowest_friend]} minutes)")
