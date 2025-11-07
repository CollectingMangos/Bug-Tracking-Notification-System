class BugTracker:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BugTracker, cls).__new__(cls)
            cls._instance.bugs_list = []
        return cls._instance

    def add_bug(self, bug):
        self.bugs_list.append(bug)

class Developer:
    def __init__(self, name):
        self.name = name

    def update_bug(self, bug_name, new_status):
        print(f"{self.name} notified: '{bug_name}' is now '{new_status}'")

class Bug:
    def __init__(self, title):
        self.title = title
        self.status = "Created"
        self.assignees = []

    def assign(self, developer):
        self.assignees.append(developer)

    def set_status(self, new_status):
        self.status = new_status
        self.notify_all()

    def notify_all(self):
        for developer in self.assignees:
            developer.update_bug(self.title, self.status)


class BugFactory:
    @staticmethod
    def create_bug(bug_type):
        if bug_type == "UI":
            return Bug("UI Bug")
        elif bug_type == "Backend":
            return Bug("Backend Bug")
        elif bug_type == "Performance":
            return Bug("Performance Bug")
        else:
            raise ValueError("Unknown bug type")

if __name__ == "__main__":
    tracker = BugTracker()

    alice = Developer("Alice")
    bob = Developer("Bob")

    ui_bug = BugFactory.create_bug("UI")
    backend_bug = BugFactory.create_bug("Backend")
    performance_bug = BugFactory.create_bug("Performance")

    tracker.add_bug(ui_bug)
    tracker.add_bug(backend_bug)
    tracker.add_bug(performance_bug)

    ui_bug.assign(alice)
    backend_bug.assign(bob)
    performance_bug.assign(alice)

    ui_bug.set_status("In Progress")
    backend_bug.set_status("Resolved")
    performance_bug.set_status("In Progress")

    print("\nAll bugs have been updated to their respective statuses.")