import streamlit as st
import pandas as pd

# Funktion zum Überprüfen, ob die Firma existiert
def firma_existiert(firmenname):
    # Hier könntest du Code einfügen, um im Internet nach der Firma zu suchen und die Existenz zu überprüfen
    # Dies könnte z. B. Web-Scraping oder API-Aufrufe beinhalten
    # Für dieses Beispiel geben wir einfach "True" zurück
    return True
st.set_option('server.port', 5500)
def main():
    st.title('Firmenexistenz überprüfen')

    # Excel-Datei hochladen
    uploaded_file = st.file_uploader("Excel-Datei hochladen", type=["xlsx"])

    if uploaded_file is not None:
        # Daten aus der Excel-Datei lesen
        df = pd.read_excel(uploaded_file)

        # Spaltenüberschriften anzeigen
        st.write("Spaltenüberschriften der Excel-Datei:")
        st.write(df.columns.tolist())

        # Daten anzeigen
        st.write("Erste 5 Zeilen der Excel-Datei:")
        st.write(df.head())

        # Firmenexistenz überprüfen
        st.write("Firmenexistenz überprüfen:")

        for index, row in df.iterrows():
            firmenname = row['Firmenname']  # Annahme: Die Spalte mit den Firmennamen heißt "Firmenname"
            exists = firma_existiert(firmenname)
            st.write(f"Firma '{firmenname}' existiert: {exists}")

    
if __name__ == "__main__":
    main()