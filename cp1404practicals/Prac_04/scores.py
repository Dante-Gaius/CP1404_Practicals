"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    IT101 = []
    IT201 = []
    IT202 = []
    IT301 = []
    IT302 = []
    for score in score_values:
        IT101.append(score[0])
        IT201.append(score[1])
        IT202.append(score[2])
        IT301.append(score[3])
        IT302.append(score[4])
    subject_scores = [IT101, IT201, IT202, IT301, IT302]
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for scores in subject_scores[i]:
            print(scores)
        print("Max:", max(subject_scores[i]))
        print("Min:", min(subject_scores[i]))
        print("Average:", (sum(subject_scores[i]) / len(subject_scores[i])))
        print()


main()
