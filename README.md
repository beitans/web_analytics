# web_analytics
developing a system to generate insight out of variouse internet data sources like e-mail Newsletter; RSS- Feeds and press releases


E-Mail Newsletter Analysis
a data Science project by Florian Beitans    - 


 Inhalt

Inhalt	1
Einleitung	1
Zielsetzung	1
Motivation & Relevanz	2
Weitere Überlegungen	3
Rahmenbedingungen	3
Allgemeine Rahmenbedingungen	3
Technische Rahmenbedingungen	3
P	3

Einleitung
Zielsetzung
Das Ziel dieses Projektes ist es zweiseitiger Natur. Auf der einen Seite soll hiermit eine Simulation eines beruflichen Projektes erfolgen. Es ist dahingehend als Übung zu betrachten um strukturiert ein lauffähiges, gut dokumentiertes und robustes Projekt durchzuführen. Es soll als Simulation eines beruflichen Projektes gesehen werden, welches am Ende der Projektdauer abzugeben ist. Als solches wird dieses dann als Beispielprojekt auf meine Website, welche noch anzulegen ist, hochgeladen. 
Das andere Projektziel ist es für mich selber ein nötiges Stück Software zu schaffen und mit der Allgemeinheit zu teilen. Dieses Software muss:
E-Mail Newsletter sammeln und in einer Datenbank strukturiert speichern
Den Inhalt von E-Mail Newsletter, sowie den Betreff und den Absender extrahieren und strukturiert speichern
Eine Zerlegung in einzelne Sätze vornehmen und dieses strukturiert speichern
Gut Dokumentiert sein
Eine Option besitzen, in der jede E-Mail nach definierbaren Keywords durchsucht wird und bei Vorkommen eines dieser Keywords den Benutzer via E-Mail benachrichtigt und die entsprechenden E-Mails gesondert in der Datenbank kennzeichnet

Dieses Software kann außerdem folgende Features bekommen, wenn dies während der Entwicklungszeit entschieden wird.
Algorithmen des Maschinellen Lernen nutzen, um den Inhalt von E-Mail Newslettern zu analysieren und bewerten
Events identifizieren und strukturiert speichern


Motivation & Relevanz
Die Motivation für dieses Projekt rührt daher, dass es bei mir privat einen großen Nutzen für diese Anwendung gibt. Es ist in der heutigen Zeit immer wichtiger aktuelle Entwicklungen zu verfolgen und strategisch relevante Informationen zu besitzen. E-Mail Newsletter sind dabei eine nicht zu verachtende Datenquelle mit sehr großem Potential. Das liegt daher, dass Autoren von E-Mail Newslettern einen Mehrwert für interessierte Abonnenten bieten wollen und einen eigenen Nutzen im halten der Nutzer haben.
Ich selber bin seit vielen Jahren Abonnent von dutzenden Newslettern. Was allerdings bei dieser Form der Informationsbeschaffung als ein negativer Aspekt mit einhergeht, ist die Tatsache, dass bei einer größeren Anzahl von Newslettern die Menge an Text kaum händelbar wird. Außerdem doppeln sich, vor allem bei Newslettern aus den Gleichen Themenkomplexen, die Informationen häufig.
Der durchschnittliche Newsletter hat 14000 Worte und wird 3 mal pro Woche versendet. Für dieses Projekt wird angestrebt, zwischen 100 und 500 Newsletter als Informationsquelle zu abonnieren. Das würde bedeuten, dass an einem durchschnittlich Tag 200000 Worte dem Nutzer zugeschickt werden. Dies entspricht ca. 200 DinA4 Seiten. Eine, für einen Menschen, nicht händelbare Menge an, zu diesem Zeitpunkt quasi nur noch beschreibbar als, Daten.
Darüber hinaus können aus der Menge an Daten nützliche Informationen extrahiert werden und dem Nutzer zugänglich gemacht werden. An dieser Stelle ein Beispiel:
Wenn in einem Newsletter der Begriff “Dekarbonisierungsstrategie” fällt kann man es als eine Wortneuschöpfung des Autors abtun. Hat man allerdings aus dem gleichen technischen Sektor beispielsweise 20 Newsletter abonnieren und alle nutzen ab einem gewissen Zeitpunkt regelmäßig dieses Wort kann eine genauere Überprüfung der Vokabel ratsam sein. Beispielsweise könnte es sich hier um eine neue von der Regierung erlassene Strategie handeln, welche Subventionen, Änderungen an aktuellen Regelungen oder allgemein neue Geschäftschancen mit sich bringt.
Weitere Überlegungen

Rahmenbedingungen
Allgemeine Rahmenbedingungen
Um dem ganzen einen formalen Rahmen zu geben, wird dieses private Projekt behandelt als würde es sich um einen beruflichen Auftrag handeln. Es wurde in einer eigenen Website eine Zeitmessung realisiert, mit dem der der Fortschritt dokumentiert werden soll. Die vorgesehene Zeit beträgt mindesten 100 Stunden und maximal 350 Stunden. Der 31.08.2021 ist als Start Zeitpunktes des Projekt festgelegt worden. Die Bearbeitungsdauer beträgt 60 Tage.
Über die Technische Implementierung heraus soll dieses mindestens 8 Seitige Dokument genutzt werden, um den Aufbau zu beschreiben und den Code, über die normalen In-Code-Comments heraus, zu dokumentieren. Bearbeitet wird dieses Projekt ausschließlich von Florian Beitans und am Ende der Dauer für die private Website verwendet, sowie auf GitHub veröffentlicht.
Technische Rahmenbedingungen
Für dieses Projekt wurde die E-Mail Adresse “beitans.newsletter@gmail.com” angelegt und wird als Eingangstor für die abonnierten Newsletter verwendet. Das ganze Projekt soll später in einem Docker Container bereit gestellt werden.
P

