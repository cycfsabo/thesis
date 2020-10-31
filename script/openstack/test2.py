# List servers in Nova
from novaclient import client 
conn = client.Client(user='admin', password='123456', project='admin', auth_url='http://172.16.41.168/compute/v2.1/')
print(conn)
#from server in conn.servers.list():
#	print(server.name)
