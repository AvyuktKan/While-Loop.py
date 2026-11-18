total_chores = 4
original_chores = total_chores
print("You have", original_chores, "chores to finish today.")

completed_chores = 0
chore_num = 1  

while completed_chores <= total_chores:
    if chore_num == 1: next_chore = "Make your Bed"
    elif chore_num == 2: next_chore = "Do the Laundry"
    elif chore_num == 3: next_chore = "Clean your Room"
    else: next_chore = "Tidy up the Living Room"
    answer = input("Have you completed the chore: " + next_chore + "? (yes/no) ")
    if answer == "yes":
        completed_chores += 1
        chore_num += 1
        print("Great job! You have completed", completed_chores, "out of", original_chores, "chores.")
    else:
        print("No worries! You still have", original_chores - completed_chores, "chores to complete.")

print("Congratulations! You have completed all your chores for today.")

test_value = 0
safety_counter = 0
while test_value <= 0:
    safety_counter += 1
    if safety_counter == 3:
        print("Safety limit reached.")
        break
print("Checklist Summary: You completed", completed_chores, "chores out of", original_chores, "total chores.")
