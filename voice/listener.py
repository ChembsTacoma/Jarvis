import subprocess
import os


def listen():
    print("🎤 Speak now...")
    subprocess.run(["python3", "whisper_record.py"])
    result = subprocess.run(
        ["whisper", "temp.wav", "--language", "en", "--model", "base"],
        capture_output=True,
        text=True
    )
    print("Whisper raw output:", result.stdout)

    # Delete Whisper's extra temp files
    for ext in [".txt", ".json", ".srt", ".vtt", ".tsv"]:
        filename = f"temp{ext}"
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception as e:
                print(f"Failed to remove {filename}: {e}")

    return result.stdout.strip()
