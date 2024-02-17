import streamlit as st
import random

words_db = [
    {"estonian": "ja", "translation": "and", "rank": 1, "score_of_knowledge": 0},
    {"estonian": "on", "translation": "is", "rank": 2, "score_of_knowledge": 0},
    {"estonian": "ei", "translation": "not", "rank": 3, "score_of_knowledge": 0},
    {"estonian": "see", "translation": "this", "rank": 4, "score_of_knowledge": 0},
    {"estonian": "olema", "translation": "to be", "rank": 5, "score_of_knowledge": 0},
    {"estonian": "mis", "translation": "what", "rank": 6, "score_of_knowledge": 0},
    {"estonian": "ma", "translation": "I", "rank": 7, "score_of_knowledge": 0},
    {"estonian": "ta", "translation": "he/she", "rank": 8, "score_of_knowledge": 0},
    {"estonian": "me", "translation": "we", "rank": 9, "score_of_knowledge": 0},
    {"estonian": "nii", "translation": "so", "rank": 10, "score_of_knowledge": 0},
    {"estonian": "aga", "translation": "but", "rank": 11, "score_of_knowledge": 0},
    {"estonian": "kui", "translation": "when", "rank": 12, "score_of_knowledge": 0},
    {"estonian": "nad", "translation": "they", "rank": 13, "score_of_knowledge": 0},
    {"estonian": "see", "translation": "that", "rank": 14, "score_of_knowledge": 0},
    {"estonian": "minu", "translation": "my", "rank": 15, "score_of_knowledge": 0},
    {"estonian": "sa", "translation": "you (singular)", "rank": 16, "score_of_knowledge": 0},
    {"estonian": "te", "translation": "you (plural)", "rank": 17, "score_of_knowledge": 0},
    {"estonian": "see", "translation": "it", "rank": 18, "score_of_knowledge": 0},
    {"estonian": "ole", "translation": "be", "rank": 19, "score_of_knowledge": 0},
    {"estonian": "oma", "translation": "own", "rank": 20, "score_of_knowledge": 0},
    {"estonian": "kõik", "translation": "all", "rank": 21, "score_of_knowledge": 0},
    {"estonian": "või", "translation": "or", "rank": 22, "score_of_knowledge": 0},
    {"estonian": "mida", "translation": "which", "rank": 23, "score_of_knowledge": 0},
    {"estonian": "kui", "translation": "if", "rank": 24, "score_of_knowledge": 0},
    {"estonian": "seal", "translation": "there", "rank": 25, "score_of_knowledge": 0},
    {"estonian": "siin", "translation": "here", "rank": 26, "score_of_knowledge": 0},
    {"estonian": "miks", "translation": "why", "rank": 27, "score_of_knowledge": 0},
    {"estonian": "kuidas", "translation": "how", "rank": 28, "score_of_knowledge": 0},
    {"estonian": "nende", "translation": "their", "rank": 29, "score_of_knowledge": 0},
    {"estonian": "mitte", "translation": "not", "rank": 30, "score_of_knowledge": 0},
    {"estonian": "see", "translation": "the", "rank": 31, "score_of_knowledge": 0},
    {"estonian": "kes", "translation": "who", "rank": 32, "score_of_knowledge": 0},
    {"estonian": "meie", "translation": "our", "rank": 33, "score_of_knowledge": 0},
    {"estonian": "mul", "translation": "I have", "rank": 34, "score_of_knowledge": 0},
    {"estonian": "sinu", "translation": "your", "rank": 35, "score_of_knowledge": 0},
    {"estonian": "neil", "translation": "they have", "rank": 36, "score_of_knowledge": 0},
    {"estonian": "mis", "translation": "which", "rank": 37, "score_of_knowledge": 0},
    {"estonian": "seda", "translation": "this", "rank": 38, "score_of_knowledge": 0},
    {"estonian": "sest", "translation": "because", "rank": 39, "score_of_knowledge": 0},
    {"estonian": "veel", "translation": "more", "rank": 40, "score_of_knowledge": 0},
    {"estonian": "oma", "translation": "your", "rank": 41, "score_of_knowledge": 0},
    {"estonian": "üks", "translation": "one", "rank": 42, "score_of_knowledge": 0},
    {"estonian": "kaks", "translation": "two", "rank": 43, "score_of_knowledge": 0},
    {"estonian": "kolm", "translation": "three", "rank": 44, "score_of_knowledge": 0},
    {"estonian": "neli", "translation": "four", "rank": 45, "score_of_knowledge": 0},
    {"estonian": "viis", "translation": "five", "rank": 46, "score_of_knowledge": 0},
    {"estonian": "kuus", "translation": "six", "rank": 47, "score_of_knowledge": 0},
    {"estonian": "seitse", "translation": "seven", "rank": 48, "score_of_knowledge": 0},
    {"estonian": "kaheksa", "translation": "eight", "rank": 49, "score_of_knowledge": 0},
    {"estonian": "üheksa", "translation": "nine", "rank": 50, "score_of_knowledge": 0},
    {"estonian": "kümme", "translation": "ten", "rank": 51, "score_of_knowledge": 0},
    {"estonian": "inimene", "translation": "person", "rank": 52, "score_of_knowledge": 0},
    {"estonian": "aeg", "translation": "time", "rank": 53, "score_of_knowledge": 0},
    {"estonian": "öö", "translation": "night", "rank": 54, "score_of_knowledge": 0},
    {"estonian": "päev", "translation": "day", "rank": 55, "score_of_knowledge": 0},
    {"estonian": "koer", "translation": "dog", "rank": 56, "score_of_knowledge": 0},
    {"estonian": "kass", "translation": "cat", "rank": 57, "score_of_knowledge": 0},
    {"estonian": "raamat", "translation": "book", "rank": 58, "score_of_knowledge": 0},
    {"estonian": "auto", "translation": "car", "rank": 59, "score_of_knowledge": 0},
    {"estonian": "maja", "translation": "house", "rank": 60, "score_of_knowledge": 0},
    {"estonian": "töö", "translation": "work", "rank": 61, "score_of_knowledge": 0},
    {"estonian": "linn", "translation": "city", "rank": 62, "score_of_knowledge": 0},
    {"estonian": "riik", "translation": "country", "rank": 63, "score_of_knowledge": 0},
    {"estonian": "vesi", "translation": "water", "rank": 64, "score_of_knowledge": 0},
    {"estonian": "suur", "translation": "big", "rank": 65, "score_of_knowledge": 0},
    {"estonian": "väike", "translation": "small", "rank": 66, "score_of_knowledge": 0},
    {"estonian": "uus", "translation": "new", "rank": 67, "score_of_knowledge": 0},
    {"estonian": "hea", "translation": "good", "rank": 68, "score_of_knowledge": 0},
    {"estonian": "halb", "translation": "bad", "rank": 69, "score_of_knowledge": 0},
    {"estonian": "vana", "translation": "old", "rank": 70, "score_of_knowledge": 0},
    {"estonian": "noor", "translation": "young", "rank": 71, "score_of_knowledge": 0},
    {"estonian": "ilus", "translation": "beautiful", "rank": 72, "score_of_knowledge": 0},
    {"estonian": "kole", "translation": "ugly", "rank": 73, "score_of_knowledge": 0},
    {"estonian": "pikk", "translation": "tall", "rank": 74, "score_of_knowledge": 0},
    {"estonian": "lühike", "translation": "short", "rank": 75, "score_of_knowledge": 0},
    {"estonian": "raske", "translation": "heavy", "rank": 76, "score_of_knowledge": 0},
    {"estonian": "kerge", "translation": "light", "rank": 77, "score_of_knowledge": 0},
    {"estonian": "kiire", "translation": "fast", "rank": 78, "score_of_knowledge": 0},
    {"estonian": "aeglane", "translation": "slow", "rank": 79, "score_of_knowledge": 0},
    {"estonian": "külm", "translation": "cold", "rank": 80, "score_of_knowledge": 0},
    {"estonian": "soe", "translation": "warm", "rank": 81, "score_of_knowledge": 0},
    {"estonian": "kõva", "translation": "hard", "rank": 82, "score_of_knowledge": 0},
    {"estonian": "pehme", "translation": "soft", "rank": 83, "score_of_knowledge": 0},
    {"estonian": "sile", "translation": "smooth", "rank": 84, "score_of_knowledge": 0},
    {"estonian": "kare", "translation": "rough", "rank": 85, "score_of_knowledge": 0},
    {"estonian": "tühi", "translation": "empty", "rank": 86, "score_of_knowledge": 0},
    {"estonian": "täis", "translation": "full", "rank": 87, "score_of_knowledge": 0},
    {"estonian": "raske", "translation": "difficult", "rank": 88, "score_of_knowledge": 0},
    {"estonian": "lihtne", "translation": "easy", "rank": 89, "score_of_knowledge": 0},
    {"estonian": "lai", "translation": "wide", "rank": 90, "score_of_knowledge": 0},
    {"estonian": "kitsas", "translation": "narrow", "rank": 91, "score_of_knowledge": 0},
    {"estonian": "märg", "translation": "wet", "rank": 92, "score_of_knowledge": 0},
    {"estonian": "kuiv", "translation": "dry", "rank": 93, "score_of_knowledge": 0},
    {"estonian": "tugev", "translation": "strong", "rank": 94, "score_of_knowledge": 0},
    {"estonian": "nõrk", "translation": "weak", "rank": 95, "score_of_knowledge": 0},
    {"estonian": "kõrge", "translation": "high", "rank": 96, "score_of_knowledge": 0},
    {"estonian": "madal", "translation": "low", "rank": 97, "score_of_knowledge": 0},
    {"estonian": "vana", "translation": "old (age)", "rank": 98, "score_of_knowledge": 0},
    {"estonian": "uus", "translation": "new (fresh)", "rank": 99, "score_of_knowledge": 0},
    {"estonian": "sama", "translation": "same", "rank": 100, "score_of_knowledge": 0}
]


def get_top_x_relevant_words(word_list, x):
    for word in word_list:
        word['relevance'] = word['rank'] + word['score_of_knowledge']
    sorted_list = sorted(word_list, key=lambda x: x['relevance'])
    return sorted_list[:x]

def generate_sentences(word_list):
    # Placeholder function, replace with actual sentence generation
    return [f"Example sentence for {word['estonian']}: ..." for word in word_list]


def main():
    st.title("Learn Estonian - Top Words")
    
    # Initialize session variables
    if 'correct_answers' not in st.session_state:
        st.session_state.correct_answers = 0
    if 'current_word_index' not in st.session_state:
        st.session_state.current_word_index = 0
    if 'attempted' not in st.session_state:
        st.session_state.attempted = False
    
    # Initialize words to learn only once
    if 'words_to_learn' not in st.session_state:
        st.session_state.words_to_learn = get_top_x_relevant_words(words_db, 5)

    # Display the current word and options
    if st.session_state.correct_answers < len(st.session_state.words_to_learn):
        word = st.session_state.words_to_learn[st.session_state.current_word_index]
        choices = [w['translation'] for w in random.sample(words_db, 3)] + [word['translation']]
        random.shuffle(choices)

        st.write(f"**Word to learn**: {word['estonian']}")

        # Using a placeholder for dynamic content updates
        placeholder = st.empty()
        option = placeholder.radio("Choose the correct translation:", choices, key="dynamic_option")

        if st.button("Submit") or st.session_state.attempted:
            st.session_state.attempted = True  # Indicate an attempt was made
            
            if option == word['translation']:
                if not st.session_state.attempted:
                    word['score_of_knowledge'] += 0.1
                    st.session_state.correct_answers += 1
                    st.success("Correct!")
                else:
                    st.info("Correct! Moving to the next word.")
            else:
                if not st.session_state.attempted:
                    word['score_of_knowledge'] -= 0.2
                    st.error("Incorrect. Try again!")
            
            # Move to the next word after feedback
            if st.button("Next") or (option == word['translation']):
                st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(st.session_state.words_to_learn)
                st.session_state.attempted = False  # Reset for the next word
                placeholder.empty()  # Clear the previous selection
                
    else:
        st.write("You've learned all words for now! Here are some example sentences:")
        sentences = generate_sentences(st.session_state.words_to_learn)
        for sentence in sentences:
            st.write(sentence)

        if st.button("Restart"):
            # Resetting the app to start over
            st.session_state.correct_answers = 0
            st.session_state.current_word_index = 0
            st.session_state.words_to_learn = get_top_x_relevant_words(words_db, 5)
            st.session_state.attempted = False

if __name__ == "__main__":
    main()
