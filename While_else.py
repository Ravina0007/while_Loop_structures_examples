command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Welcome in the world of coding.")
print("Execution stopped.")