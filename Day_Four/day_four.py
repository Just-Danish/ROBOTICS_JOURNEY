# 🤖 Challenge: Robot Speed Monitor
# Create a Python program that:

# Accepts speed inputs from the user for 5 robots

# Saves those speeds in a list

# Checks each speed using a loop

# Uses if/else statements to classify:

# 🚀 Speed > 1.5 → “Too fast!”

# 🐢 Speed < 0.5 → “Too slow.”

# ✅ Speed between 0.5 and 1.5 → “Optimal speed.”

     
    # 🛠️ Step 1: Start with an empty list to collect robot speeds
robot_speeds = []

# 🧑‍🔬 Step 2: Ask user to enter speeds for 5 robots one by one
for robot_number in range(1, 6):
    speed_input = input(f"🔢 Enter speed for Robot {robot_number}: ")
    
    try:
        # 📏 Convert input to decimal (float) — important for speeds like 0.8 or 1.2
        speed = float(speed_input)
        
        # 📋 Add valid speed to our list for analysis later
        robot_speeds.append(speed)

    except ValueError:
        # ⚠️ If user types letters or invalid numbers
        print("❌ Not a valid number! Please enter a correct speed (like 1.2 or 0.5).")

# 📊 Step 3: Analyze each robot's speed and print what it means
print("\n📡 Robot Speed Summary:")
for index, speed in enumerate(robot_speeds, start=1):

    # 🏎️ Case 1: Speed is too high
    if speed > 1.5:
        print(f"Robot {index} speed = {speed} → 🚀 Too fast! Consider slowing it down.")

    # 🐌 Case 2: Speed is too low
    elif speed < 0.5:
        print(f"Robot {index} speed = {speed} → 🐢 Too slow. Maybe increase the power.")

    # 🧘 Case 3: Speed is just right
    else:
        print(f"Robot {index} speed = {speed} → ✅ Optimal speed. Good job!")




