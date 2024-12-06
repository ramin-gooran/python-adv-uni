import requests 

class Fetcher:
    def __init__(self):
        response = requests.get("https://cdn.ituring.ir/ex/users.json")
        response.raise_for_status()
        self.__students = list(response.json())

    def nerds(self):
        nerds = {
            f"{student['name']} {student['last_name']}"
            for student in self.__students
            if student.get('score', 0) > 18.5
        }
        return nerds
    def sultans(self):
        max_score = 0
        for student in self.__students:
            if student['score'] > max_score:
                max_score = student['score']
        sultans = tuple(
        (student['name'], student['last_name'])
        for student in self.__students
        if student['score'] == max_score
    )
        return sultans
    
    def mean(self):
        sum = 0
        count = 0
        for student in self.__students:
            sum += student['score']
            count += 1
        return sum // count
    
    def get_students(self):
        students = list(
            {
                'name': student['name'],
                'last_name': student['last_name'],
                'height': student['height'],
                'weight': student['weight'],
                'score': student['score'],
                'savings': student['savings'],
                'salary': student['salary'],
            }
            for student in self.__students
        )
        return students
