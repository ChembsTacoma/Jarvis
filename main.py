import re
from voice.listener import listen
from voice.speaker import Speaker
from brain.commands import handle

def main():
    speaker = Speaker()
    greeting = "Greetings bruv. How can I help you today?"
    speaker.speak(greeting)
    speaker.wait_until_done()  # Wait for greeting to finish before listening

    while True:
        print("Press ENTER when you want me to listen...")
        input()
        command = listen()

        if command:
            # Remove Whisper timestamps like [00:00.000 --> 00:02.000]
            command = re.sub(r'\[.*?\]', '', command).strip()
            print(f"Cleaned command: '{command}'")  # Optional: Debug print
            handle(command, speaker)  # handle() handles speaking & waiting internally
        else:
            speaker.speak("Sorry, I didn't catch that.")
            speaker.wait_until_done()

        if command and ("bye" in command.lower() or "exit" in command.lower()):
            break

if __name__ == "__main__":
    main()
