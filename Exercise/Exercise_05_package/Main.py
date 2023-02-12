import random

import People


def stdtec_list(job1, name1, gender1, addr1, grade1, room1, subject1, num: int):
    stdlist = []
    teclist = []

    while True:

        if len(stdlist) >= 10 and len(teclist) >= 10:
            break

        r_job = job1[random.randint(0, len(job1)-1)]
        r_name = name1[random.randint(0, len(name1)-1)]
        r_gender = gender1[random.randint(0, len(gender1)-1)]
        r_addr = addr1[random.randint(0, len(addr1)-1)]
        r_grade = grade1[random.randint(0, len(grade1)-1)]
        r_room = room1[random.randint(0, len(room1)-1)]
        r_subject = subject1[random.randint(0, len(subject1)-1)]

        if r_job == '학생':
            stdlist.append(People.Student(r_job, r_name, r_gender, r_addr, r_grade, r_room))
        else:
            teclist.append(People.Teacher(r_job, r_name, r_gender, r_addr, r_subject))

    return stdlist, teclist


if __name__ == '__main__':
    name = ['홍길동', '김길동', '박길동', '이길동', '최길동']
    gender = ['남', '여']
    addr = ['서울', '대전', '대구', '부산', '인천']

    grade = ['1학년', '2학년', '3학년']
    room = ['1반', '2반', '3반']

    job = ['학생', '교사']

    subject = ['국어', '영어', '수학', '체육']

    std_list, tec_list = stdtec_list(job, name, gender, addr, grade, room, subject, 30)

    for i in range(len(std_list)):
        print(f'학생 {i+1}')
        std_list[i].print_pinfo()
        print('--------------------')

    for i in range(len(tec_list)):
        print(f'선생님 {i+1}')
        tec_list[i].print_pinfo()
        print('--------------------')
