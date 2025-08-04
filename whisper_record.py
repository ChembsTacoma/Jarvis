import sounddevice as sd
from scipy.io.wavfile import write

def record_voice(duration=5, fs=44100):
    print("🎙️ Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write("temp.wav", fs, recording)
    print("✅ Recorded")

if __name__ == "__main__":
    record_voice()
