#nested list containing three students scores
scores = [
    [90,90,90],
    [80,80,80],
    [70,70,70]
]

#empty list to store average scores
avg_score=[]

#iteration over each inner list
for score in scores:
    total=sum(score) #sum of score for student
    avg=total/len(score) #average of score for student
    avg_score.append(avg) #append average to list of average scores 

#loop to print scores for each student
#enumerate takes an iterable ie avg_score and returns a pair of values i.e index starting from 1 and an item from the iterable
for i,j in enumerate(avg_score,start=1): #i holds the index, j holds the average score 
    print(f"Average score for student {i} is {j}")



