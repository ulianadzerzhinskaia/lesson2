grades = [{'school_class': '4a','scores': ['3,4,4,5,2']},
{'school_class':'4b', 'scores':['3,3,3,4,5']},
{'school_class':'4c', 'scores':['2,2,4,4,4']}]

def average_scores(school):
    sum_grades = 0
    number_of_grades = 0

    for grade in grades:
        sum_grades += sum(grades['scores'])
        number_of_grades +=len(grade['scores'])

    average_school = sum_grades / number_of_grades
    print ('Средний балл по школе {}'.format(average_school))

    for school_class in grades:
        sum_grades +=sum(grades['scores'])
        number_of_pupils = count(grades['scores'])

    average_class = sum_grades/number_of_pupils
    print ('Средний балл по классу {}'.format(average_class))





