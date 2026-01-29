import streamlit as st

# WICHTIG: Muss ganz oben stehen
st.set_page_config(
    page_title="Notenrechner",
    layout="wide"
)

st.title("Notenrechner – mehrere Fächer")

st.markdown("""
**Gewichtung**
- 3 Klassenarbeiten: **40 %**
- Mündliche Note: **50 %**
- Referat: **10 %**
""")

# -----------------------------
# Session State initialisieren
# -----------------------------
if "faecher" not in st.session_state:
    st.session_state.faecher = []

if "fach_counter" not in st.session_state:
    st.session_state.fach_counter = 1

# -----------------------------
# Fach hinzufügen
# -----------------------------
if st.button("➕ Fach hinzufügen"):
    st.session_state.faecher.append(st.session_state.fach_counter)
    st.session_state.fach_counter += 1

st.markdown("---")

ergebnisse = {}

# -----------------------------
# Fächer anzeigen
# -----------------------------
for fach_id in st.session_state.faecher:
    st.subheader(f"Fach {fach_id}")

    fachname = st.text_input(
        "Fachname",
        key=f"name_{fach_id}",
        placeholder="z. B. Mathematik"
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        k1 = st.number_input("Klassenarbeit 1", 0.0, 15.0, 0.0, 0.1, key=f"k1_{fach_id}")
    with col2:
        k2 = st.number_input("Klassenarbeit 2", 0.0, 15.0, 0.0, 0.1, key=f"k2_{fach_id}")
    with col3:
        k3 = st.number_input("Klassenarbeit 3", 0.0, 15.0, 0.0, 0.1, key=f"k3_{fach_id}")

    col4, col5 = st.columns(2)
    with col4:
        muendlich = st.number_input("Mündliche Note", 0.0, 15.0, 0.0, 0.1, key=f"m_{fach_id}")
    with col5:
        referat = st.number_input("Referat", 0.0, 15.0, 0.0, 0.1, key=f"r_{fach_id}")

    schnitt_klassenarbeiten = (k1 + k2 + k3) / 3
    endnote = (
        schnitt_klassenarbeiten * 0.40 +
        muendlich * 0.50 +
        referat * 0.10
    )

    name = fachname if fachname else f"Fach {fach_id}"
    ergebnisse[name] = endnote

    st.info(f"Aktueller Durchschnitt: {endnote:.2f}")
    st.markdown("---")

# -----------------------------
# Ergebnisübersicht
# -----------------------------
if ergebnisse:
    st.header("Übersicht")

    for fach, note in ergebnisse.items():
        st.write(f"**{fach}:** {note:.2f}")
