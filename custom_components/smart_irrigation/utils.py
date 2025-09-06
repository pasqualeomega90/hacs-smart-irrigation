def load_config(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_config(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def validate_irrigation_schedule(schedule):
    if not isinstance(schedule, list):
        return False
    for entry in schedule:
        if not isinstance(entry, dict) or 'start_time' not in entry or 'duration' not in entry:
            return False
    return True

def format_schedule_for_display(schedule):
    formatted_schedule = []
    for entry in schedule:
        formatted_schedule.append(f"Start: {entry['start_time']}, Duration: {entry['duration']} minutes")
    return formatted_schedule

def calculate_next_irrigation(schedule):
    from datetime import datetime, timedelta
    now = datetime.now()
    for entry in schedule:
        start_time = datetime.strptime(entry['start_time'], '%H:%M')
        irrigation_time = now.replace(hour=start_time.hour, minute=start_time.minute, second=0, microsecond=0)
        if irrigation_time > now:
            return irrigation_time
    return None