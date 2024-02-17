import streamlit as st
import time


# Page title and icon
st.set_page_config(page_title="<Music Selector Name>", page_icon=":musical_note:", layout="wide")

#Default moods and corresponding songs
# note: change this into the working code

moods = {
    "Happy": ["song 1", "song 2", "song 3", "song 4", "song 5"],
    "Sad": ["song 1", "song 2", "song 3", "song 4", "song 5"],
    "Excited": ["song 1", "song 2", "song 3", "song 4", "song 5"],
    "Relaxed": ["song 1", "song 2", "song 3", "song 4", "song 5"]
}

def dummy_text_function():
    st.subheader(f"Here's a {mood.lower()} playlist for you!")
    for playlist in moods[mood]:
        return st.write(playlist)

def dummy_image_function():
    st.subheader(f"Here's a <identified emotion> playlist for you!")
    st.write("imagine this is a list of songs")

def dummy_video_function():
    st.subheader(f"Here's a <identified emotion> playlist for you!")
    st.write("imagine this is a list of songs")


#---------------------------------------------------------------

# Header and Description
st.title("<Music Selector Project>") #official name still hasn't been decided
st.write(" ")

col3, col4 = st.columns([1.5,3])
with col3:
    st.subheader("Tune in your Emotions, Transform out your Playlist!")
    st.subheader(" ")
    st.image("images/instruction_flow_2.png")
    # col3_1, col3_2 = col3.columns(2)
    # col3_1.image("images/upload_icon.png")

    #caption="1. Upload your photo/ video of your face.")
    #"2. Click the submit button to start the process.")
    #caption="3. Please give the application some time identify the emotion to be used.")
    #caption="4. After emotion recognition, the application will start generating the playlist based on the extracted emotion from the image/video.")
    #caption="5. Play the generated playlist from the website and/ save it to your Spo.")

col3.title(" ")
col3.write("Some disclaimer here: data scope, accuracy etc.")
col4.image("/root/code/Atsuto-T/Music_Selector_Project/music-selector/interface/images/Playlist-amico (1).png")
#image attribute: <a href="https://storyset.com/app">App illustrations by Storyset</a>
st.subheader(" ")

#---------------------------------------------------------------

# Sidebar
st.sidebar.title("About <Music Selector>") #change to official name
st.sidebar.image("/root/code/Atsuto-T/Music_Selector_Project/music-selector/interface/images/Music-cuate.png")
#attribute: <a href="https://storyset.com/app">App illustrations by Storyset</a>
st.sidebar.subheader("I. How to generate your playlist?")
st.sidebar.subheader("II. How to add the playlist to your Spotify library?")
st.sidebar.subheader("II. How to reset the playlist generation?")
st.sidebar.subheader("III. Meet the Team")

#---------------------------------------------------------------

#configure page layout
# three columns for inputs
col1, col2,  col3 = st.columns([3, 0.8, 4])

with col1:
    # text input form
    st.subheader("Select your current mood")
    with st.form("text_input"):
        mood = st.selectbox("Choose an emotion:", list(moods.keys()))
        st.session_state["mood"] = None
        submit_button= st.form_submit_button("Submit Emotion")
        if submit_button:
            st.write("Emotion selected")
            st.session_state["mood"] = mood

with col1:
    #image input form
    st.write(" ")
    st.subheader("Upload an image of your face showing how you currently feel")
    with st.form("image_input"):
        uploaded_image = st.file_uploader("Choose a picture:", type=["png", "jpeg", "jpg"])
        st.session_state["uploaded_image"] = None
        submit_button = st.form_submit_button("Submit Image")
        if submit_button:
            st.write("Image input detected")
            st.session_state["uploaded_image"] = uploaded_image


with col1:
    #video input form
    st.write(" ")
    st.subheader("Upload a video of your face showing how you currently feel")
    with st.form("video_input"):
        uploaded_video = st.file_uploader("Choose a video:", type=["mp4"])
        st.session_state["uploaded_video"] = None
        submit_button = st.form_submit_button("Submit Video")
        if submit_button:
            st.write("Video input detected")
            st.session_state["uploaded_video"] = uploaded_video


# Display generated playlist based on input
with col3:
    st.write(" ")
    if st.session_state.get("mood"):
        mood = st.session_state["mood"]
        st.write(f"Selected emotion: {mood}")
        with st.spinner("Transforming Emotions into Melodies..."):
            time.sleep(5)  # simulate playlist generation time
        dummy_text_function()

        #embeded link to spotify
        st.write("Add this playlist to your Spotify library!")
        st.markdown('<iframe src="https://open.spotify.com/embed/playlist/0HI7czcgdxj4bPu3eRlc2C?utm_source=generator"\
        width="500" height="400"></iframe>', unsafe_allow_html=True)
        #change with dynamic link

    elif st.session_state.get("uploaded_image"):
        uploaded_image = st.session_state["uploaded_image"]
        st.write("Image input detected")
        with st.spinner("Transforming Emotions into Melodies..."):
            time.sleep(5)  # simulate playlist generation time
        dummy_image_function()

        #link to spotify
        st.write("Add this playlist to your Spotify library!")
        st.markdown('<iframe src="https://open.spotify.com/embed/playlist/0HI7czcgdxj4bPu3eRlc2C?utm_source=generator"\
        width="500" height="400"></iframe>', unsafe_allow_html=True)
        #change with dynamic link

    elif st.session_state.get("uploaded_video"):
        uploaded_video = st.session_state["uploaded_video"]
        st.write("Video input detected")
        with st.spinner("Transforming Emotions into Melodies..."):
            time.sleep(5)  # simulate playlist generation time
        dummy_video_function()

        #link to spotify
        st.write("Add this playlist to your Spotify library!")
        st.markdown('<iframe src="https://open.spotify.com/embed/playlist/0HI7czcgdxj4bPu3eRlc2C?utm_source=generator"\
        width="500" height="400"></iframe>', unsafe_allow_html=True)
        #change with dynamic link

    else:
        st.subheader(" ")
        st.caption("                 Please Choose your preferred input type to generate the playlist.")
        # st.image("/root/code/Atsuto-T/Music_Selector_Project/music-selector/interface/images/World Emoji Day-bro.png", width=400)
        #attribute: <a href="https://storyset.com/technology">Technology illustrations by Storyset</a>
# st.subheader(" ")
# col5, col6 = st.columns(2)
# col6.write("Add this playlist to your Spotify library!")

# col7, col8, col9, col0 = st.columns([2,2,2,2])
# col9.link_button("share to library", "https://docs.streamlit.io/library/api-reference/widgets/st.link_button")
# col0.link_button("re-generate playlist", "https://docs.streamlit.io/library/api-reference/widgets/st.link_button")
