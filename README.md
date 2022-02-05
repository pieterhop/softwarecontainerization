Software Containerization (Group 4)
-
<h3>How to get it up and running on k8s: </h3>

 1. Clone this repo.
 2. cd to softwarecontainerization/helm_chart
 3. run `helm install . --generate-name ` on google kubernetes engine or, <br> run `microk8s helm3 install . --generate-name` on local machine / microk8s.
 4. The app can be accessed on port 30002, or on the IP of Google Cloud's load balancer, which can be seen in the ingress section of google kubernetes engine.
 ---
 <h3> Details about our project </h3>
 
---
We made a to-do list which can:
 - Add Tasks
 - Delete Tasks
 - Filter tasks as Completed or Active

![how the app looks](https://i.imgur.com/1Cr2hYy.png)

It has 3 components:

 1. The Front-end, made using ReactJS.
 2. The API server, made using Python-Flask.
 3. The database, which is a postgres DB.
 
All the components mentioned above run in their own containers and are exposed via services called `inventory-ui-service`, `inventory-api-service` and `postgres-service` respectively.
We also have 2 ingress rules that allow https connections to the UI and API called `ui-ingress` and api-`ingress` respectively.
