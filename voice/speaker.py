import subprocess
import queue
import threading

class Speaker:
    def __init__(self):
        self.queue = queue.Queue()
        self.speaking = False
        self.thread = threading.Thread(target=self._speak_worker, daemon=True)
        self.thread.start()

    def _speak_worker(self):
        while True:
            text = self.queue.get()
            if text is None:
                break
            self.speaking = True
            subprocess.run(["say", "-v", "Moira", "-r", "195", text])
            self.speaking = False
            self.queue.task_done()

    def speak(self, text):
        print(f"🗣️ Jarvis: {text}")
        self.queue.put(text)

    def wait_until_done(self):
        self.queue.join()
