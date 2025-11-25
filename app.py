import streamlit as st

st.set_page_config(
    page_title="Light & Color - Mini Science Lab",
    layout="wide"
)

# ---------- Helper functions ----------

def header_block(title, subtitle, page_no):
    st.markdown(f"### {title}")
    st.caption(subtitle)
    st.caption(f"Experiment {page_no}")

def materials_block(items):
    st.subheader("You will need")
    for item in items:
        st.markdown(f"- {item}")

def steps_block(steps):
    st.subheader("Procedure")
    for i, step in enumerate(steps, start=1):
        st.markdown(f"**Step {i}.** {step}")

def explanation_block(text):
    st.subheader("What is happening")
    st.write(text)

def reflection_block(questions):
    st.subheader("Think and discuss")
    for q in questions:
        st.markdown(f"- {q}")
    st.markdown("Did the activity work as expected?")
    st.checkbox("Yes, it was successful", key=f"succ_{st.session_state.get('exp_key','')}")
    st.checkbox("No, it did not work well", key=f"unsucc_{st.session_state.get('exp_key','')}")


# ---------- Experiment content ----------

def experiment_3():
    st.session_state["exp_key"] = "exp3"
    header_block(
        "Exploring Colors",
        "How colored water changes the light that passes through it",
        "03"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        materials_block(
            [
                "Transparent glass or clear plastic cups",
                "Clean water",
                "Food colouring (red, blue, green, etc.)",
                "Flashlight or torch"
            ]
        )

    with col2:
        st.subheader("Quick setup")
        st.markdown(
            """
            1. Fill each cup most of the way with water.  
            2. Put a different food colour in each cup.  
            3. Darken the room a little and get your torch ready.
            """
        )

    st.divider()

    steps_block(
        [
            "Pour water into the cups, leaving a little empty space at the top.",
            "Add a few drops of a different food colouring into each cup and mix gently.",
            "Turn on the torch and shine it through one coloured cup at a time.",
            "Watch the colour of the beam on the table, wall or your hand."
        ]
    )

    st.divider()

    st.subheader("Try it on the screen")
    colour = st.selectbox(
        "Choose the colour of the water",
        ["Red", "Blue", "Green", "Yellow"]
    )

    if colour == "Red":
        observation = "The beam looks reddish because the water has removed much of the other colours from the white light."
    elif colour == "Blue":
        observation = "The beam looks bluish because most of the red and green parts of the light have been taken in by the water."
    elif colour == "Green":
        observation = "The beam has a green look because mainly green light is passing through to your eyes."
    else:
        observation = "The beam looks yellow because the water is letting the yellow part of the light pass more easily."

    st.info(observation)

    explanation_block(
        "White light is made of many colours. The coloured water keeps (absorbs) some "
        "parts of the light and lets other parts pass through. The colour you see is the "
        "part of the light that was not absorbed by the water."
    )

    reflection_block(
        [
            "What changed when you added more food colouring to a cup",
            "Which colour made the strongest beam",
            "How could you mix colours to make a new colour of light"
        ]
    )


def experiment_4():
    st.session_state["exp_key"] = "exp4"
    header_block(
        "Refraction with Water and Pencil",
        "Why objects can look bent under water",
        "04"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        materials_block(
            [
                "Transparent glass",
                "Clean water",
                "Pencil, straw or stick"
            ]
        )

    with col2:
        st.subheader("Quick setup")
        st.markdown(
            """
            1. Fill the glass with water.  
            2. Put the pencil so that it is part in water and part in air.  
            3. Look from the side of the glass.
            """
        )

    st.divider()

    steps_block(
        [
            "Fill the glass almost to the top with water.",
            "Place the pencil or straw so that it is standing or leaning in the glass, partly under the water.",
            "Look carefully at the point where the pencil meets the water surface.",
            "Move your head to different sides and heights and keep watching the pencil."
        ]
    )

    st.divider()

    st.subheader("Try it on the screen")
    angle = st.slider(
        "Imagine you are looking from different angles. Move the slider.",
        min_value=0,
        max_value=90,
        value=30,
        step=5
    )
    if angle < 30:
        txt = "From almost straight above, the bending is hard to see."
    elif angle < 60:
        txt = "From the side, the pencil looks clearly bent where it enters the water."
    else:
        txt = "From a very low side angle, the bending looks even stronger."
    st.info(txt)

    explanation_block(
        "Light changes direction when it moves from air into water. This change of direction "
        "is called refraction. The light from the part of the pencil in water reaches your eyes "
        "from a different path than the light from the part in air. Your brain joins these paths "
        "together and the pencil seems to be broken or bent at the water surface."
    )

    reflection_block(
        [
            "What happens to the bending when you use a wider glass",
            "Would the effect be stronger in oil or in water",
            "Where do you see similar bending effects in daily life"
        ]
    )


def experiment_5():
    st.session_state["exp_key"] = "exp5"
    header_block(
        "Colourful Light Absorption",
        "Exploring how different colours handle light",
        "05"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        materials_block(
            [
                "Pieces of paper, cloth or plastic in different colours",
                "Scissors and tape",
                "Flashlight or other light source",
                "A darkened room or shaded corner"
            ]
        )

    with col2:
        st.subheader("Quick setup")
        st.markdown(
            """
            1. Cut small pieces of different coloured materials.  
            2. Darken the room slightly.  
            3. Use the torch to shine light through or onto each piece.
            """
        )

    st.divider()

    steps_block(
        [
            "Collect several materials of different colours and cut them into similar small pieces.",
            "Create a darker space by closing curtains or switching off some lights.",
            "Hold one piece at a time in front of the torch or place it on a flat surface and shine the light on it.",
            "Notice how bright or dark the material looks and what happens to the light behind or around it."
        ]
    )

    st.divider()

    st.subheader("Try it on the screen")
    material = st.selectbox(
        "Choose a material colour",
        ["Black material", "White material", "Red material", "Blue material"]
    )

    if material == "Black material":
        obs = "The material looks very dark because it keeps almost all the light that hits it."
    elif material == "White material":
        obs = "The material looks bright because it sends back most of the light in many directions."
    elif material == "Red material":
        obs = "The material sends back mainly red light and keeps most of the other colours."
    else:
        obs = "The material sends back mostly blue light and keeps much of the rest."

    st.info(obs)

    explanation_block(
        "Objects handle light in different ways. Some take in (absorb) most of the light and "
        "look dark. Others send most of the light back and look bright. A coloured object keeps "
        "many colours from white light and sends back only a smaller range, which is the colour "
        "that your eyes see."
    )

    reflection_block(
        [
            "Which colours became warmer to touch after shining the torch for some time",
            "How would these findings be useful when choosing clothes for a hot day",
            "What might this mean for building materials in hot climates"
        ]
    )


def experiment_6():
    st.session_state["exp_key"] = "exp6"
    header_block(
        "Ice Magnifying Glass",
        "Using ice to make objects look bigger",
        "06"
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        materials_block(
            [
                "Flat, clear piece of ice (cube or slab)",
                "Small objects to observe such as leaves, insects, or toys",
                "Tray or plate to hold the melting ice"
            ]
        )

    with col2:
        st.subheader("Quick setup")
        st.markdown(
            """
            1. Prepare a flat, clear piece of ice.  
            2. Place small objects on a tray.  
            3. Hold the ice between your eye and the object.
            """
        )

    st.divider()

    steps_block(
        [
            "Prepare or take a flat piece of clear ice. Ask an adult to support if needed.",
            "Collect small items, for example leaves, printed letters or tiny toys, and place them on a surface.",
            "Hold the ice carefully between your fingers and place it between your eye and one object.",
            "Move the ice nearer or farther from the object and from your eye until the image looks large and clear."
        ]
    )

    st.divider()

    st.subheader("Try it on the screen")
    distance = st.slider(
        "Move the virtual ice closer or farther from the object",
        min_value=1,
        max_value=10,
        value=5
    )
    if distance <= 3:
        msg = "The ice is very close to the object. The image is large but may look blurry."
    elif distance <= 7:
        msg = "The distance is comfortable. The object looks bigger and fairly clear."
    else:
        msg = "The ice is far away. The magnifying effect is weaker."
    st.info(msg)

    explanation_block(
        "When light travels through different materials such as air and ice, its speed and direction change. "
        "The curved shape of the ice can bend and focus light, similar to a simple magnifying glass. "
        "By changing the distance between the ice and the object, you find a position where the light forms a clear, enlarged image for your eye."
    )

    reflection_block(
        [
            "What happened as the ice started to melt",
            "How is this similar to using a real magnifying glass",
            "Where might people use similar ideas in daily tools or technology"
        ]
    )


# ---------- Main layout ----------

st.title("Light & Color - Virtual Experiment Lab")
st.write(
    "This small lab helps learners explore how light and colour behave using simple home materials. "
    "Each activity is meant to support learning by doing."
)

exp_choice = st.sidebar.radio(
    "Choose an experiment",
    (
        "03 - Exploring Colors",
        "04 - Refraction with Water and Pencil",
        "05 - Colourful Light Absorption",
        "06 - Ice Magnifying Glass"
    )
)

if exp_choice.startswith("03"):
    experiment_3()
elif exp_choice.startswith("04"):
    experiment_4()
elif exp_choice.startswith("05"):
    experiment_5()
else:
    experiment_6()
