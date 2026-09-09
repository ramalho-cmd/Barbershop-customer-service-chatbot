


def mocked_avaliable_appointments_response(date: str) -> str:
    """
    Mocked function to simulate the response of available dates from Google Calendar.
    
    Returns:
        str: A mocked response representing available dates.
    """
    return True, f"Available appointments on {date}: 9:00 AM, 10:30 AM, 1:00 PM, 3:30 PM"


def mocked_create_event_response(event_details: dict) -> str:
    """
    Mocked function to simulate the response of creating an event in Google Calendar.
    
    Returns:
        str: A mocked response confirming the creation of the event.
    """
    return True, f"Event '{event_details.get('summary', 'No Title')}' created successfully on {event_details.get('start', {}).get('dateTime', 'Unknown Date')}'."
