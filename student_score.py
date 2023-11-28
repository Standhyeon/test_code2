student_tup = (('211101', '조성훈', '010-1234-4500'),
               ('211102', '김은지', '010-2230-6540'),
               ('211103', '윤소정', '010-3232-7788'))

student_tup = {i[0]: [i[1], i[2]] for i in student_tup}

while True:
    student_id = input('학점을 추가하고 싶은 학생의 학번을 입력하세요: (종료를 원하시면 99를 입력하세요)')
    if student_id == '99':
        print('학생의 정보 목록')
        for k, v in student_tup.items():
            print({k: v})
        break
    else:
        if student_id in student_tup:
            grade = float(input(f'{student_id}의 학점을 입력하세요: '))
            student_tup[student_id].append(grade)
        else:
            print(f'{student_id}은 등록되지 않은 학생입니다.')
            break
