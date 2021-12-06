# Containerized application to calulate the factorial with Python.


Application container deployed to AWS EKS in region us-eats-2 from the image which has been saved in ECR as public repository in us-east-1 region.</br>
The creation of the public container has been done via aws panel GUI and the docker image pushed build and pushed via Cloud9.</br>

According to my previous experiences with Kubernetes which is most powerfull platform for this purpose and in compare with ECS , ECS limitted in configuration option and as  you can share an ENI between multiple pods and place more pods per instance and in terms of portability you are locked into Amazon infrastructure with ECS and not able to move your cluster to other cloud provider since the EKS is based on Kubernetes you can move and run your cluster in any other kubernetes environments. I decided to use EKS on top.

In addition to above, because of below advantages in compare of ECS and fargate (Serverless solution) I decided to deploy over aws eks and create cluster: 

* Horizontal scaling.</br>
* Automates rollouts and rollbacks.</br>
* Kubernetes where to deploye the container as best location</br>
* Scale resources and applications in real time</br>
* EKS uses VPC networking which is easy to manage</b>
* ability to use public and private container. </b>




# Service Mesh
I have used Kubernetes service mesh to manange and secure traffic between --> Ref: https://istio.io/ </br> Also 
check the below CaI in kube-manifest foder
```sh 
services.yaml 
```
in order to install and use the kubernetes application, i used Helm as package maneger : ref: https://helm.sh/ </br>

# Ingress Nginx 
as a reverse proxy and load balancer i used ingress-nginx to confiugure an http/https load balancer for the application running on my eks. please check yaml file ingress.yaml </br>
in order to configure the ingress nginx a subdomain has been created "factorial.myloop.tech" on port 80 to manage incoming traffic to available nodes on eks with available namespace as defined in yaml files. 

```sh 
ubectl -n ingress-nginx get svc
NAME                                 TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)                      AGE
ingress-nginx-controller             LoadBalancer   10.100.54.252   aeaa9a969afd749609f0f079ff776254-1937423680.us-east-2.elb.amazonaws.com   80:32729/TCP,443:32636/TCP   15h
ingress-nginx-controller-admission   ClusterIP      10.100.31.56    <none>                                                                    443/TCP                      15h
```
```sh

kubectl -n ingress-nginx get pod
NAME                                      READY   STATUS    RESTARTS   AGE
ingress-nginx-controller-54bfb9bb-h9f5b   1/1     Running   0          15h
```

# Application 
The factorial application has been developed in python with flask framework in order to expose the api. The API is POST API and which authentication. Python flask used because at the moment i have more experience with Python. 
The API exposed vi gunicorn on port 8080 and port forwarded to 80 in EKS cluster.

```sh
kubectl -n factorial  port-forward factorialapp-7fccc864bf-hr4w7 8080
```

# EKS Cluster 
EKS cluster created with 2 node on aws EC2 in us-east-2b/us-east-2c. 

The cluster is available in one AZ right now. not enough time to deploye on different AZ to hava HA.

* CLI tool for creating and managing clusters on EKS: eksctl
* Run commands against Kubernetes clusters : kubectl

appcuster has been created in eksctl cli. 

# aws cli 

use aws ckd for the lambda serverless application and i decided to use aws cli for the EKS assignment and the configuration profile configured in:</br>
```sh
cat ~/.aws/config
[default]
region = us-east-2
output = json
``` 

# API and application test curl 

## request 
```sh
curl --location --request POST 'factorial.myloop.tech/api/v1/calculate/factorial' --header 'X-API-KEY: 123qwe' --header 'Content-Type: application/json' --data-raw '{
    "input":3
}'
```

## response

```sh 
{
  "result": 6
}
```

## request and reposns healthz.py

curl http://factorial.myloop.tech/healthz
{
  "success": true
}

# Checks

```sh 
kubectl -n factorial get pods
NAME                            READY   STATUS    RESTARTS   AGE
factorialapp-7fccc864bf-h45rj   1/1     Running   0          14h
factorialapp-7fccc864bf-hr4w7   1/1     Running   0          14h
factorialapp-7fccc864bf-zv6dq   1/1     Running   0          14h

kubectl -n factorial describe svc
Name:              factorialapp
Namespace:         factorial
Labels:            <none>
Annotations:       <none>
Selector:          app=factorialapp
Type:              ClusterIP
IP Family Policy:  SingleStack
IP Families:       IPv4
IP:                10.100.36.14
IPs:               10.100.36.14
Port:              <unset>  80/TCP
TargetPort:        8080/TCP
Endpoints:         192.168.20.230:8080,192.168.25.232:8080,192.168.86.203:8080
Session Affinity:  None
Events:            <none>
```


