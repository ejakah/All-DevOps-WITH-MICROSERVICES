# Internship Sheet - Docker + Miniwhoami (local desktop)
 

# Task 1 - Install Docker and Docker-Compose
a.Install the latest version of Docker on your Linux desktop system. What versions (client, server, API) do you have installed?

b.Install on your Linux desktop system docker composein a current version. What command did you docker compose use to install? Which version do you have installed?
 

# Task 2 - Primitive web server
a.In a subdirectory, create servmgmt-ws22/prak/pr02/miniserver a program for a small, very simple web server miniserverthat responds with "Hello Service Management winter term 2022. My name is ....".
Requirement : The web server should be programmed in a programming language (eg PHP, Node.js, Python, Go) so that the server can be functionally expanded.

b.Test your web server - i.e. the program you have created - on your Linux desktop system. (Test without Docker by just running the program). How do you proceed?

c.For your program, create servmgmt-ws22/prak/pr02/miniserver a Dockerfile.
Provide Dockerfileand explain the one for your web server.

d.DockerfileCreate a Dockerimage from your miniserverwith the tag v1. Which command do you use for this?
Run docker run your web server on your desktop system under the name miniserver_20221 as a Docker container on port 20221 . What is your docker-run command?
The port number 20221is structured as follows:

2 stands for the course Services Management in Networks,

02 for internship sheet 2,

2 for task 2 on this internship sheet,

1 is the number of the container in the task.
 

# Task 3 - Service miniwhoami
a.Create a subdirectory servmgmt-ws22/prak/pr02/miniserver. In this you expand your web server program miniserverto a web service miniwhoamiwith the following properties:
The web service miniwhoamidisplays the host name, the IP addresses (IPv4 and IPv6) in the runtime environment and the number of accesses.
The background color of miniwhoamichanges depending on the hostname.
Specifically : A different hostname results in a different background color. This property is useful, for example, for the analysis of load balancing scenarios, because it allows you to see immediately whether miniwhoamithe host name has changed when accessing the web service, i.e. another container has responded.

b.First test your application without Docker on your local machine.

c.Create one for your program Dockerfileand build a Dockerimage with it miniwhoami. Provide your Dockerfile and the Docker command to create the image.

d.Deploy with docker run two containers miniwhoami_1 and miniwhoami_2 your web application miniwhoami on your Linux desktop system. To do this, use the ports 20231and 20232. What are your docker-run commands?

e.Call both services in your browser and test the service you have programmed miniwhoami.
 

# Task 4 - Network Troubleshooting
a.Go docker exec into the container with miniwhoami_1.
What command do you use to do this?
Which of the following commands can you execute in the container: ping, ip a, curl, dig, nslookup ?

b.Now go inside the container miniwhoami_1 using the excellent Netzerk docker tool [nicolaka/netshoot](https://github.com/nicolaka).
What command do you use to do this?
Which of the following commands can you execute in the container: ping, ip a, curl, dig, nslookup ?

c.Can you access the container mini_whoami_1 from the container mini_whoami_2?

d.How are the two containers mini_whoami_1 and mini_whoami_2connected to each other?

e.Can you access mini_whoami_1the website from the container heise.de?

f.Specify and interpret the routing table in the container mini_whoami_1.



# ALL-DevOps
docker ps
docker ps -a
docker stop 2a20189b00a5
docker rm 2a20189b00a5
docker rmi hostname-color-webapp:latest
................................................
# If you still face issues, you might need to force the removal by adding the -f flag: 
................................................
docker rmi -f hostname-color-webapp:latest
docker run -p 20231:80 patrickdevops:latest
docker build --no-cache -t patrickdevops:latest -f Dockerfile .
................................................
python3 -m venv venv
source venv/bin/activate


docker build -t hostname-color-webapp .

docker run -p 80:80 hostname-color-webapp

......................................................
# Listing running Docker images with their tag (registry/namespace/name:tag) use the comman below

docker inspect --format '{{.Config.Image}}' $(docker ps --format='{{.ID}}')
..........................................................


## craete ec2 instance
1. sudo apt-get update
mkdir amc-project
cd amc-project


## clone github code and check docker file
cd folder

ubuntu>amc-project>github folder have to install docker

# Install Docker
sudo apt-get install docker.io


# If docker container permission denied
docker images
sudo usermod -a -G docker $USER
sudo reboot

git clone https://github.com/ejakah/devops-project.git

ls

docker build -t amclab:dockerimage
docker run -d -p 8000:8000 amclab:dockerimage

docker login
ejakah
password

docker image tag amclab:dockerimage ejakah/amclab:dockerimage

docker image push ejakah/amclab:dockerimage

...........................................................
# Log in to Docker Hub (if not already logged in)
...........................................................
docker login
...........................................................
# Tag your Docker image with your Docker Hub username and repository name
docker tag your-image-name:your-tag your-docker-hub-username/your-repository-name:your-tag
...........................................................
docker tag individual-lab:latest ejakah/amc-wintersemester:latest
...........................................................
# Push the image to Docker Hub
docker push your-docker-hub-username/your-repository-name:your-tag
...........................................................
docker push ejakah/amc-wintersemester:latest
...........................................................


docker image tag hostname-color-webapp:latest ejakah/amc-project:latest

docker image push ejakah/amc-project:latest



# IF WE DECIDE NOT TO PUSH, BECAUSE WE HAVE AN EXISTING DOCKER IMAGE FROM PROXY, (Public docker hub register) THEN WE USE THE FOLLOWING

docker rmi amclab:dockerimage
docker stop e05bf729681a
docker rm e05bf729681a
docker rmi ejakah/amclab:dockerimage


docker pull docker.fslab.de/migbin2s/servmgmt-ws22/miniwhoami:latest
docker images
docker ps
docker run -d -p 80:80 docker.fslab.de/migbin2s/servmgmt-ws22/miniwhoami:latest

...........................................................
# KUBERNATES SETUP 1) START WITH MINIKUBE INSTALLATION BELOW

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

..........................................................
minikube start
..........................................................

# KUBERNATES SETUP 2) START WITH KUBECTL INSTALLATION BELOW

snap install kubectl --classic
..........................................................
# VERIFY KUBECTL CONFIGURATION 

minikube status

kubectl cluster-info

kubectl cluster-info dump

...........................................................
# INTERACT WITH CLUSTERS
kubectl get po -A
minikube kubectl -- get po -A
alias kubectl="minikube kubectl --"
minikube addons enable metrics-server
minikube dashboard
...........................................................

kubectl config current-context
minikube stop
minikube start
kubectl get namespaces
kubectl get pods --namespace=kube-system
kubectl create namespace ejaka
kubectl get namespaces

# CREAT DEPLOYMENT YAML FILE
vim deployment.yaml

# COPY THE FOLLOWING CODE AND PAST
.....................................................
apiVersion: apps/v1
kind: Deployment
metadata:
  name: amclab-deployment
  labels:
    app: web-app
  namespace: ejaka
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: docker.fslab.de/migbin2s/servmgmt-ws22/miniwhoami:latest
        ports:
        - containerPort: 80


...............................................................
kubectl apply -f deployment.yaml

kubectl get pods --namespace=ejaka

..........................................................
# WE DELETE ONE OF THE PORT TO DETERMINE IF ANOTHER PORT WILL BE AUTOMATICALLY CREATED BASE ON AUTO HEALING

# NOTE, EDIT THE NAME SPACE ID YOU WISH TO DELET e.g amclab-deployment-bf6f9b6fb-b8z84
........................................................

kubectl delete pod amclab-deployment-bf6f9b6fb-b8z84 --namespace=ejaka

# TO GET THREE HOST ID (PODS IP ADDRESS) BASE ON OUR 3 REPLICAL WE USE COMMAND 

kubectl get pods -o wide -n ejaka

# CREAT SERVICE YAML FILE (Load Balancer service)

vim service.yaml

# COPY THE FOLLOWING CODE AND PAST
............................
apiVersion: v1
kind: Service
metadata:
  name: amc-lab
  namespace: ejaka
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
..................................
# TO CREAT A SINGLE CLUSTER IP ADDRESS FOR 3 PODS

kubectl apply -f service.yaml

kubectl get svc -n ejaka


# deploy the application.
minikube service amc-lab -n ejaka --url

# EDIT THE HTTP ADDRESS BELOW WITH THE ONE IN DISPLACE 

curl -L http://192.168.49.2:32644

minikube service amc-lab -n ejaka

minikube dashboard 

.......................................................
# LOGIN TO NGROK, GO TO THE WEBSITE COPT THE LINUX LINK ADDRESS TYPE WGET AND PASTE THE ADDRESS IN ORDER TO DOWNLOAD AND UNZIP THE FILE 

wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

tar -xvzf ngrok-v3-stable-linux-amd64.tgz 



# Authenticate yourself with ngrok: Go to the ngrok page and you will see under option 2 <Connect your account>. Now copy the command and run your local machine.


sudo snap install ngrok

........................................................
ngrok config add-authtoken 2XEf8P1eHcu8lPRBi93zdsxLecH_2fKp1WXpzRW4dRvuQSbXo
.........................................................

# EDIT ONLY THE IP AND PORT ADDRESS BELOW WITH YOUR CLUSTER IP
ngrok http 192.168.49.2:32644

# COPPY THIS FORWARDING LINK FROM THE DISPLAY TERMIAL 
https://0ead-54-209-19-230.ngrok-free.app





















.............................................................
KUBERNATE INSTALLATION 


curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
...........................................................

minikube start
..........................................................

curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl \
    && sudo install kubectl /usr/local/bin && rm kubectl

.........................................................


















