import os
import time
from kubernetes import client, config

import subprocess

def run_sqlmesh_ide():
    time.sleep(5)
    print(f"Your current directory is: {os.getcwd()}")
    print(f"Changing working directory to: {os.environ.get('GITSYNC_ENV')}")
    os.chdir(os.environ.get('GITSYNC_ENV'))
    print(f"Your current directory has changed to: {os.getcwd()}")
    try:
        subprocess.run(["sqlmesh", "ide","--port","8000"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'sqlmesh ide': {e}")

def shutdown_container(namespace, pod_name, container_name):
    # Load Kubernetes configuration
    config.load_incluster_config()

    # Create Kubernetes API client
    api_client = client.ApiClient()

    # Trigger the container shutdown using the Kubernetes API
    api_instance = client.CoreV1Api(api_client)
    api_instance.delete_namespaced_pod(name=pod_name, namespace=namespace, body=client.V1DeleteOptions(
        propagation_policy='Foreground',
        grace_period_seconds=5,
        preconditions=client.V1Preconditions(
            uid=api_instance.read_namespaced_pod(name=pod_name, namespace=namespace).metadata.uid
        ),
        #orphan_dependents=False
    ))

if __name__ == "__main__":
    try:
        run_sqlmesh_ide()
    except Exception as e:
        print(f"Error while running 'sqlmesh ide' command: {e}")
    # Read environment variables
    namespace = os.environ.get('NAMESPACE')
    pod_name = os.environ.get('POD_NAME')
    container_name = os.environ.get('CONTAINER_NAME')

    # Call the shutdown_container function with the environment variables
    shutdown_container(namespace, pod_name, container_name)