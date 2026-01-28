## 1. Einleitung

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


## 2. Theoretische Grundlagen

- kurze Erklärung VLLMs
- kurze Vorstellung der verschiedenen Modelle
- Fine-Tuning Methoden
- Vergleichbare Arbeiten einbeziehen
- Infrastruktur in der BA / Besonderheiten

## 3. Datenbasis und Datenschutz

- Dokumentenarten vorstellen
- Wie habe ich die Daten gelabelt
- Was waren Test und Trainingsdaten
- jeweilige Besonderheiten
- Problemfälle schildern
- Welche Felder werden extrahiert und warum sind diese relevant?
  - Schwierigkeiten bei einzelnen Feldern


## 4. Implementierung

- Auswahl des Modells
  - Architektur der Pipeline
  - Promptdesign, Entwicklung des Prompts
  - Ressourcenverbrauch der einzelnen Modelle
  - Fehlerbehandlung des Outputs
  - Endgültige Auswahl

- Fine-Tuning
  - Architektur der Pipeline
  - Framework
  - Messung des Ressourcenverbrauchs


## 5. Evaluation

- Was war die Evaluierungsstrategie? / Wie wurde sie implementiert?
  - Field F1-Score
  - Structural-Score vs Content-Score
  - Comparator
  - Schemas
- Ergebnisse der aktuellen Pipeline
- Vergleich der Modelle
  - Performance
  - Wie konstant war der JSON Output?
  - Base Modell Probleme bei Handwerkskammer wo die Daten in Kästchen steht


## 6. Diskussion

- Wie groß ist der Aufwand die Anwendung umzustellen auf ein LLM?
- Wo machen die Modelle Fehler?
- Was ist an der Implementierung eventuell zu verbessern?
- Was können die Modelle besonders gut?
- Logikfehler im dokument wie das bei kg5b beides angekreuzt wird funktioniert besser
- eingehen auf schlechtes Dokument aus 3. Datenbasis

## 7. Fazit und Ausblick

- Wie geht es weiter?
- ToolCall für Datum?
- Wird das LLM die Pipeline ersetzen?