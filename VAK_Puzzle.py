import streamlit as st

def main():
    st.title("VAK Learning Style Quiz")
    st.write("Answer the following questions to find out your preferred learning style.")

    # Questions and choices
    questions = [
        "When learning something new, you prefer to:",
        "When solving a problem, you:",
        "When giving directions, you:",
        "When remembering a phone number, you:",
        "When studying for an exam, you:",
        "When choosing a vacation destination, you:",
        "When explaining a concept to someone, you:",
        "When attending a lecture, you:",
        "When decorating your home, you:",
        "When learning a new skill, you:",
    ]

    choices = [
        [
            "See diagrams, charts, or written instructions",
            "Listen to someone explain it",
            "Try it out yourself",
        ],
        [
            "Visualize the steps in your mind",
            "Talk through the problem",
            "Physically manipulate objects or tools",
        ],
        [
            "Draw a map or show pictures",
            "Explain it verbally",
            "Point and guide physically",
        ],
        [
            "Write it down or see it written",
            "Say it out loud repeatedly",
            "Dial it multiple times to memorize it",
        ],
        [
            "Use flashcards or highlight notes",
            "Listen to recorded lectures or read aloud",
            "Practice solving problems or using examples",
        ],
        [
            "Look at pictures of the place",
            "Talk to others about it",
            "Visit or imagine being there",
        ],
        [
            "Draw a diagram or use visuals",
            "Explain step-by-step out loud",
            "Use gestures or physical examples",
        ],
        [
            "Focus on slides or notes",
            "Listen attentively to the speaker",
            "Take frequent breaks and move around",
        ],
        [
            "Look for design ideas or photos",
            "Discuss ideas with friends or family",
            "Arrange furniture and try it out",
        ],
        [
            "Follow written instructions or videos",
            "Listen to detailed verbal instructions",
            "Learn by doing and experimenting",
        ],
    ]

    # Scoring system
    scores = {"Visual": 0, "Auditory": 0, "Kinesthetic": 0}

    # Quiz logic
    responses = []

    with st.form("quiz_form"):
        for i, question in enumerate(questions):
            st.write(f"**{question}**")
            choice = st.radio(
                label=f"Question {i + 1}",
                options=choices[i],
                key=f"q{i}"
            )
            responses.append(choice)

        # Submit button
        submitted = st.form_submit_button("Submit")

    if submitted:
        # Validate responses
        if "Select an option" in responses:
            st.error("Please answer all questions before submitting.")
            return

        # Calculate scores
        for i, response in enumerate(responses):
            if response == choices[i][1]:
                scores["Visual"] += 1
            elif response == choices[i][2]:
                scores["Auditory"] += 1
            elif response == choices[i][3]:
                scores["Kinesthetic"] += 1

        # Determine percentages
        total = sum(scores.values())
        if total == 0:
            st.error("No valid answers provided. Please complete the quiz.")
            return

        percentages = {key: (value / total) * 100 for key, value in scores.items()}
        normalized_percentages = {key: value / 100 for key, value in percentages.items()}

        # Display results
        st.write("### Quiz Results")
        st.write(f"**Visual:** {percentages['Visual']:.2f}%")
        st.progress(normalized_percentages["Visual"])
        st.write(f"**Auditory:** {percentages['Auditory']:.2f}%")
        st.progress(normalized_percentages["Auditory"])
        st.write(f"**Kinesthetic:** {percentages['Kinesthetic']:.2f}%")
        st.progress(normalized_percentages["Kinesthetic"])

        # Determine dominant style
        max_score = max(scores.values())
        dominant_styles = [style for style, score in scores.items() if score == max_score]

        if len(dominant_styles) == 1:
            st.write(f"### Your preferred learning style is: **{dominant_styles[0]}**")
        else:
            st.write(f"### You have a balanced preference between: **{', '.join(dominant_styles)}**")

if __name__ == "__main__":
    main()
