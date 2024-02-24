import speech_recognition as sr
import jiwer

def recognize_speech(audio_file, language='en-US'):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language=language)
        return recognized_text
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def calculate_word_error_rate(reference_text, recognized_text):
    wer = jiwer.wer(reference_text, recognized_text)
    return wer

if __name__ == "__main__":
    reference_text = "hello how are you"

    audio_file_path = 'audio_file.wav'
    recognized_text = recognize_speech(audio_file_path)

    if recognized_text:
        print(f"Reference Text: {reference_text}")
        print(f"Recognized Text: {recognized_text}")

        wer = calculate_word_error_rate(reference_text, recognized_text)
        print(f"Word Error Rate (WER): {wer * 100:.2f}%")
    else:
        print("No text recognized.")
