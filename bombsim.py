import streamlit as st
from random import randint
import time
import threading

colors = ["red", "green", "blue"]
bomb_defused = False
selected_color = None

# Function to randomly select a color
def random_color():
    return colors[randint(0, len(colors) - 1)]

# Function to handle the countdown
def countdown():
    global bomb_defused
    for i in range(10, 0, -1):
        if bomb_defused:
            return
        st.warning(f"Time remaining: {i} seconds")
        time.sleep(1)
    if not bomb_defused:
        st.error("BOOM! The bomb exploded. Time's up.")
        st.stop()

# Simulate BOOGIE bomb
def bomb_simulation():
    global bomb_defused, selected_color
    selected_color = random_color()

    # Start the countdown in a separate thread
    timer_thread = threading.Thread(target=countdown)
    timer_thread.start()

# Streamlit app
st.title("BOOGIE Bomb Simulation")

if st.button("Start Simulation"):
    bomb_simulation()

if selected_color:
    user_choice = st.selectbox("Cut a wire:", colors)
    if st.button("Submit"):
        if user_choice == selected_color:
            bomb_defused = True
            st.success("BOOGIE bomb defused!")
        else:
            st.error(f"BOOM! The bomb exploded. The correct color was {selected_color}.")
