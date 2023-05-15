


```sh
helm install prometheus helm-charts/kube-prometheus-stack -n monitoring --create-namespace
kubectl apply -f rbac.yaml
kubectl apply -f role.yaml
kubectl apply -f role-binding.yaml
kubectl apply -f yamls/monitoring/prometheus-config-no-istio-no-kubelet.yaml
kubectl apply -f yamls/monitoring/prometheus-deployment.yaml
kubectl apply -f yamls/monitoring/grafana-pvc.yaml
kubectl apply -f yamls/monitoring/grafana-deployment.yaml
kubectl apply -f yamls/monitoring/grafana-service.yaml

```
