USERNAME='admin'
PASSWORD='123456'
PROJECT_ID='5e27f73f596c4b0382cbf96b59c5f5bc'
PROJECT_NAME='admin'
from keystoneclient.v3 import client as keystone_client
from novaclient import client as nova_client

keystoneclient = keystone_client.Client( username=USERNAME, project_name=PROJECT_NAME, password=PASSWORD, auth_url='http://172.16.41.168/identity/v3/')

#print(keystoneclient.auth_token)
nova_client = nova_client.Client('2.1','admin', None,'admin', auth_url='http://172.16.41.168/compute/v2.1/', auth_token=keystoneclient.auth_token)

s = type(nova_client.servers.list())
print(s)

