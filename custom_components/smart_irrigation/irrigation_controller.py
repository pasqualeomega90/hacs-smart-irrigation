class IrrigationController:
    def __init__(self, config):
        self.config = config
        self.schedule = []
        self.active_sessions = []

    def add_schedule(self, schedule):
        self.schedule.append(schedule)

    def remove_schedule(self, schedule):
        self.schedule.remove(schedule)

    def start_irrigation(self, session):
        self.active_sessions.append(session)
        # Logic to start irrigation

    def stop_irrigation(self, session):
        self.active_sessions.remove(session)
        # Logic to stop irrigation

    def monitor_irrigation(self):
        # Logic to monitor active irrigation sessions
        pass

    def get_status(self):
        # Logic to return the status of irrigation
        return {
            "active_sessions": self.active_sessions,
            "schedule": self.schedule
        }