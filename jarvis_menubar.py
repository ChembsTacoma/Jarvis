import rumps
import subprocess

class JarvisApp(rumps.App):
    def __init__(self):
        super(JarvisApp, self).__init__("Jarvis")
        self.menu = ["Listen"]

    @rumps.clicked("Listen")
    def listen_command(self, _):
        rumps.notification("Jarvis", "", "Listening now...")
        # Run your listen command — adjust this to your real command!
        subprocess.Popen(["python3", "jarvis_launcher.py"])

if __name__ == "__main__":
    JarvisApp().run()
