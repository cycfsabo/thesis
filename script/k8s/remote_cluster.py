from kubernetes import client, config


def main():
    # Define the barer token we are going to use to authenticate.
    # See here to create the token:
    # https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
    aToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6InlSVHVBVXZFeUVXNTlhcnYzWFFhTXk2N0N2OVdpV0VTUHowQWs1U2lXRDAifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tZmtjOW0iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjFlMjJlNmI0LTkwZTgtNGVjYy1iMDk4LWNhNjhmOTMwNWI0OCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.UHiUAcczfuSPfEdR_jqypmkqk1STMZxv-RR46fyXfykQZ2AuhWlHW8pfO8UHWF_bamNUuBc9OvXPuHBfSLUiln6GXPZKCSNZ_mRny1a7XMFP9cKYFLMBOaK_0rfokjBCTJbLmg6J1M2MxIz4IMuavPdHUjZZB9KfRS85JP4EkgKcSJyXeYhMBQzaeUbea4w5aIOgq7VBTt9hPRtg0Krms13ayElLqUrP4QzVQlM_ERjeAteZam9c9K-jYZNh1eR8XyYsz4SMKmirFWz63QMuMY8BMSNHNPkYJFUYmHN1vcpBGAsYnaPDXUjxHEpzyGXRoVJOs9pHGnzrSQDKR4dxUQ"

    # Create a configuration object
    aConfiguration = client.Configuration()

    # Specify the endpoint of your Kube cluster
    aConfiguration.host = "https://192.168.182.223:6443"

    # Security part.
    # In this simple example we are not going to verify the SSL certificate of
    # the remote cluster (for simplicity reason)
    aConfiguration.verify_ssl = False
    # Nevertheless if you want to do it you can with these 2 parameters
    # configuration.verify_ssl=True
    # ssl_ca_cert is the filepath to the file that contains the certificate.
    # configuration.ssl_ca_cert="certificate"

    aConfiguration.api_key = {"authorization": "Bearer " + aToken}

    # Create a ApiClient with our config
    aApiClient = client.ApiClient(aConfiguration)

    # Do calls
    v1 = client.CoreV1Api(aApiClient)
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
#    print(v1.list_pod_for_all_namespaces(watch=True))

if __name__ == '__main__':
    main()
