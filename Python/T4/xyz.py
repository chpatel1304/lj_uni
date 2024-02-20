class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.free = True

    def receive_call(self):
        print(f"Call received by {self.name}")
        self.free = False

    def end_call(self):
        print("Call ended")
        self.free = True

    def is_free(self):
        return self.free

    def get_rank(self):
        pass


class Respondent(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.rank = 3

    def get_rank(self):
        return self.rank


class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.rank = 2

    def get_rank(self):
        return self.rank


class Director(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.rank = 1

    def get_rank(self):
        return self.rank


class Call:
    def __init__(self, id, name):
        self.caller_id = id
        self.caller_name = name
        self.assigned = False


class CallHandler:
    respondents = []
    managers = []
    directors = []

    @classmethod
    def add_employee(cls, employee):
        if isinstance(employee, Respondent):
            cls.respondents.append(employee)
        elif isinstance(employee, Manager):
            cls.managers.append(employee)
        elif isinstance(employee, Director):
            cls.directors.append(employee)

    @classmethod
    def dispatch_call(cls, call):
        for employee_list in [cls.respondents, cls.managers, cls.directors]:
            for employee in employee_list:
                if employee.is_free():
                    employee.receive_call()
                    call.assigned = True
                    return
        print("Sorry! All employees are currently busy.")


# Create employees
respondent1 = Respondent(1, "Respondent 1")
respondent2 = Respondent(2, "Respondent 2")
respondent3 = Respondent(3, "Respondent 3")
manager1 = Manager(4, "Manager 1")
manager2 = Manager(5, "Manager 2")
director1 = Director(6, "Director 1")

# Add employees to CallHandler
call_handler = CallHandler()
call_handler.add_employee(respondent1)
call_handler.add_employee(respondent2)
call_handler.add_employee(respondent3)
call_handler.add_employee(manager1)
call_handler.add_employee(manager2)
call_handler.add_employee(director1)

# Create a call and dispatch it
call = Call(7, "John Doe")
call_handler.dispatch_call(call)
