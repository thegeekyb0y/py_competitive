if __name__ == '__main__':
    students=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    sorted_scores=sorted(list(set(scores)))
    second_lowest_score=sorted_scores[1]
    sorted_students=sorted(students)
    for x in sorted_students:
        if x[1]==second_lowest_score:
            print(x[0])
    
    
    