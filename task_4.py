class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, rest_days, hours=None):
        if hours is None:
            return (7 - rest_days) * 8
        else:
            return hours
        
    @classmethod
    def get_email(cls, name, email=None):
        if email is None:
            return f"{name}@email.com"
        else:
            return email
        
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment

    def salary(self):
        return self.get_hours(self.rest_days, self.hours) * self.hourly_payment