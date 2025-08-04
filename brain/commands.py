import datetime
import subprocess
import webbrowser
import time

def activate_app(app_name):
    if app_name == "Finder":
        script = '''
        tell application "Finder"
            activate
            if not (exists window 1) then
                make new Finder window
            end if
        end tell
        '''
    elif app_name == "System Settings":
        script = '''
        tell application "System Settings"
            activate
        end tell
        delay 0.5
        tell application "System Events"
            tell process "System Settings"
                set frontmost to true
                try
                    if exists window 1 then
                        perform action "AXRaise" of window 1
                    end if
                end try
            end tell
        end tell
        '''
    elif app_name == "Notes":
        script = '''
        tell application "System Events"
            set notesRunning to (exists process "Notes")
        end tell

        if notesRunning then
            tell application "Notes" to quit
            delay 2
        end if

        do shell script "open -a Notes"
        '''
    else:
        script = f'''
        tell application "{app_name}"
            if it is running then
                activate
            else
                launch
                activate
            end if
        end tell
        '''
    subprocess.run(["osascript", "-e", script])

def handle(command, speaker):
    command = command.lower()

    def say_and_wait(text):
        speaker.speak(text)
        speaker.wait_until_done()
        time.sleep(0.5)

    if "time" in command:
        response = datetime.datetime.now().strftime("The time is %I:%M %p")
        say_and_wait(response)

    elif "safari" in command and "spotify" not in command:
        say_and_wait("Opening Safari")
        activate_app("Safari")

    elif "finder" in command:
        say_and_wait("Opening Finder")
        activate_app("Finder")

    elif "messages" in command:
        say_and_wait("Opening Messages")
        activate_app("Messages")

    elif "mail" in command:
        say_and_wait("Opening Mail")
        activate_app("Mail")

    elif "notes" in command:
        say_and_wait("Opening Notes")
        activate_app("Notes")

    elif "settings" in command or "system settings" in command:
        say_and_wait("Opening System Settings")
        activate_app("System Settings")

    elif any(phrase in command for phrase in ["spotify", "open spotify"]):
        say_and_wait("Opening Spotify in Safari")
        webbrowser.open("https://open.spotify.com")

    elif any(phrase in command for phrase in [
        "chatgpt", "chat gpt", "open chat gpt", "charge gpt", "chat gb", "charge ib"
    ]):
        say_and_wait("Opening ChatGPT in Safari")
        webbrowser.open("https://chatgpt.com")

    elif any(phrase in command for phrase in ["google", "open google", "search google"]):
        say_and_wait("Opening Google")
        webbrowser.open("https://www.google.com")

    elif any(phrase in command for phrase in ["youtube", "open youtube"]):
        say_and_wait("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "hello" in command or "hi" in command:
        say_and_wait("Hello! How can I help you?")

    elif "bye" in command or "exit" in command:
        say_and_wait("Goodbye!")

    else:
        fallback_text = "Sorry, I didn't understand that. Could you please repeat?"
        say_and_wait(fallback_text)
