# Clear function
britain = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print("britain dictionary")
print(britain)
britain.clear()
print("britain dictionary")
print(britain)

# Copy function
britain = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print("britain dictionary")
print(britain)
britain_copy = britain.copy()
print("britain_copy dictionary")
print(britain_copy)
britain_copy.popitem()
print("britain dictionary")
print(britain)
print("britain_copy dictionary")
print(britain_copy)

# Update function
northern_ireland = {4: "Northern Ireland"}
britain_copy.update(northern_ireland)
print("britain_copy dictionary")
print(britain_copy)
print("Northern Ireland dictionary")
print(northern_ireland)

britain_copy[4] = "Whatever"
print("britain_copy dictionary")
print(britain_copy)
britain_copy.update(northern_ireland)  # updates it back to Northern Ireland
print("britain_copy dictionary")
print(britain_copy)

britain_copy[4] = "Whatever"
print("britain_copy dictionary")
print(britain_copy)
britain_copy.update({})  # nothing gets updated
print("britain_copy dictionary")
print(britain_copy)
