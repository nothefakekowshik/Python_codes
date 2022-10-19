class parent:
    def parent_display():
        print("in the parents")

class student(parent):
    def display(self):
        print("in the student")
        print("going to parent")
        parent.parent_display()

student_obj=student()
student_obj.display()