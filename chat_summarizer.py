def parse_chat_log(file_path):
    user_messages = []
    ai_messages = []
    current_msg = ""
    current_speaker = None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("User:"):
                    if current_speaker == "User":
                        user_messages.append(current_msg.strip())
                    elif current_speaker == "AI":
                        ai_messages.append(current_msg.strip())
                    current_speaker = "User"
                    current_msg = line.replace("User:", "").strip()
                elif line.startswith("AI:"):
                    if current_speaker == "User":
                        user_messages.append(current_msg.strip())
                    elif current_speaker == "AI":
                        ai_messages.append(current_msg.strip())
                    current_speaker = "AI"
                    current_msg = line.replace("AI:", "").strip()
                else:
                    current_msg += " " + line.strip()  # Append continuation

            # Add the last message
            if current_speaker == "User":
                user_messages.append(current_msg.strip())
            elif current_speaker == "AI":
                ai_messages.append(current_msg.strip())

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return [], []

    return user_messages, ai_messages

# Main execution
if __name__ == "__main__":
    chat_file = "chat.txt"  # Make sure this file exists in your current directory
    user_msgs, ai_msgs = parse_chat_log(chat_file)

    print("\nUser Messages:")
    for msg in user_msgs[:3]:  # Show first 3 user messages
        print("- " + msg)

    print("\nAI Messages:")
    for msg in ai_msgs[:3]:  # Show first 3 AI messages
        print("- " + msg)