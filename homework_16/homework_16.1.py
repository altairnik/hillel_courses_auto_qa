class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def test_team_lead_attributes():
    team_lead = TeamLead(name="John Doe", salary=120000, department="IT", programming_language="Python", team_size=5)

    assert hasattr(team_lead, 'name') and team_lead.name == "John Doe", "TeamLead не має правильного атрибуту 'name'"
    assert hasattr(team_lead, 'salary') and team_lead.salary == 120000, "TeamLead не має правильного атрибуту 'salary'"
    assert hasattr(team_lead, 'department') and team_lead.department == "IT", "TeamLead не має правильного атрибуту 'department'"
    assert hasattr(team_lead, 'programming_language') and team_lead.programming_language == "Python", "TeamLead не має правильного атрибуту 'programming_language'"
    assert hasattr(team_lead, 'team_size') and team_lead.team_size == 5, "TeamLead не має правильного атрибуту 'team_size'"

    print("Усі атрибути TeamLead успішно пройшли перевірку.")


test_team_lead_attributes()
