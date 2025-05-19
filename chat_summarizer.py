import string
from collections import Counter
#Add stop words manually
STOP_WORDS = {
    "the", "is", "in", "and", "to", "a", "of", "that", "it", "this",
    "for", "on", "with", "as", "was", "at", "by", "an", "be", "are",
    "i","can","hi","hello","How","you","What","me","my","your","we","our","us",
    "he","she","they","them","his","her","their","its","there","where"
}

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


def generate_statistics(user_messages, ai_messages):
    user_count = len(user_messages)
    ai_count = len(ai_messages)
    total_count = user_count + ai_count

    print(f"\nTotal Messages: {total_count}")
    print(f"User Messages: {user_count}")
    print(f"AI Messages: {ai_count}")

def extract_keywords(messages, top_n=5):
    words = []
    for message in messages:
        message = message.lower().translate(str.maketrans('', '', string.punctuation))
        words.extend(message.split())
    filtered_words = [word for word in words if word not in STOP_WORDS]
    frequency = Counter(filtered_words)
    most_common = frequency.most_common(top_n)  
    return most_common


# Main execution
if __name__ == "__main__":
    chat_file = "chat.txt"  # Make sure this file exists in your current directory
    user_messages, ai_messages = parse_chat_log(chat_file)

    print("\nUser Messages:")
    for msg in user_messages[:3]:  # Show first 3 user messages
        print("- " + msg)

    print("\nAI Messages:")
    for msg in ai_messages[:3]:  # Show first 3 AI messages
        print("- " + msg)

    generate_statistics(user_messages, ai_messages)

    print("\n===== Keyword Analysis =====")
    all_messages = user_messages + ai_messages
    top_keywords = extract_keywords(all_messages)
    print("\nMost Common Keywords in All Messages:")
    user_keywords = extract_keywords(user_messages)    
    for word, count in top_keywords:
        print(f"{word}: {count}")  