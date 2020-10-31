from openstack import connection

conn = connection.Connection(
    region_name='RegionOne',
    auth=dict(
        auth_url='http://172.16.41.168/identity/v3/',
        username='admin',
        password='123456',
        project_id='5e27f73f596c4b0382cbf96b59c5f5bc',
        user_domain_id='default'),
#    compute_api_version='2.1',
#    identity_interface='internal'
)

def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server.name)

def list_images(conn):
    print("List Images:")

    for image in conn.compute.images():
        print(image.name)

def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print(network.name)

def stop_instance(conn, server_id):
    conn.compute.stop_server(server_id)

def start_instance(conn, server_id):
    conn.compute.start_server(server_id)

start_instance(conn,'745b70de-196f-484f-84cf-0ad92740523b')