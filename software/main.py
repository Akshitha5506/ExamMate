from stt_module import listen_command
from tts_module import speak_text
from question_engine import get_question

def main():
    speak_text("Welcome to ExamMate. Please choose a subject.")
    
    subject = listen_command()
    question = get_question(subject)

    speak_text(question)

if __name__ == "__main__":
    main()
