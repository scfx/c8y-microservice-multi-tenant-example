import os
import base64
import json
import logging
from urllib.request import Request
from urllib.request import urlopen

logger = logging.getLogger('microservice-common')
# values provided into environment by cumulocity platform during deployment
C8Y_BASEURL = os.getenv('C8Y_BASEURL')
C8Y_BOOTSTRAP_USER = os.getenv('C8Y_BOOTSTRAP_USER')
C8Y_BOOTSTRAP_TENANT = os.getenv('C8Y_BOOTSTRAP_TENANT')
C8Y_BOOTSTRAP_PASSWORD = os.getenv('C8Y_BOOTSTRAP_PASSWORD')


def base64_credentials(tenant, user, password):
    '''result is Base64 encoded "tenant/user:password"'''
    str_credentials = tenant + "/" + user + ":" + password
    return 'Basic ' + base64.b64encode(str_credentials.encode()).decode()


def get_subscriber_for(tenant_id):
    '''subscriber has form of dictionary with 3 keys {tenant, user, password}'''
    req = Request(
        C8Y_BASEURL + '/application/currentApplication/subscriptions')
    req.add_header('Authorization', base64_credentials(
        C8Y_BOOTSTRAP_TENANT, C8Y_BOOTSTRAP_USER, C8Y_BOOTSTRAP_PASSWORD))

    response = urlopen(req)
    subscribers = json.loads(response.read().decode())["users"]
    return [s for s in subscribers if s["tenant"] == tenant_id][0]


def get_url_for(tenant_id, service_auth):
    '''returns url of subscribed tenant'''
    req = Request(
        C8Y_BASEURL + '/tenant/tenants/' + tenant_id)
    req.add_header('Authorization', service_auth)

    response = urlopen(req)
    domain = json.loads(response.read().decode())["domain"]
    return domain


def get_epl_files(tenant_url, service_auth):
    '''Retrieve all available EPL files'''
    req = Request('https://' +
                  tenant_url + '/service/cep/eplfiles')
    req.add_header('Authorization', service_auth)
    response = urlopen(req)
    files = json.loads(response.read().decode())
    return files
