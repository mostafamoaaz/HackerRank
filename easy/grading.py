def gradingStudents(grades):
    for g in range(len(grades)):
        if grades[g] > 37:
            i = grades[g] // 5
            ii = grades[g] % 5
            if ii > 2 :
                grades[g] = i*5 + 5
    return grades



g = [36,37,38,81,82,83,84,85]

gg = gradingStudents(g)
print(gg)