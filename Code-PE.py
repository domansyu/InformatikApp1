import streamlit as st
from transformers import pipeline
from PIL import Image

# --------------------------------
# Seitenlayout
# --------------------------------
st.set_page_config(
    page_title="Pflanzenerkennung",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 KI-Pflanzenerkennung")

st.write(
    "Lade ein Bild einer Pflanze hoch. "
    "Die KI versucht die Pflanze zu erkennen."
)

# --------------------------------
# Modell laden
# --------------------------------
@st.cache_resource
def load_model():

    classifier = pipeline(
        "image-classification",
        model="juppy44/plant-identification-2m-vit-b"
    )

    return classifier

classifier = load_model()

# --------------------------------
# Bild hochladen
# --------------------------------
uploaded_file = st.file_uploader(
    "Bild hochladen",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------
# Pflanze erkennen
# --------------------------------
if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Hochgeladenes Bild",
        use_container_width=True
    )

    with st.spinner("Pflanze wird erkannt..."):

        results = classifier(image)

    st.subheader("🔍 Ergebnisse")

    # Top 3 Ergebnisse
    top_results = results[:3]

    for i, result in enumerate(top_results):

        plant_name = result["label"]
        confidence = round(result["score"] * 100, 2)

        st.write(
            f"{i+1}. {plant_name} "
            f"({confidence} % Wahrscheinlichkeit)"
        )

# --------------------------------
# Hinweis
# --------------------------------
st.info(
    "Die KI kann Fehler machen. "
    "Unscharfe oder schlechte Bilder "
    "können zu falschen Ergebnissen führen."
)
