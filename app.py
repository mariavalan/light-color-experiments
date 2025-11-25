import streamlit as st
from pathlib import Path
from PIL import Image

# ----------------------------------------------------
# BASIC PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Virtual Science Lab - Light and Color",
    layout="wide"
)

# ----------------------------------------------------
# SIMPLE CSS FOR VISUAL STYLE
# ----------------------------------------------------
APP_CSS = """
<style>
    body {
        background-color: #f4f6fb;
    }
    .main-title {
        font-size: 2rem;
        font-weight: 700;
        color: #12355b;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #4b5b70;
        margin-bottom: 1.5rem;
    }
    .lab-card {
        background-color: #ffffff;
        border-radius: 14px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(18, 53, 91, 0.08);
    }
    .step-header {
        font-weight: 600;
        color: #12355b;
        margin-bottom: 0.4rem;
    }
    .step-number {
        background-color: #12355b;
        color: #ffffff;
        border-radius: 999px;
        padding: 0.1rem 0.6rem;
        font-size: 0.8rem;
        margin-right: 0.4rem;
    }
    .small-note {
        font-size: 0.85rem;
        color: #6b7c90;
    }
</style>
"""

st.markdown(APP_CSS, unsafe_allow_html=True)


# ----------------------------------------------------
# HELPER FUNCTIONS
# ----------------------------------------------------
def show_asset(path: str, caption: str | None = None):
    """
    Try to show an image or GIF.
    If file is missing, show a gentle teacher note instead of error.
    """
    p = Path(path)
    if p.exists():
        img = Image.open(p)
        st.image(img, caption=caption, use_column_width=True)
    else:
        st.info(
            f"Teacher note: place a file at `{path}` to show this step visually. "
            f"PNG, JPG or GIF are supported."
        )


def step_card(step_no: int, title: str, body: str):
    """
    Visual container for each step.
    """
    with st.container():
        st.markdown('<div class="lab-card">', unsafe_allow_html=True)
        st.markdown(
            f'<span class="step-number">Step {step_no}</span>'
            f'<span class="step-header">{title}</span>',
            unsafe_allow_html=True,
        )
        st.write(body)
        st.markdown("</div>", unsafe_allow_html=True)


def reflection_questions(questions: list[str], key_prefix: str):
    """
    Simple reflective questions at the end of each experiment.
    Supports INEE style learning by reflection.
    """
    st.subheader("Reflection and learning")
    for i, q in enumerate(questions, start=1):
        st.markdown(f"**Q{i}. {q}**")
        st.text_area(
            "Your notes",
            "",
            key=f"{key_prefix}_q{i}",
            placeholder="Write observations, group feedback or learner comments here.",
        )


# ----------------------------------------------------
# EXPERIMENT 3
# ----------------------------------------------------
def experiment_3():
    st.markdown('<div class="lab-card">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Experiment 3 - Exploring Colours</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">How coloured water changes the light that passes through it</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Virtual lab table: left materials, right live actions
    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown('<div class="lab-card">', unsafe_allow_html=True)
        st.subheader("Materials on the lab table")
        st.markdown(
            """
            - Transparent glasses or clear plastic cups  
            - Clean water  
            - Food colouring (red, blue, green, yellow)  
            - Flashlight or torch  
            """
        )
        st.markdown(
            '<p class="small-note">These materials can usually be found in homes, temporary learning spaces or simple classroom settings.</p>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        tabs = st.tabs(["Prepare", "Do the experiment", "Observe", "Explain"])

        with tabs[0]:
            step_card(
                1,
                "Set up coloured water",
                "Fill each glass with clean water. Add a different food colour to each glass and mix gently.",
            )
            show_asset("assets/images/exp03_setup.png", "Glasses with coloured water")

        with tabs[1]:
            step_card(
                2,
                "Shine the light",
                "Darken the room slightly. Shine the torch through one glass at a time onto a wall or paper.",
            )
            show_asset("assets/gif/exp03_shine.gif", "Torch shining through coloured water")

            colour = st.selectbox(
                "Choose the colour of the water to simulate the beam",
                ["Red", "Blue", "Green", "Yellow"],
                key="exp3_colour",
            )
            intensity = st.slider(
                "Adjust colour intensity",
                min_value=1,
                max_value=10,
                value=5,
                key="exp3_intensity",
            )

            if colour == "Red":
                obs = "The beam looks more and more red as the colour intensity increases."
            elif colour == "Blue":
                obs = "The beam becomes deeper blue when the water is more coloured."
            elif colour == "Green":
                obs = "The beam gets a stronger green tone with higher intensity."
            else:
                obs = "The beam appears brighter yellow at medium intensity and darker at very high intensity."

            st.success(obs + " This simulates what learners might see in the real activity.")

        with tabs[2]:
            step_card(
                3,
                "Observe the beam",
                "Watch the colour of the beam on the wall or paper. Repeat with each colour and compare.",
            )
            show_asset("assets/images/exp03_observe.png", "Example of coloured beams on a wall")

            mix_two = st.multiselect(
                "Choose two colours to mix and imagine the result",
                ["Red", "Blue", "Green", "Yellow"],
                max_selections=2,
                key="exp3_mix",
            )
            if len(mix_two) == 2:
                st.info(
                    f"Discuss with learners: What new colour might appear if {mix_two[0]} and {mix_two[1]} beams mix together"
                )
            else:
                st.info("Select two colours to prompt a colour mixing discussion.")

        with tabs[3]:
            step_card(
                4,
                "What is happening",
                "White light is made of many colours together. Coloured water keeps some parts of the light and lets other parts pass through. "
                "The colour that reaches your eyes is the part that is not absorbed by the water.",
            )
            show_asset("assets/images/exp03_explain.png", "Simple diagram of light and coloured filters")

    reflection_questions(
        [
            "Which colour of water gave the strongest visible beam",
            "How could you adapt this experiment in a low light or high light classroom",
            "How does this experiment support understanding of colour in daily life",
        ],
        key_prefix="exp3",
    )


# ----------------------------------------------------
# EXPERIMENT 4
# ----------------------------------------------------
def experiment_4():
    st.markdown('<div class="lab-card">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Experiment 4 - Refraction with Water and Pencil</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Why objects can look bent under water</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown('<div class="lab-card">', unsafe_allow_html=True)
        st.subheader("Materials on the lab table")
        st.markdown(
            """
            - Transparent glass  
            - Clean water  
            - Pencil, straw or stick  
            """
        )
        st.markdown(
            '<p class="small-note">This experiment is suitable for temporary learning spaces and does not require electricity.</p>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        tabs = st.tabs(["Prepare", "Do the experiment", "Observe", "Explain"])

        with tabs[0]:
            step_card(
                1,
                "Prepare the glass",
                "Fill the transparent glass with water, leaving a small space at the top.",
            )
            show_asset("assets/images/exp04_setup.png", "Glass partly filled with water")

        with tabs[1]:
            step_card(
                2,
                "Place the pencil",
                "Place the pencil or straw so that part of it is under water and part is in the air.",
            )
            show_asset("assets/gif/exp04_place.gif", "Pencil placed in water")

            angle = st.slider(
                "Viewing angle (simulate moving your head)",
                min_value=0,
                max_value=90,
                value=30,
                step=5,
                key="exp4_angle",
            )
            if angle < 20:
                st.info("From almost above, the bending is less visible.")
            elif angle < 60:
                st.success("From the side, the pencil looks clearly bent at the surface of the water.")
            else:
                st.info("From a very low side angle, the bending effect seems stronger.")

        with tabs[2]:
            step_card(
                3,
                "Observe carefully",
                "Ask learners to look at the place where the pencil enters the water. Invite them to describe what they see.",
            )
            show_asset("assets/images/exp04_observe.png", "Apparent bending of pencil in water")

            clarity = st.selectbox(
                "How clear is the water in your context",
                ["Very clear", "Somewhat cloudy", "Quite cloudy"],
                key="exp4_clarity",
            )
            if clarity == "Very clear":
                st.info("With clear water, the bending effect is easy to see.")
            elif clarity == "Somewhat cloudy":
                st.info("With somewhat cloudy water, the effect is still visible but less sharp.")
            else:
                st.info("With very cloudy water, you may need a brighter background to see the effect well.")

        with tabs[3]:
            step_card(
                4,
                "What is happening",
                "Light changes direction when it moves from air into water. This change of direction is called refraction. "
                "The light that comes from the part of the pencil in water reaches your eyes from a different path than the light from the part in air. "
                "Your brain joins these paths and the pencil seems bent.",
            )
            show_asset("assets/images/exp04_explain.png", "Simple refraction diagram")

    reflection_questions(
        [
            "Where do learners see similar bending of light in their daily lives",
            "How could this idea be linked to navigation, fishing or other local livelihoods",
            "How might refraction be important in designing glasses or lenses",
        ],
        key_prefix="exp4",
    )


# ----------------------------------------------------
# EXPERIMENT 5
# ----------------------------------------------------
def experiment_5():
    st.markdown('<div class="lab-card">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Experiment 5 - Colourful Light Absorption</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Exploring how different colours handle light</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown('<div class="lab-card">', unsafe_allow_html=True)
        st.subheader("Materials on the lab table")
        st.markdown(
            """
            - Pieces of paper, cloth or plastic in different colours  
            - Flashlight or lamp  
            - Scissors and tape  
            """
        )
        st.markdown(
            '<p class="small-note">This activity is useful when discussing safe shelter design and heat in hot climates.</p>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        tabs = st.tabs(["Prepare", "Do the experiment", "Observe", "Explain"])

        with tabs[0]:
            step_card(
                1,
                "Prepare coloured samples",
                "Cut pieces of different coloured materials to similar sizes so they can be compared fairly.",
            )
            show_asset("assets/images/exp05_setup.png", "Different coloured materials prepared")

        with tabs[1]:
            step_card(
                2,
                "Shine light on each colour",
                "Place one piece at a time under the torch or lamp. Keep the distance the same for each colour.",
            )
            show_asset("assets/gif/exp05_shine.gif", "Shining light on different coloured surfaces")

            material = st.selectbox(
                "Select a colour to simulate absorption",
                ["Black", "White", "Red", "Blue"],
                key="exp5_material",
            )
            time = st.slider(
                "Time that light shines on the material (relative scale)",
                min_value=1,
                max_value=10,
                value=3,
                key="exp5_time",
            )

            if material == "Black":
                msg = "Black materials absorb more light and often feel warmer after some time."
            elif material == "White":
                msg = "White materials reflect much of the light and usually feel less warm."
            elif material == "Red":
                msg = "Red materials absorb many colours and reflect mostly red light."
            else:
                msg = "Blue materials absorb many colours and reflect mostly blue light."

            st.success(
                msg + " At higher time values the warming effect in real life would usually be stronger."
            )

        with tabs[2]:
            step_card(
                3,
                "Observe warmth and brightness",
                "Ask learners to carefully touch the materials after shining the light for some time and describe differences.",
            )
            show_asset("assets/images/exp05_observe.png", "Comparing brightness and warmth")

            context = st.selectbox(
                "Context for discussion",
                ["Clothing choices", "Roof material", "Tent material", "School wall paint"],
                key="exp5_context",
            )
            st.info(
                f"Facilitators can link findings to {context.lower()} to support practical decision making."
            )

        with tabs[3]:
            step_card(
                4,
                "What is happening",
                "Objects handle light in different ways. Some absorb most of the light and look dark. Others reflect most of the light and look bright. "
                "A coloured object absorbs many colours from white light and reflects only a smaller range, which is the colour that the eyes see.",
            )
            show_asset("assets/images/exp05_explain.png", "Diagram of absorption and reflection")

    reflection_questions(
        [
            "How could this experiment inform choices of shelter material in a hot climate",
            "How might colour choices improve comfort in learning spaces",
            "What local examples can learners identify where colour and heat are linked",
        ],
        key_prefix="exp5",
    )


# ----------------------------------------------------
# EXPERIMENT 6
# ----------------------------------------------------
def experiment_6():
    st.markdown('<div class="lab-card">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Experiment 6 - Ice Magnifying Glass</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Using ice to make objects look bigger</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.markdown('<div class="lab-card">', unsafe_allow_html=True)
        st.subheader("Materials on the lab table")
        st.markdown(
            """
            - Flat, clear piece of ice (cube or slab)  
            - Small objects (leaves, small text, small toys)  
            - Tray or plate to hold the melting ice  
            """
        )
        st.markdown(
            '<p class="small-note">Adult supervision is recommended when preparing ice, especially with younger learners.</p>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        tabs = st.tabs(["Prepare", "Do the experiment", "Observe", "Explain"])

        with tabs[0]:
            step_card(
                1,
                "Prepare the ice and objects",
                "Place the small objects on a flat surface. Prepare a clear piece of ice and place it on a tray.",
            )
            show_asset("assets/images/exp06_setup.png", "Ice piece and small objects")

        with tabs[1]:
            step_card(
                2,
                "Use the ice as a lens",
                "Hold the ice between your eye and one object. Move the ice slowly nearer and farther from the object.",
            )
            show_asset("assets/gif/exp06_move.gif", "Moving the ice between object and eyes")

            distance = st.slider(
                "Simulated distance between ice and object",
                min_value=1,
                max_value=10,
                value=5,
                key="exp6_distance",
            )
            if distance <= 3:
                st.info("Very close distance. The object may look larger but less clear.")
            elif distance <= 7:
                st.success("Medium distance. The object looks bigger and reasonably clear.")
            else:
                st.info("Larger distance. The magnifying effect becomes weaker.")

        with tabs[2]:
            step_card(
                3,
                "Observe changes",
                "Ask learners to describe how the size and clarity of the object change as the ice moves.",
            )
            show_asset("assets/images/exp06_observe.png", "Object seen through ice")

            melt = st.slider(
                "Simulated melting level of ice",
                min_value=0,
                max_value=100,
                value=20,
                key="exp6_melt",
            )
            if melt < 30:
                st.info("Ice is mostly solid. The magnification is more stable.")
            elif melt < 70:
                st.info("Ice is partly melted. Shapes may look distorted.")
            else:
                st.info("Ice is almost melted. The magnifying effect almost disappears.")

        with tabs[3]:
            step_card(
                4,
                "What is happening",
                "When light passes through ice, it changes speed and direction. The curved surface of the ice can focus light, "
                "similar to a simple magnifying glass. At certain distances the image appears larger to the eye.",
            )
            show_asset("assets/images/exp06_explain.png", "Concept of simple lens using ice")

    reflection_questions(
        [
            "How is this similar to using a glass magnifier or spectacles",
            "What challenges might teachers face when doing this in hot climates",
            "How could this activity support children who enjoy practical science but have limited materials",
        ],
        key_prefix="exp6",
    )


# ----------------------------------------------------
# MAIN APP LAYOUT
# ----------------------------------------------------
st.markdown('<div class="main-title">Virtual Science Lab - Light and Color</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Interactive experiments designed for learning by doing in classroom and non classroom settings.</div>',
    unsafe_allow_html=True,
)

st.sidebar.title("Experiment menu")
exp_choice = st.sidebar.radio(
    "Select an experiment",
    (
        "Experiment 3 - Exploring Colours",
        "Experiment 4 - Refraction with Water and Pencil",
        "Experiment 5 - Colourful Light Absorption",
        "Experiment 6 - Ice Magnifying Glass",
    ),
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "Facilitator note: This virtual lab is designed to complement real hands on activities, "
    "not to replace practical experiments where they are possible."
)

if exp_choice.startswith("Experiment 3"):
    experiment_3()
elif exp_choice.startswith("Experiment 4"):
    experiment_4()
elif exp_choice.startswith("Experiment 5"):
    experiment_5()
elif exp_choice.startswith("Experiment 6"):
    experiment_6()
