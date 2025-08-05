import rumps
from voice.listener import listen
from voice.speaker import Speaker
from brain.commands import handle

class JarvisApp(rumps.App):
    def __init__(self):
        super().__init__("Jarvis")
        self.speaker = Speaker()

        # Say intro greeting once on startup
        self.speaker.speak("Greetings bruv. How can I help you today?")
        self.speaker.wait_until_done()

        # Create a menu with a Listen item
        self.menu = ["Listen"]

    @rumps.clicked("Listen")
    def listen_command(self, _):
        rumps.notification("Jarvis", "", "Listening now...")
        command = listen()
        if command:
            # Clean Whisper timestamps if present
            import re
            command = re.sub(r'\[.*?\]', '', command).strip()
            print(f"Cleaned command: '{command}'")

            handle(command, self.speaker)
        else:
            self.speaker.speak("Sorry, I didn't catch that.")
            self.speaker.wait_until_done()

        # Optional: Quit if command is exit/bye
        if command and ("bye" in command.lower() or "exit" in command.lower()):
            rumps.quit_application()

if __name__ == "__main__":
    JarvisApp().run()
