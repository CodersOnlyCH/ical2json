from ical2json import calendar
import datetime
import icalendar
import pytest


@pytest.fixture()
def url():
    return "https://www.meetup.com/coders-only/events/ical/"


def test_from_url(url):
    cal = calendar.from_url(url)
    assert hasattr(cal, "events")


def test_raises_when_not_an_ical():
    with pytest.raises(Exception):
        cal = calendar.from_url("https://www.meetup.com/")


@pytest.fixture()
def cal():
    cal = icalendar.Calendar()

    event = icalendar.Event()
    event.add("SUMMARY", "Coders Monthly - Zürich")
    event.add("DESCRIPTION", "A meetup for coders.\nJoin us every month!")
    event.add("URL", "https://codersonly.org")
    event.add(
        "DTSTART", datetime.datetime(2025, 3, 1, 18, 30, tzinfo=datetime.timezone.utc)
    )
    event.add(
        "DTEND", datetime.datetime(2025, 3, 1, 21, 0, tzinfo=datetime.timezone.utc)
    )
    event.add("LOCATION", "Zürich, Switzerland")

    cal.add_component(event)

    return cal


def test_to_jsonable(cal):
    json_events = calendar.to_jsonable(cal)

    assert isinstance(json_events, list)
    assert len(json_events) == 1

    event = json_events[0]

    assert event["SUMMARY"] == "Coders Monthly - Zürich"
    assert event["DESCRIPTION"] == "A meetup for coders.\nJoin us every month!"
    assert event["URL"] == "https://codersonly.org"
    assert event["DTSTART"] == "2025-03-01T18:30:00+00:00"
    assert event["DTEND"] == "2025-03-01T21:00:00+00:00"
    assert event["LOCATION"] == "Zürich, Switzerland"
