import services.ia.openai.openai_agent as openai_agent
import services.messaging.whatsapp.whatsapp as whatsapp
import services.db.dynamodb.dynamodb as dynamodb
import services.calendar.google_calendar.google_calendar as google_calendar


def handle_chatbot_request(user_phone_number: str, user_message: str) -> str:
    """
    Handles the chatbot request by processing the user's message, interacting with the AI assistant,
    and sending a response via WhatsApp.

    Args:
        user_phone_number (str): The phone number of the user.
        user_message (str): The message sent by the user.

    Returns:
        str: A response message indicating the result of the operation.
    """
    # Fetch old messages from the database
    success, old_messages = dynamodb.get_mocked_data(user_phone_number)
    if not success:
        return "Failed to retrieve old messages."

    # Generate a response using the AI assistant
    success, ai_response = openai_agent.mocked_assistant_response(user_message, context=old_messages)
    if not success:
        return "Failed to generate a response from the AI assistant."

    #Simulate checking available appointments from Google Calendar
    success, available_appointments = google_calendar.mocked_avaliable_appointments_response("2024-06-15")
    if not success: 
        return "Failed to retrieve available appointments."

    message_response = f"{ai_response}\n\n{available_appointments}"

    # Send the response via WhatsApp
    success, send_status = whatsapp.send_whatsapp_message(user_phone_number, message_response)
    if not success:
        return "Failed to send message via WhatsApp."

    return send_status