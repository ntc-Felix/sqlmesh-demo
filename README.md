# Create your minikube cluster
minikube start --nodes 3 --memory 16384 --cpus 2 --driver=virtualbox --disk-size 200GB 

# Install the Yugabyte Operator
```sh
kubectl apply -f helm-charts/yugabyte-operator/deploy/crds/yugabyte.com_ybclusters_crd_v1.yaml
kubectl create -f helm-charts/yugabyte-operator/deploy/operator.yaml
kubectl apply -f helm-charts/yugabyte-operator/deploy/crds/yugabyte.com_v1alpha1_ybcluster_full_cr.yaml
```
- if you are on minikube you will have to download the image used in this tutorial.

```sh
docker pull yugabytedb/yugabyte:2.17.3.0-b152
minikube image load yugabytedb/yugabyte:2.17.3.0-b152
```

# Monitoring Yugabyte
Now that we have our cluster we want to monitor it using Grafana and Prometheus. To achieve that we are going to use the kube-prometheus-stack.
```sh
helm install prometheus helm-charts/kube-prometheus-stack -n monitoring --create-namespace
```
Now that we have prometheus operator running, we are going to provide the prometheus configmap to get metrics from yugabyte.
```sh
kubectl apply -f yamls/monitoring/rbac.yaml
kubectl apply -f yamls/monitoring/role.yaml
kubectl apply -f yamls/monitoring/role-binding.yaml
kubectl apply -f yamls/monitoring/prometheus-config-new.yaml
kubectl apply -f yamls/monitoring/prometheus-service.yaml
kubectl apply -f yamls/monitoring/prometheus-deployment.yaml
kubectl apply -f yamls/monitoring/pv.yaml
kubectl apply -f yamls/monitoring/grafana-pvc.yaml
kubectl apply -f yamls/monitoring/grafana-deployment.yaml
kubectl apply -f yamls/monitoring/grafana-service.yaml
```

# Deploying SQLMesh in Kubernetes
```sh
kubectl create ns sqlmesh
kubectl apply -f yamls/sqlmesh/role.yaml
kubectl apply -f yamls/sqlmesh/role-binding.yaml
```

- you will also need to expose the load balancers through minikube tunnel
```sh
minikube tunnel
```