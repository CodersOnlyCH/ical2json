import icalendar
import datetime
import requests


def from_url(url):
    r = requests.get(url)
    assert r.status_code == 200
    r.encoding = "utf-8"
    return icalendar.Calendar.from_ical(r.text)


def to_jsonable(cal):
    events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            event_data = {}
            for key, value in component.items():
                if isinstance(value, icalendar.vText):
                    event_data[key] = str(value)
                elif hasattr(value, "dt"):
                    event_data[key] = value.dt.isoformat()
                elif hasattr(value, "to_ical"):
                    event_data[key] = value.to_ical().decode("utf-8")
                else:
                    event_data[key] = value
            events.append(event_data)
    return events
