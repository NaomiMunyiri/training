# tuple1=(input("Enter tuple1:"))
# tuple2=(input("Enter tuple2:"))

# if_greater=False

# for i in range (len(tuple1)):
#     if tuple1[i]<=tuple2[i]:
#         if_greater=True
#         print(if_greater)
#     else:
#         print(if_greater)
        


stu_score=int(input("Enter score:"))

if stu_score>=90:
    grade='A'
elif stu_score >=80 and stu_score<90:
    grade='B'
elif stu_score>=70 and stu_score<80:
    grade='C'
elif stu_score>=60 and stu_score<70:
    grade='D'
else:
    grade='F'

print("The grade is",grade)


# exam_score={}
# for i in range(3):
#     subject = input("subject name: ")
#     score = int(input(f"Enter score for {subject}: "))
#     exam_score[subject]=score
# print(exam_score)

# if any(score >=60 for score in exam_score.values()):
#     print(True)
# else:
#     print(False)


