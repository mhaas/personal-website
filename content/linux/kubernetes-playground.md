Title: Playing around with Kubernetes
Date: 2018-03-20
lang: en
tags: docker, kubernetes, devops

## Containerizing an application and deploying to Kubernetes Engine on Google Cloud Platform ##

For last weekend's coding exercise, I played around with Kubernetes Engine on Google Cloud Platform.
GCP offers a nice trial period where you get USD300 worth of credits on top of the already free
monthly resource allotments. Definitely [check it out!](https://cloud.google.com/free/)

I had initially planned to containerize an old project: the backend part of our Twitter sentiment
analysis project. It consists of multiple web services implemented in Perl and Python. A perfect example:
each microservice goes into its own Docker image with it its own dependencies. Each service is then
independently deployed to Kubernetes.

Since each service has different CPU usage requirements, the built-in autoscaling would have been very
welcome. After all, the Bayes classifier likely requires more CPU than the feature extraction microservice.
It makes sense to have more instances of the classifier running, with Kubernetes automatically distributing
and scaling the workload.

Sadly, I do not have access to the trained model files anymore.

To still get started, I containerized and deployed [TensorFlask](https://github.com/JoelKronander/TensorFlask),
a toy image classification service based on TensorFlow.

The `Dockerfile` is simple enough:

<script src="https://gist.github.com/mhaas/b4bc912eac7c34f50c54aeb4a486ac47.js"></script>

You can find the `Dockerfile` and the Kubernetes Engine deployment scripts [on my Github](https://github.com/mhaas/gcp-k8s-playground).

Kubernetes and GCP in particular really are great fun. See below for an example session:

[![asciicast](https://asciinema.org/a/wG7Zq3UC9yuqJctOo67JTQ07w.png)](https://asciinema.org/a/wG7Zq3UC9yuqJctOo67JTQ07w) 
