def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

num_subjects = int(input("กรุณาระบุจำนวนวิชา: "))

for i in range(1, num_subjects + 1):
    score = float(input(f"กรุณาระบุคะแนนของวิชาที่ {i}: "))
    grade = calculate_grade(score)
    print(f"เกรดที่ได้จากคะแนน {score} คะแนน ก็คือ {grade}")