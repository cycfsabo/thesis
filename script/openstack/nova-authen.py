from os import environ as env
import novaclient.client
nova = novaclient.client.Client("2.1", auth_url=env['http://172.16.41.168/compute/v2.1'],username=env['admin'],api_key=env['123456'],project_id=env['admin'],region_name=env['default'])

print(nova)
