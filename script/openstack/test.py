from keystoneclient.v3 import client
auth_url = 'http://172.16.41.168/identity/v3/'
username = 'admin'
user_domain_name = 'Default'
project_name = 'admin'
project_domain_name = 'Default'
password = '123456'
keystone = client.Client(auth_url=auth_url, version=(3,),username=username,password=password,user_domain_name=user_domain_name,project_name=project_name,project_domain_name=project_domain_name)
print (keystone.auth_token)

