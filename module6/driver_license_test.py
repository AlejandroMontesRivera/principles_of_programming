# Save correct answers in a list from a file
infile = open('correct_answers', 'r')
corr_ans_list = infile.readlines()
# Close the file
infile.close()
# Save user answers in a list from a file
infile = open('user_answers', 'r')
user_ans_list = infile.readlines()
# Close the file
infile.close()

# Initialize values
incorrect_list = []
correct_ct = 0
num_questions = len(corr_ans_list)

i = 0
while i < num_questions:
    if user_ans_list[i].strip() == corr_ans_list[i].strip():
        correct_ct += 1
    else:
        incorrect_list.append(user_ans_list[i].strip())
    i += 1

if correct_ct >= 15:
    print("Congratulations for passing your driving test!!!")
else:
    print("Sorry, you did not pass the driving test")

print(f"Correct questions: {correct_ct}")
print(f"Incorrect questions: {num_questions - correct_ct}")
print(f"Incorrect questions: {incorrect_list}")
