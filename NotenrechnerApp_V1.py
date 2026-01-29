import streamlit as st

# Muss ganz oben stehen
st.set_page_config(
    page_title="Notenrechner",
    layout="wide"
)

st.title("📘 Notenrechner – mehrere Fächer")

st.markdown("""
**Gewichtung**
- 3 Klassenarbeiten: **40 %**
- Mündliche Note: **50 %**
- Referat: **10 %**

🔢 **Notenskala: 1–6 (nur natürliche Zahlen)**
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

st.divider()

ergebnisse = {}

# -----------------------------
# Fächer anzeigen
# -----------------------------
for fach_id in st.session_state.faecher:
    with st.container():
        col_title, col_delete = st.columns([5, 1])

        with col_title:
            st.subheader(f"Fach {fach_id}")

        with col_delete:
            if st.button("❌ Entfernen", key=f"del_{fach_id}"):
                st.session_state.faecher.remove(fach_id)
                st.experimental_rerun()

        fachname = st.text_input(
            "Fachname",
            key=f"name_{fach_id}",
            placeholder="z. B. Mathematik"
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            k1 = st.number_input(
                "Klassenarbeit 1", min_value=1, max_value=6, step=1, key=f"k1_{fach_id}"
            )
        with col2:
            k2 = st.number_input(
                "Klassenarbeit 2", min_value=1, max_value=6, step=1, key=f"k2_{fach_id}"
            )
        with col3:
            k3 = st.number_input(
                "Klassenarbeit 3", min_value=1, max_value=6, step=1, key=f"k3_{fach_id}"
            )

        col4, col5 = st.columns(2)
        with col4:
            muendlich = st.number_input(
                "Mündliche Note", min_value=1, max_value=6, step=1, key=f"m_{fach_id}"
            )
        with col5:
            referat = st.number_input(
                "Referat", min_value=1, max_value=6, step=1, key=f"r_{fach_id}"
            )

        # Berechnung
        schnitt_klassenarbeiten = (k1 + k2 + k3) / 3
        endnote = (
            schnitt_klassenarbeiten * 0.40 +
            muendlich * 0.50 +
            referat * 0.10
        )

        name = fachname if fachname else f"Fach {fach_id}"
        ergebnisse[name] = endnote

        st.info(f"📊 Aktueller Durchschnitt: **{endnote:.2f}**")
        st.divider()
