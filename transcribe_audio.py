import openai
import os
import argparse

def transcribe_audio(audio_file):
    # Open the audio file in binary mode
    with open(audio_file, "rb") as loaded_file:
        # Transcribe the audio file using OpenAI API
        transcript = openai.Audio.transcribe("whisper-1", loaded_file)

    # Create the output file name by appending ".txt" to the audio file name
    output_file = os.path.basename(audio_file) + ".txt"

    # Open the output file in write mode and write the transcribed text into it
    with open(output_file, 'w') as f:
        f.write(transcript['text'])

if __name__ == '__main__':
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description='Transcribe audio file. Usage: python transcribe_audio.py <path_to_audio_file>')
    # Add an argument to the parser for the audio file path
    parser.add_argument('audio_file', help='path to audio file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the transcribe_audio function with the audio file path argument
    transcribe_audio(args.audio_file)