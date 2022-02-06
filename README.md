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
___
<h3>Below we describe parts of the project according to the grading rubric</h3>

---
1. **Persistent layer (SQL or No-SQL database)**<br/>
	We have created a deployment for the postgresql DB called `postgres-deployment`, along with a persistent volume and a persistent volume claim called `postgres-pv-claim`. <br/> The database is exposed via a service called `postgres-service`. <br/> The credentials for the database is stored in a secret called `postgres-secret`. <br/>All the yaml files for the database are in the directory `/helm_chart/charts/db/templates`.
2. **REST API**	<br/>
	We have made an API server with python-flask which handles GET, POST and DELETE requests to the database. The API is exposed via a service called `inventory-api-service`. <br/> Since our front-end is client-side rendered, it means the requests to the API from the front-end will be coming from the client's browser, and not from somewhere within our k8s cluster. So we have decided to make a `NodePort` for the `inventory-api-service`. <br/> We have also made an ingress called `api-ingress` to serve requests over https with a self-signed certificate.<br/> All the yaml files for the API are in the directory `/helm_chart/charts/api/templates`.
	
3. **Web front-end**<br/>
	The front-end is made using ReactJS. <br/>It is exposed via a service called `inventory-ui-service`, which uses a `NodePort` since the requests to the front-end will be coming from outside the cluster.<br/>We also have an ingress called `ui-ingress` to serve requests over https with a self signed certificate. <br/>All the yaml files for the front-end are in the directory `/helm_chart/templates`.
4. **Transport Level Security**<br/>
	We have configured TLS and serve https requests by using a self-signed certificate generated with openssl. 
	The key and certificate secrets are stored inside a secret called `my-tls-secret`. Both our ingress use the same TLS secret.
5. **Helm Chart**<br/>
	We have configured a helm chart to manage installation, updates, rollbacks and uninstallation. <br/>Everything can be installed by a single command from within the /helm_chart directory: `helm install . --generate name`on google kubernetes engine or, `microk8s helm3 install . --generate-name` on local machine / microk8s. 
6. **Security - Network Policies**<br/>
	We have configured a network policy named `api-allow` which only allows ingress traffic from the API to the DB and blocks everything else. Since the DB is only ever accessed by the API, doing this made sense.
7. **Security - RBAC**<br/>
	We have created 2 users - `readeruser` and `writeruser`. The `readeruser` can only execute `kubectl get`, `kubectl watch` and `kubectl list` commands. So it is a 'read-only' user. The `writeruser`, in addition to the commands executed by the `readeruser` can also execute `kubectl create`, `kubectl update`, `kubectl patch` and `kubectl delete` commands.<br/> We able to get RBAC working on our local machine, but not on google cloud.
8. **Google Cloud Platform**<br/>
	We were able to perform everything on google cloud, except for RBAC.
