import psutil

def get_power_status():
    battery = psutil.sensors_battery()
    # Returns True if plugged in, False if on battery, None if not detected
    return battery.power_plugged if battery else None