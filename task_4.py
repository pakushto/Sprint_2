class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            return (7 - self.rest_days) * 8
        else:
            return self.hours
        
    def get_email(self):
        if self.email is None:
            return f"{self.name}@email.com"
        else:
            return self.email
        
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment

    def salary(self):
        return self.hours * self.hourly_payment