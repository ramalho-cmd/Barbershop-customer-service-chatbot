import application.use_cases.chatbot_assistant as chatbot_assistant

assistant_calling = chatbot_assistant.handle_chatbot_request(
	"1234567890", "Hello, I need help with my appointment at 2024-06-15."
)

print(assistant_calling)