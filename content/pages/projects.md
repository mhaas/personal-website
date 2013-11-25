Title: Projects & Software
Author: Michael Haas
Slug: software-projects-michael-haas
Lang: en

Here's a list of projects I have been working on. Some are university projects,
some are just smaller tools I have developed for my own needs.
You can find more things on my [GitHub account](https://github.com/mhaas?tab=repositories).

Bachelor's Thesis <span class="item-date">2011</span>
=====================================================
My bachelor's thesis:
> "Analyse von Netzwerken zwischen Pharma-Firmen sowie von
klinischen Studien auf die Frage, ob befreundete Firmen noch ihre
Produkte gegeneinander testen"

In English:
> "Analyzing a pharma company network: Are friends still competing?"

My Bachelor's thesis was supervised by Prof. Dr. Stefan Riezler and
Prof. Dr Gerhard Reinelt. Research was done in
the junior research group "Network Analysis and Graph Theory" led by
[Dr. Nina Zweig](http://www.ninasnet.de/) at the Interdisciplinary Center
for Scientific Computing.

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Thesis PDF](|filename|/downloads/ba-thesis/ba.pdf)

* [Slides for thesis defense, German, PDF](|filename|/downloads/ba-thesis/pres_pruefung.pdf)

</div>


University Projects
===================
Most of these projects were done as part of course work and are not necessarily
production quality. They are intended to serve as proof of concept for
design and algorithm implementation.


Multimodal Distributional Semantics <span class="item-date">2013</span>
-----------------------------------------------------------------------
Traditional distributional models of meaning are built from large text corpora.
However, many things go unmentioned in text. As McClelland puts it,
the traditional approach to distribution semantics is like "learning meaning
by listening to the radio". By integrating other modalities, such as images,
we can improve our semantic models.

In this project, I try to enhance prediction of semantic relations between
head nouns and modifier nouns by integrating pictoral data from
[ImageNet](http://www.image-net.org/). For example, the QUALITY relation
holds for the noun phrase "brick house". I extract image features
from pictures showing [bricks](http://www.image-net.org/synset?wnid=n02897820) and
[houses](http://www.image-net.org/synset?wnid=n03544360) to improve prediction performance.
Image features are extracted as SIFT descriptors using the [OpenCV](http://www.opencv.org/)
framework. The code is written in Python and C++.

This project was done as course work for the course
["Distributionelle Semantik jenseits der Wortbedeutung"](http://www.cl.uni-heidelberg.de/courses/ss13/distribsem/).
The multimodal approach is inspired by presentations from the seminar
["Multimodale Semantik"](http://www.cl.uni-heidelberg.de/courses/ss13/multisem/).

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Source on GitHub](https://github.com/mhaas/semrel-pictoral)
* [Project Report](|filename|/downloads/semrel-pictoral/report.pdf)
* [Slides on related paper](|filename|/downloads/semrel-pictoral/slides.pdf)

</div>



Twitter Sentiment Analysis <span class="item-date">2013</span>
--------------------------------------------------------------
Social Media Monitoring has become an important research
focus. Applications range from reputation monitoring to earthquake detection.

In this project, we adapt and extend existing approaches to the German language
to build a sentiment polarity classifier for German tweets. As a basic use case,
we would like to get a feeling if the sentiments towards a currently trending topic
such as '#tatort' are positive or negative.

This project was done by Tilman Wittl and myself as course work
for the course ["Text Mining"](http://www.cl.uni-heidelberg.de/courses/ws12/textmining/).

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Source on GitHub](https://github.com/mhaas/twitter-sentiment-analysis)
* [Project Report, PDF](|filename|/downloads/twitter-sentiment-analysis/report.pdf)

</div>

Distributed Web Crawler <span class="item-date">2012</span>
-----------------------------------------------------------
A distributed web crawler and indexer written in Hadoop. It starts with a small list
of URLs and iteratively expands its index from there. A simple boolean query model
is supported.

This project was done as course work for the course
["Advanced Programming"](http://www.cl.uni-heidelberg.de/courses/ss12/advancedprog/).


<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Source on GitHub](https://github.com/mhaas/distributed-crawl)

* [Project report, PDF](|filename|/downloads/distributed-crawler/report.pdf)

* [Flowchart, PNG](|filename|/downloads/distributed-crawler/flowchart.png)

</div>

GIVE-2: Natural Language Generation in Virtual Environments <span class="item-date">2010</span>
---------------------------------------------------------------------------------------
The goal of the GIVE-2 challenge is to generate directions in a virtual 3D environment
which direct the user to a well-hidden trophy. GIVE-2 systems create directions in
natural language based on an abstract plan provided by the GIVE framework.

This project was jointly done by Eric Hildebrand, Eleftherios Matios and myself as course
work for the course
["Natural Language Generation for Virtual Environments"](http://www.cl.uni-heidelberg.de/courses/ws09/generation/).

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Michael Roth, Michael Haas, Eric Hildebrand, Eleftherios Matios: The Heidelberg GIVE-2 System, presented during Generation Challenges Poster Session at INLG 2010 in Dublin, PDF](|filename|/downloads/give2/GIVE-2-Heidelberg.pdf)

* [Term paper: "Content Selection in Natural Language Generation Systems", PDF](|filename|/downloads/give2/hausarbeit.pdf)

</div>

RECIPE: Recipe Event Chain Imperative Processing Engine <span class="item-date">2010</span>
-------------------------------------------------------
Narratives contain chains of events. The RECIPE project extracts common event chains from cooking recipes from a basic logic representation
of the instructions contained therein.

This project was jointly done by Hiko Schamoni, Tilman Wittl, Britta Zeller and myself as "Softwareprojekt" as
required by the Bachelor of Arts curriculum at the University of Heidelberg.

<h3 class="item-ressources-header">Ressources</h3>
<div class="item-ressources" markdown>

* [Michael Haas, Hiko Schamoni, Tilman Wittl, Britta Zeller: Recipe Event Chain Imperative Processing Engine, Poster, PDF]()

</div>


Software
========
Leechi <span class="item-date">2012</span>
-------------------------------------------
Leechi is a small Python library to automate downloads from web servers
without drawing too much attention to oneself.

Leechi was developed as part of my work at the
[Forschungsdaten Service Center](http://service.informatik.uni-mannheim.de/).

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>

* [Leechi on GitHub](https://github.com/mhaas/leechi)

* [Leechi on Pypi](https://pypi.python.org/pypi/Leechi/)

</div>


Tutorials
=========
Screen Scraping & BeautifulSoup <span class="item-date">2013</span>
-------------------------------------------------------------------
I have given a presentation on Information Extraction using
HTML scraping with Python and
BeautifulSoup as part of my work at the
[Forschungsdaten Service Center](http://service.informatik.uni-mannheim.de/).
Slides and code are available.

<h3 class="item-ressources-header">Ressources</h3>

<div class="item-ressources" markdown>
* [Repository on GitHub](https://github.com/mhaas/tutorial-screen-scraping)

* [Slides, German, PDF](|filename|/downloads/tutorial-screen-scraping/slides.pdf)
</div>



