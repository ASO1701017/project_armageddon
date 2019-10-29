from armageddon_system.models.form import Form


class PayLog:
    time_stamp = ""
    student_id = 0
    school_id = 0
    school_name = ""
    course_id = 0
    course_name = ""
    form_list: list
    total = 0

    def __init__(self, time_stamp, student_id, school_id, school_name, course_id, course_name, form_list):
        self.time_stamp = time_stamp
        self.student_id = student_id
        self.school_id = school_id
        self.school_name = school_name
        self.course_id = course_id
        self.course_name = course_name
        self.form_list = []
        for l in form_list:
            self.form_list.append(
                {'form': l['form'], 'quantity': l['quantity']}
            )
            # self.total += l['form']['fee'] * l['quantity']
