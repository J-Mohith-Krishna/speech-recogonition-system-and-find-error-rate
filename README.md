# Speech-recogonition-system-and-find-error-rate
## Description-
This Python script uses `speech_recognition` to transcribe speech from an audio file and calculates the Word Error Rate (WER) with `jiwer`. It simulates a reference text and processes an audio file for recognition. If successful, it prints the reference text, recognized text, and WER; otherwise, it displays a message if no text is recognized. 
## Explanation-
  -1. **Importing Libraries**: The script begins by importing the necessary libraries: `speech_recognition` for speech recognition functionality and `jiwer` for calculating the Word Error Rate.

  -2. **Speech Recognition Function (`recognize_speech`)**: This function transcribes speech from an audio file into text using the `recognize_google` method from the `Recognizer` class in `speech_recognition`. It handles exceptions for unknown value errors or request errors.

  -3. **Calculating Word Error Rate Function (`calculate_word_error_rate`)**: This function calculates the Word Error Rate (WER) between a reference text and a recognized text using the `wer` function from the `jiwer` library.

  -4. **Main Execution (`__main__` Block)**: Simulated reference text and the path to the audio file are provided. The `recognize_speech` function transcribes speech from the audio file. If successful, the reference text, recognized text, and Word Error Rate are printed. If no text is recognized, a message indicating the absence of recognized text is displayed.
