


def mocked_assistant_response(prompt: str, context: str = "") -> str:
    """
    Mocked function to simulate the response of an AI assistant.
    
    Args:
        prompt (str): The input prompt for the AI assistant.
        context (str): Optional context to provide additional information for the response.
        
    Returns:
        str: A mocked response based on the input prompt.
    """
    # Simple mock logic based on the prompt and context
    if "hello" in prompt.lower():
        return True, "Hello! How can I assist you today?"
    elif "help" in prompt.lower():
        return True, "Sure! What do you need help with?"
    elif "appointment" in prompt.lower():
        return True, "I you help you with your appointment."
    else:
        return False, "I'm not sure how to respond to that. Can you please clarify?"