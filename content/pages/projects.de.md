Title: Projekte
Author: Michael Haas
Slug: software-projects-michael-haas
Lang: de

Hier finden Sie eine Liste meiner Projekte. Einige Projekte entstanden
im Rahmen meines Studiums, andere aufgrund persönlicher Bedürfnisse.
Mehr Software finden Sie auf meinem [GitHub account](https://github.com/mhaas?tab=repositories).


Masterarbeit <span class="item-date">2014</span>
=====================================================
Meine Master-Arbeit:
> "Weakly Supervised Learning for Compositional Sentiment Recognition"

Meine Master-Arbeit wurde von [Dr. Yannick Versley](http://www.versley.de/) betreut,
mit Prof. Dr. Anette Frank als Zweitprüfer.
Genauere Informationen befinden sich auf einer
[eigenen Seite zu meiner Master-Arbeit](ma-thesis).

<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>

* [Thesis PDF](|filename|/downloads/ma-thesis/Master_Thesis-Michael_Haas-Weakly_Supervised_Learning_for_Compositional_Sentiment_Recognition.pdf)

* [Code auf GitHub](https://github.com/mhaas/ma-thesis)

</div>

Bachelor-Arbeit <span class="item-date">2011</span>
=====================================================
Meine Bachelor-Arbeit:
> "Analyse von Netzwerken zwischen Pharma-Firmen sowie von
klinischen Studien auf die Frage, ob befreundete Firmen noch ihre
Produkte gegeneinander testen"

Meine Bachelorarbeit wurde von Prof. Dr. Stefan Riezler und Prof. Dr.
Gerhard Reinelt betreut. Die Arbeit entstand in der Juniorforschungsgruppe
"Network Analysis and Graph Theory" von [Dr. Nina Zweig](http://www.ninasnet.de/)
am Interdisziplinären Zentrum für wissenschaftliches Rechnen der
Universität Heidelberg.

<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>

* [Bachelor-Arbeit, PDF](|filename|/downloads/ba-thesis/ba.pdf)

* [Vortrag Bachelor-Arbeit, Deutsch, PDF](|filename|/downloads/ba-thesis/pres_pruefung.pdf)

</div>


Projekte Studium
===================

Die meisten dieser Projekte entstanden als Hausarbeiten und sind nicht als
fertige, ready-to-run Lösungen gedacht, sondern als Machbarkeitsstudien
für Design und Implementierung der Algorithmen.

Multimodale Distributionelle Semantik <span class="item-date">2013</span>
-----------------------------------------------------------------------
Traditionelle distributionelle Modelle der Semantik basieren auf Statistiken
über großen Textkorpora. Viele Bedeutungsfacetten werden in Texten allerdings nicht
berücksichtigt. Dieser traditionelle Ansatz der Bedeutungsrepräsentation ist
daher ein wenig, wie "Radio zu hören, um Bedeutung zu lernen" (McClelland).
Durch Integration anderer Modalitäten wie beispielsweise Bilder können wir die
Modelle allerdings verbessern.


In diesem Projekt versuche Ich, die Vorhersage semantischer Relationen zwischen
Kopf einer Nominalphrase und ihres Modifikators zu verbessern. Das geschieht
durch Integration von Bilddaten aus [ImageNet](http://www.image-net.org/).
Zum Beispiel ist QUALITY die semantische Relation für "brick house". Durch Integration von
Bild-Features für ["brick"](http://www.image-net.org/synset?wnid=n02897820)
und ["house"](http://www.image-net.org/synset?wnid=n03544360) in das
semantische Model will ich die Performance des Systems verbessern.
Bild-Features werden über die SIFT-Implementierung des [OpenCV](http://www.opencv.org/)-Frameworks
extrahiert. Das Projekt ist in C++ und Python implementiert.

Diese Hausarbeit entstand für den Kurs
["Distributionelle Semantik jenseits der Wortbedeutung"](http://www.cl.uni-heidelberg.de/courses/ss13/distribsem/).
Der multimodale Ansatz ist inspiriert durch Präsentation aus dem Seminar
["Multimodale Semantik"](http://www.cl.uni-heidelberg.de/courses/ss13/multisem/).


<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>

* [Quelltext und Daten auf GitHub](https://github.com/mhaas/semrel-pictoral)

* [Ausarbeitung](|filename|/downloads/semrel-pictoral/report.pdf)

* [Folien zu verwandtem Papier](|filename|/downloads/semrel-pictoral/slides.pdf)

</div>



Twitter Sentiment Analysis <span class="item-date">2013</span>
--------------------------------------------------------------

Die Überwachung und Beobachtung sozialer Medien wie Twitter ist ein
wichtiger Forschungsbereich geworden. Anwendungen umfassen
Reputationsmonitoring für Unternehmen bis hin zur Früherkennung von Erdbeben.

In diesem Projekt erweitern wir bestehende Ansätze zur Sentiment-Analyse auf
die deutsche Sprache mit dem Ziel, die Polarität des Sentiments von deutschen
Tweets in *positiv*, *negativ* oder *neutral* zu klassifizieren.
Ein grundlegender Anwendungsfall wäre die Überwachung der Stimmung bezüglich
trending topics wie *#tatort*.

Dieses Projekt ist noch nicht abgeschlossen. Bearbeitet wird es von Tilman Wittl
und mir als Hausarbeit für den Kurs 
["Text Mining"](http://www.cl.uni-heidelberg.de/courses/ws12/textmining/).

<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>

* [Quelltext, GitHub](https://github.com/mhaas/twitter-sentiment-analysis)
* [Project Report, PDF](|filename|/downloads/twitter-sentiment-analysis/report.pdf)

</div>

Distributed Web Crawler <span class="item-date">2012</span>
-----------------------------------------------------------
Ein verteilter Crawler und Indizierer für das Web, geschrieben in Hadoop.
Ausgehend von einer initialen Liste von Websites vergrößert der Crawler
iterativ seinen Index. Ein boolsches Abfragemodell wird unterstützt.

Dieses Projekt entstand als Hausarbeit für den Kurs
["Advanced Programming"](http://www.cl.uni-heidelberg.de/courses/ss12/advancedprog/).


<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>

* [Quelltext, GitHub](https://github.com/mhaas/distributed-crawl)

* [Dokumentation, Englisch, PDF](|filename|/downloads/distributed-crawler/report.pdf)

* [Flowchart, PNG](|filename|/downloads/distributed-crawler/flowchart.png)

</div>

GIVE-2: Natural Language Generation in Virtual Environments <span class="item-date">2010</span>
---------------------------------------------------------------------------------------

Ziel der GIVE-2-Challenge ist die Erzeugung von Navigationsanweisungen in einer
virtuellen 3D-Umgebung, die den Benutzer zu einer versteckten Trophäe lotsen.
Die Anweisungen werden in natürlicher Sprache ausgehend von einem abstrakten
Plan des GIVE-Frameworks erzeugt.

Dieses Projekt wurde erarbeitet von Eric Hildebrand, Elftherios Matios und mir als
Hausarbeit für den Kurs
["Natural Language Generation for Virtual Environments"](http://www.cl.uni-heidelberg.de/courses/ws09/generation/).

<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>

* [Michael Roth, Michael Haas, Eric Hildebrand, Eleftherios Matios: The Heidelberg GIVE-2 System, presented during Generation Challenges Poster Session at INLG 2010 in Dublin, PDF](|filename|/downloads/give2/GIVE-2-Heidelberg.pdf)

* [Hausarbeit, Englisch, PDF: "Content Selection in Natural Language Generation Systems", PDF](|filename|/downloads/give2/hausarbeit.pdf)

</div>

RECIPE: Recipe Event Chain Imperative Processing Engine <span class="item-date">2010</span>
-------------------------------------------------------
Geschichten und Erzählungen enthalten Ketten von Ereignissen.
Das RECIPE-Projekt extrahiert häufige Ereignisketten aus Kochrezepten
ausgehend von einer Logik-Repräsentation der Instruktionen.

Dieses Projekt wurde als *Softwareprojekt* von Hiko Schamoni, Tilman Wittl,
Britta Zeller und mir erarbeitet. Das Softwareprojekt ist Bestandteil
des Curriculums B.A Computerlinguistik an der Universität Heidelberg.

<h3 class="item-ressources-header">Ressourcen</h3>
<div class="item-ressources" markdown>

* [Michael Haas, Hiko Schamoni, Tilman Wittl, Britta Zeller: Recipe Event Chain Imperative Processing Engine, Poster, PDF]()

</div>


Software
========
Leechi <span class="item-date">2012</span>
-------------------------------------------
Leechi ist eine kleine Bibliothek für Python. Ziel ist, automatische
Downloads von Webservern so zu gestalten, dass nicht zu viel Last erzeugt wird.
So wird unnötige Erregung von Aufmerksamkeit vermieden.

Leechi wurde im Rahmen meiner Arbeit am 
[Forschungsdaten Service Center](http://service.informatik.uni-mannheim.de/)
entwickelt.

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Leechi auf GitHub](https://github.com/mhaas/leechi)

* [Leechi auf Pypi](https://pypi.python.org/pypi/Leechi/)

</div>


Tutorials
=========
Screen Scraping & BeautifulSoup <span class="item-date">2013</span>
-------------------------------------------------------------------
Ich habe eine Präsentation zum Thema Informationsextraktion aus
Websites mit Python und BeautifulSoup gegeben. Die Präsentation
entstand im Rahmen meiner Arbeit am 
[Forschungsdaten Service Center](http://service.informatik.uni-mannheim.de/).

Folien und Quelltext sind verfügbar.

<h3 class="item-ressources-header">Ressourcen</h3>

<div class="item-ressources" markdown>
* [Code auf GitHub](https://github.com/mhaas/tutorial-screen-scraping)

* [Folien, PDF](|filename|/downloads/tutorial-screen-scraping/slides.pdf)
</div>



