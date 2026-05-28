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
    "Lade ein Bild einer Pflanze hoch."
)

# --------------------------------
# Modell laden
# --------------------------------
@st.cache_resource
def load_model():

    try:
        classifier = pipeline(
            "image-classification",
            model="google/vit-base-patch16-224"
        )

        return classifier

    except Exception as e:
        st.error(f"Fehler beim Laden des Modells: {e}")
        return None

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

    classifier = load_model()

    if classifier is None:
        st.stop()

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Hochgeladenes Bild",
        use_container_width=True
    )

    with st.spinner("Pflanze wird erkannt..."):

        results = classifier(image)

    st.subheader("🔍 Ergebnisse")

    top_results = results[:5]

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
    "Besonders bei schlechten Bildern oder ähnlichen Pflanzen."
)
