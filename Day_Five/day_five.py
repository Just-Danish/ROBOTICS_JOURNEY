# Container dictionary: container number ➡ size
container_list = {
    "MEDU1197371": "40",
    "CBHU5822943": "20",
    "CCLU3680048": "40",
    "GESU3582471": "40",
    "U1197371": "20"
}

# Counters for each size
size_20 = 0
size_40 = 0

# Loop through container sizes and count
for size in container_list.values():
    if size == "20":
        size_20 += 1
    elif size == "40":
        size_40 += 1

# Print summary
print("📦 Container Size Summary:")
print(f"20ft Containers: {size_20}")
print(f"40ft Containers: {size_40}")

