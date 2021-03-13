students = dict()
list_of_grade = []
def course_grade():
    for index in range(5):
        students[index] = {}
        mid_term = int(input("Enter Mid Term Grade: "))
        project = int(input("Enter Project Grade: "))
        final = int(input("Enter Final Grade: "))
        passing_grade(index,mid_term,project,final)
        students[index]["mid_term"] = mid_term
        students[index]["project"] = project
        students[index]["final"] = final
    sorting()

def passing_grade(index,mid_term,project,final):
    passing_grade = mid_term * 0.3 + project * 0.3 + final * 0.4
    list_of_grade.insert(index,passing_grade)

def sorting():
    list_of_grade.sort(reverse = True)

if __name__ == '__main__':
    course_grade()
    print(list_of_grade)
