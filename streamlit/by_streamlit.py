import random
import streamlit as st

st.title("🎯 Number Guessing Game")

st.image("https://media.licdn.com/dms/image/v2/D4E12AQEESBzNwql5lw/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1676955184042?e=2147483647&v=beta&t=AG1oEokXly7AAuBBJOgMOleY9Q9D-ydaUj_q7iqY_w8" , width=800 )

# Session state initialization
if "computer_guess" not in st.session_state:
    st.session_state.computer_guess = random.randint(1, 100)
if "score" not in st.session_state:
    st.session_state.score = 100
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "won" not in st.session_state:
    st.session_state.won = False
if "lost" not in st.session_state:
    st.session_state.lost = False

MAX_ATTEMPTS = 10
game_over = st.session_state.won or st.session_state.lost

# Score & attempts display
col1, col2 = st.columns(2)
col1.metric("⭐ Score", f"{st.session_state.score}/100")
col2.metric("🎲 Attempts", f"{st.session_state.attempts}/{MAX_ATTEMPTS}")
st.progress(st.session_state.score / 100)

st.divider()

# Input
user_number = st.number_input(
    "**Choose your number (1-100)**",
    min_value=1,
    max_value=100,
    step=1,
    disabled=game_over
)

if st.button("Submit Guess", disabled=game_over):
    st.session_state.attempts += 1

    if user_number == st.session_state.computer_guess:
        st.session_state.won = True
        st.success(f"🎉 Exactly! You win! Final score: {st.session_state.score}/100")
        st.balloons()

    else:
        st.session_state.score = max(0, st.session_state.score - 10)

        # High/low hint
        if user_number > st.session_state.computer_guess:
            st.warning("📉 Too high!")
        else:
            st.warning("📈 Too low!")

        # Hot/cold hint
        diff = abs(user_number - st.session_state.computer_guess)
        if diff <= 5:
            st.info("🔥 Very warm!")
        elif diff <= 15:
            st.info("😐 Lukewarm...")
        else:
            st.info("🥶 Cold!")

        # Check loss condition
        if st.session_state.attempts >= MAX_ATTEMPTS:
            st.session_state.lost = True
            st.error(f"💀 Game over! The number was {st.session_state.computer_guess}")

st.divider()

if st.button("🔄 Reset Game"):
    st.session_state.clear()
    st.rerun()