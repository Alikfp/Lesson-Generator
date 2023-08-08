import streamlit as st

def multiple_choice_quiz(questions):
    score = 0
    total_questions = len(questions)

    st.title("Multiple Choice Quiz")

    for idx, (question, options, correct_answer) in enumerate(questions, start=1):
        st.subheader(f"Question {idx}: {question}")
        selected_option = st.radio(f"Select an option for Question {idx}:", options, key=idx)

        # Show feedback only when the "Submit" button is clicked
        submit_key = f"submit_{idx}"
        submit = st.button("Submit", key=submit_key)
        if submit:
            if selected_option == correct_answer:
                st.success("Correct!")
                score += 1
            else:
                st.error("Incorrect. The correct answer is: " + correct_answer)
            st.write("---")  # Separator between questions

    st.subheader("Quiz Results")
    st.write(f"You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], "Paris"),
        ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Mercury"], "Mars"),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
    ]

    multiple_choice_quiz(questions)
