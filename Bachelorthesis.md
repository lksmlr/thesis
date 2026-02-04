# Bachelorarbeit

## Aufbau

### 1. Einleitung

- Motivation
  - demografischer Wandel / Fachkräftemangel
  - erhöhtes Aufkommen von Anträgen
  - schnellere Bearbeitung
  - Entlastung der Mitarbeiter

- Problemstellung
  - handschriftliche Erkennungen
  - aktuelles Verfahren erklären
  - Warum / Wo stößt es an Grenzen?
  - Herausforderung unstrukturierte Daten (Scans, schiefe Dokumente, ...)

- Zielsetzung
  - Prototyp entwickeln der Dokumente erkennt und JSON extrahiert
  - Vergleich von verschiedenen Modellen
  - Forschungsfragen einbeziehen
  - Abgrenzung der Arbeit (Keine vollständige Integration in das bestehende System)


### 2. Theoretische Grundlagen

- kurze Erklärung VLLMs
- kurze Vorstellung der verschiedenen Modelle
- Fine-Tuning Methoden
- Vergleichbare Arbeiten einbeziehen
- Infrastruktur in der BA / Besonderheiten
- Dokumentenarten vorstellen

### 3. Methodik und Datenaufbereitung


- Wie habe ich die Daten gelabelt
- Was waren Test und Trainingsdaten
- jeweilige Besonderheiten
- Problemfälle schildern
- Welche Felder werden extrahiert und warum sind diese relevant?
  - Schwierigkeiten bei einzelnen Feldern


### 4. Implementierung

- Promptdesign, Entwicklung des Prompts
- Auswahl des Modells
  - Architektur der Pipeline
  - Ressourcenverbrauch der einzelnen Modelle
  - Fehlerbehandlung des Outputs
  - Endgültige Auswahl

- Fine-Tuning
  - Architektur der Pipeline
  - Framework
  - Messung des Ressourcenverbrauchs

- Was war die Evaluierungsstrategie? / Wie wurde sie implementiert?
- Field F1-Score
- Structural-Score vs Content-Score
- Comparator
- Schemas


### 5. Ergebnisse

- Ergebnisse der aktuellen Pipeline
- Ergebnisse Qwen, Pixtral
- Ergebnisse Fine-Tuning


## 6. Diskussion

- Vergleich der Modelle
  - Performance
  - Wie konstant war der JSON Output?
  - Base Modell Probleme bei Handwerkskammer wo die Daten in Kästchen stehen
- Wie groß ist der Aufwand die Anwendung umzustellen auf ein LLM?
- Wo machen die Modelle Fehler?
- Was ist an der Implementierung eventuell zu verbessern?
- Was können die Modelle besonders gut?
- Logikfehler im dokument wie das bei kg5b beides angekreuzt wird funktioniert besser
- eingehen auf schlechtes Dokument aus 3. Datenbasis

### 7. Fazit und Ausblick

- Wie geht es weiter?
- Wird das LLM die Pipeline ersetzen?

## Zeitplan

### Daten, Vorbereitung, Anbindung

- Testkonstellationen aufstellen    ✓
- KubeFlow Anbindung                ✓
- Modelle herunterladen             ✓
- Prompting techniques              ✓
- Literatur lesen                   ✓
- Anmeldeformular abgeben           ✓
- Wie speichere ich die Daten       ✓
- Tägliches Doing erfassen          ✓

### Testen, FineTuning, Anfang schreiben

- Modelle testen                    ✓
- Ergebnisse persistieren           ✓
- Wie FineTuned man?                ✓
- Beginn Bachelorarbeit             ✓
- Austausch mit Experten            ✓
- Literaturarbeit beenden           ✓
- Vortrag vorbereiten               ✓
- Termin für Vortrag festsetzen     ✓
    - neues Verfahren!!!
- Inhaltsangabe schreiben           ✓

### Schreiben der Arbeit, Vortrag

- Vortrag halten                    ✓
- Bachelorarbeit schreiben          O
- Vorstellung Ergebnisse auf Arbeit X
- Abgabe                            X

Alte Ergebnisse Qwen 7B Base Model:
KG5b:     0.82
Vertrag:  0.59
Sonstige: 0.80

Neue Ergebnisse Qwen 7B Base Model:
KG5b:     0.79
Vertrag:  0.84
Sonstige: 0.83

# Fragen:

- Feedback Vortrag
- Gleichheit statt Similarity, Schwellenwerte statt Thresholds?
- Präsens?
- Weitere Grundlagen ja/nein?
- Wo Kritik äußern?
- Statt Methodik und Datenaufbereitung nur Methodik und Daten?
- Ergebnisse basismodelle extra, oder reicht Überblick
- Testdatensatz -> Modellauswahl -> Trainingsdatensatz?
- In Zusammenfassung Ergebnis nennen?
- Niemals referenzieren? Beispiel Trainingsdatensatz