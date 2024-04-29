import streamlit as st
import pandas as pd
import openpyxl as op
import requests
import json
from io import StringIO

# Funktion zum Überprüfen, ob die Firma existiert
def firma_existiert(Firmenname):
 
    print(Firmenname)
    userprompt = f"Search for the Company {Firmenname}. Provide me the Information about their existence. If they exist answer with yes and provide me with the official URL, else with no"
    print(userprompt)
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar-small-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": userprompt
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": ""     #Hier muss ein API Key hin
    }

    response = requests.post(url, json=payload, headers=headers)

    # Der gegebene JSON-String
    json_data = response.text

    # Konvertiere den JSON-String in ein Python-Dictionary
    data = json.loads(json_data)

    # Extrahiere den Inhalt des Content-Teils
    content = data['choices'][0]['message']['content']

    # Drucke den Inhalt
    print(content)
    return content

def main():
    st.title('Firmenexistenz überprüfen')

    # Excel-Datei hochladen
    uploaded_file = st.file_uploader("Excel-Datei hochladen", type=["xlsx"])

    # Chatfunktion
    prompt = st.text_input("Enter company name:")

    if prompt:
        st.write(f"You entered: {prompt}")
        exists = firma_existiert(prompt)
        st.write(f"Company '{prompt}' exists: {exists}")

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

        # Ergebnisse speichern
        results = []

        for index, row in df.iterrows():
            firmenname = row['firmenname']  # Annahme: Die Spalte mit den Firmennamen heißt "Firmenname"
            exists = firma_existiert(firmenname)
            url = ""  # Platzhalter für die URL
            adresse = ""  # Platzhalter für die Adresse der Firma
            results.append({'Firmenname': firmenname, 'Existiert': exists, 'URL': url, 'Adresse': adresse})

        # Ergebnisse in einer Tabelle anzeigen
        result_df = pd.DataFrame(results)
        st.write("Ergebnisse:")
        st.table(result_df)

        # Button zum Exportieren der Ergebnisse als CSV hinzufügen
        csv = result_df.to_csv(index=False)
        st.download_button(
            label="CSV herunterladen",
            data=csv,
            file_name='firmen_existenz_results.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
