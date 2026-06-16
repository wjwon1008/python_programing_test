# utils.py -- 성적 분석 함수 모음
#   (함수 이름과 매개변수는 바꾸지 마세요. 내용만 고치세요.)
#   ※ 각 함수가 정확히 어떻게 동작해야 하는지는 '문제지(정상 동작 명세)'를 따르세요.

GPA_TABLE = {"A": 4.5, "B": 4.0, "C": 3.0, "D": 2.0, "F": 0.0}


def total_score(student):
    """학생의 총점."""
    return student["국어"] + student["영어"] + student["수학"]


def average_score(student):
    """학생의 평균."""
    return total_score(student) / 3


def to_grade(avg):
    """평균을 학점으로 변환."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_to_gpa(grade):
    """학점을 평점으로 변환."""
    return GPA_TABLE[grade]


def subject_average(students, subject):
    """과목 평균."""
    total = 0
    for stu in students:
        total += stu[subject]
    return total / len(students)


def subject_top(students, subject):
    """과목 최고점."""
    top = 0
    for stu in students:
        if stu[subject] > top:
            top = stu[subject]
    return top


def grade_distribution(students):
    """학점별 인원."""
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for stu in students:
        g = to_grade(average_score(stu))
        dist[g] += 1
    return dist


def rank_list(students):
    """총점 기준 정렬."""
    return sorted(students, key=lambda s: total_score(s), reverse=True)


def pass_rate(students, cutoff=60):
    """합격 비율(%)."""
    count = 0
    for stu in students:
        if average_score(stu) >= cutoff:
            count += 1
    return count / len(students) * 100
