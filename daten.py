class Frage:
    def __init__(self, text, richtige_antwort, falsche_antworten):
        self.text = text
        self.richtige_antwort = richtige_antwort
        self.falsche_antworten = falsche_antworten

fragen = [
    Frage("Ca. wieviele Charaktere gibt es in FF14?", "13 Mio", ["20 Mio", "8 Mio"]),
    Frage("Welche ist die am häufigsten gespielt männliche Rasse?", "Hyur", ["Miqo'te", "Lalafell"]),
    Frage("Welche ist die am häufigsten vertretene Klasse?", "Barde", ["Paladin", "Weißmagier"]),
    Frage("Wieviele Datenzentren gibt es aktuell?", "77", ["83", "65"]),
    Frage("Wieviele Hochzeiten gab es ca. Ingame (ewiger Bund)?", "400000", ["200,000", "1 Mio"]),
    Frage("Wer ist der Schutzgott von Ul'dah?", "Nald'thal", ["Thaliak", "Halone"]),
    Frage("Die Miqo'te (Sonnentatzen) haben am Anfang ihres Namens einen Buchstaben, der ihren Stamm repräsentiert. Der Name steht jeweils für ein Tier, wofür steht das M?", "Murmelhörnchen", ["Mull", "Morbol"]),
    Frage("Wie viele Ätheryten gibt es im Spiel?", "2155", ["736", "1,498"]),
    Frage("Lalafell sind die kleinste Rasse im Spiel. Was ist die geringste Größe, die man wählen kann?", "86.9 cm", ["79,2 cm", "90,8 cm"]),
    Frage("Der Gold Saucer stammt ursprünglich aus welchem Teil?", "7", ["9", "11"]),
    Frage("Das Kartenspiel Triple Triad stammt aus Teil 8. Wie hieß es dort?", "Balamb Card", ["Stratego Card", "Monster Card"]),
    Frage("Wie viele Baurezepte (alle Kategorien) hat derzeit der Gourmet?", "719", ["553", "1012"]),
    Frage("Die Revolverklinge stammt ursprünglich aus welchem Teil?", "8", ["7", "10"]),
    Frage("Wie viele Dungeons gibt es derzeit?", "86", ["65", "73"]),
    Frage("Wie viele unterschiedliche Färbemittel gibt es?", "114", ["98", "132"]),
    Frage("Im eorzäischen Kalender entspricht der 3. Lichtmond welchem Monat?", "Juni", ["Februar", "Oktober"]),
    Frage("Wie viele Handwerksberufe gibt es?", "8", ["7", "9"]),
    Frage("Das Volk der Viera stammt ursprünglich aus welchem Teil?", "12", ["10", "9"]),
    Frage("Wer gehörte nicht zum Konvent der 14?", "Travanchet", ["Fandaniel", "Lahabrea"]),
    Frage("Wie viele Rüstungssets kann ausschließlich der Paladin (inkl. Gladiator) tragen?", "18", ["9", "27"]),
    Frage("Wie viele Gegenstandsfächer kann die Gildentruhe maximal haben?", "5", ["4", "6"]),
    Frage("Wie viele Skills kann der Blaumagier erlernen?", "104", ["85", "131"]),
    Frage("Wie heißt die Mutter von Hildibrand Manderville?", "Julyan", ["Imme", "Alistair"]),
    Frage("Wie viele Gegenstände können in einem Haus der Größe L maximal platziert werden?", "400", ["300", "500"]),
    Frage("Alle wie viel Stunden kann man Schatzkarten finden?", "18", ["16", "20"]),
    Frage("Wie viel Gil kann man maximal wöchentlich beim Aufbau der domanischen Enklave erhalten?", "40000", ["30000", "50000"]),
    Frage("Wie lange benötigt der Jute-Samen nach Anbau, bis er ausgewachsen ist?", "7 Tage", ["5 Tage", "3 Tage"]),
    Frage("Wie viele S-Rang Kopfgeldziele gibt es?", "41", ["28", "53"]),
    Frage("Wie viele Gegenstände fasst die Chocobo-Satteltasche?", "70", ["100", "85"]),
    Frage("Wie viele Fischer enthält das Fischverzeichnis?", "1378", ["936", "1604"]),
    Frage("Wie viele Windätherquellen gibt es (inkl. durch Missionen)?", "248", ["176", "212"]),
    Frage("Wie oft muss man zum wertvollsten Spieler ernannt werden, um den Parade-Chocobo zu erhalten?", "3000", ["2000", "1000"]),
    Frage("Wie viele Herausforderungen muss man abschließen, um in der wöchentlichen Agenda Stufe 5 abzuschließen?", "30", ["35", "25"]),
    Frage("Wie viele Monster umfasst das Bestarium - alle Klassen einbezogen?", "450", ["350", "550"]),
    Frage("Wie viele Rüstungsteile können maximal in der Projektionskommode verstaut werden?", "400", ["200", "300"]),
]
