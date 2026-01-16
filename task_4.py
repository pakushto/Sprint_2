class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, rest_days, hours, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, hours=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        if email is None: # Если email не передан, вызываем get_email
            return cls.get_email(name, rest_days, hours, email)
        else:
            return cls(name, rest_days, hours, email)

    @classmethod
    def get_email(cls, name, rest_days, hours=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        if hours is None: # Если hours не передан, вызываем get_hours
            return cls.get_hours(name, rest_days, hours, email)
        else:
            return cls(name, rest_days, hours, email)
    
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment

    def salary(self):
        return self.hours * self.hourly_payment