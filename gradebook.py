'''
Landon Pack
IS - 303 - A05

Gradebook Program
A program in which tasks can be added, the average can be calculated, the letter grade can be retrieved, 
and the lowest and highest grades can be found

Inputs: No user input; grades are hardcoded

Processes:
Grade- stores a single grade's name, numeric value, and letter grade; can return its name, numeric value, and letter grade
GradeBook - holds a list of Grade objects; can add grades, display all grades, 
            calculate the average of all grades, and find the lowest and highest grade


Outputs:
- A formatted grade list showing the grades and their letter value along with their average, lowest, and highest grade



CLASS: Grade
RESPONSIBILITIES                    | COLLABORATORS
------------------------------------|-------------
Knows its name                      |
Knows its numeric value             |
Knows its letter grade              |

CLASS: GradeBook
RESPONSIBILITIES                         | COLLABORATORS
-----------------------------------------|-------------
Knows all existing grades (the list)     | Grade
Can add a grade                          | Grade
Can display all grades                   | Grade
Can calculate the average of all grades  | Grade
Can find the lowest grade                | Grade
Can find the highest grade               | Grade

    


'''
class Grade:


    def __init__(self, name, numeric_value):
        self.name = name
        self.numeric_value = numeric_value
        self.letter_grade = self.calculate_letter_grade()

    def calculate_letter_grade(self):
        if self.numeric_value >= 90:
            return 'A'
        elif self.numeric_value >= 80:
            return 'B'
        elif self.numeric_value >= 70:
            return 'C'
        elif self.numeric_value >= 60:
            return 'D'
        else:
            return 'F'
        
    def __str__(self):
        return f"{self.name}: {self.numeric_value} ({self.letter_grade})"
    
class GradeBook:

    def __init__(self):
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    

    def display_all_grades(self):
        print(f"----ALL GRADES----")
        for grade in self.grades:
            print(grade)

    def calculate_average(self):
        cumulative_points = 0
        for grade in self.grades:
            cumulative_points += grade.numeric_value

        if len(self.grades) == 0:
            return 0
        
        average = cumulative_points / len(self.grades)
        return average
    
    def find_highest_grade(self):
        highest = None
        for grade in self.grades:
            if highest == None or grade.numeric_value > highest.numeric_value:
                highest = grade

        return highest
    
    def find_lowest_grade(self):
        lowest = None
        for grade in self.grades:
            if lowest == None or grade.numeric_value < lowest.numeric_value:
                lowest = grade

        return lowest
    
    def __str__(self):
        total = len(self.grades)
        avg = self.calculate_average()
        return f"Gradebook: {total} grades | Average: {avg}"


# Main flow
def main():
    
    landon = GradeBook()

    landon.add_grade(Grade("A05 gradebook build", 90))
    landon.add_grade(Grade("A05 task manager build", 100))
    landon.display_all_grades()
    print(f"Average: {landon.calculate_average()}")
    print(f"Highest: {landon.find_highest_grade()}")
    print(f"Lowest: {landon.find_lowest_grade()}")
    print(landon)


main()
