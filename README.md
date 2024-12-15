Script:
    a python script that retrive data from rick & morty api ("https://rickandmortyapi.com/api").
    it pules data of the characters how are "Human", "Alive" and there origin is "Earth".
    it extract the result into a csv file called characters.csv.
    
        execute script:
            in the main folder:
                python ./rick_morty_csv.py

Rick and Morty REST API

    this image is a REST API which fetch characters from the Rick and Morty API (https://rickandmortyapi.com/api)
    where the origin is Earth, status is Alive, and species is Human.

    the application listen on port 5000
    it return a json string with the results.

    Accessing the REST API:
        http://localhost:5000/characters to fetch the filtered characters.
        http://localhost:5000/healthcheck to check the health of the service.return status 200


docker:

    the Dockerfile builds an image of the REST API. based on python:3.12-slim. it loads dependencies and run rhe REST-Api script (rick_morty_REST.py)
    the image is stored in DockerHub:
    https://hub.docker.com/repository/docker/ecyanofsky/rick_and_morty/general

    applying on docker (must pull it first):
        docker pull ecyanofsky/rick_and_morty:1.2 (or any other tag available)
        docker run -d -p 5000:5000 --name rick_morty ecyanofsky/rick_and_morty:1.2 (same as above)
    
    entering the API is the same as above.

K8s:

    important!!!
    * you need to create manually before starting the deployment a name-space called "rickmorty".
    * the ingress is for a Domain "issy.site.local". set the HOST file locally to address the public ingress address IP.

    inside the "yamls" folder there are the files needed to run the application on a K8s cluster. 
    Deployment.yaml - Deployment file that lunches an image from DockerHub (ecyanofsky/rick_and_morty:1.0) on a pod under the name: rick-morty.  it set to 1 replica (can serve more), pulling a image of the
    REST-api of the ricky and morty. it listen on port 5000.
    Service.yaml - this is the service file (called: rick-morty-service). it sets to port 80 and its target port is 5000 (80:5000).
    Ingress.yaml- this file set the ingress gateway for the rick and morty API on a istio ingress gateway (name: "rick-morty-gateway"). 
    it also include the virtual map for the REST service ("name: rick-morty-virtualservice").
    it set to listen on port 80 and HTTP protocol. transfer traffic for the domain "issy.site.local". which is been routed to the following routs:
        /characters - opens a webpage with the result as jason map (http://issy.site/characters). 
        /healthcheck - opens a webpage with the status "healthy" (http://issy.site/healthcheck).
    the ports transfer are set to 80.
        * /htmlversion - from v1.1 of the image on dockerHub there is a html version of the results: (http://issy.site/htmlversion)
            (need to change in the Deployment.yaml file - ecyanofsky/rick_and_morty:1.1).
       
helm:
    to execute the helm chard you first need to navigate to the rickmorty folder under the helm folder and execute the following command:

    helm upgrade --install -n rickmorty rickmorty -f values.yaml .

    it will deploy the pod and all nececery dependencies (Deployment.yaml, Service.yaml, Ingress.yaml)
    the valur.yaml is set to deploy image v1.0 with ingress listening for the domain "issy.site".

    
