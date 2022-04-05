#!flask/bin/python

import os
import logging
from flask import Flask, jsonify, request
from common import base64_credentials, get_subscriber_for, get_url_for, get_epl_files

app = Flask(__name__)
logger = logging.getLogger('microservice')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.debug('Logger for microservice was initialized')
# Hello world endpoint


@app.route('/')
def hello():
    return 'Hello world!'

# Verify the status of the microservice


@app.route('/health')
def health():
    return '{ "status" : "UP" }'

# Get environment details


@app.route('/environment')
def environment():
    '''Get environment details'''
    environment_data = {
        'platformUrl': os.getenv('C8Y_BASEURL'),
        'mqttPlatformUrl': os.getenv('C8Y_BASEURL_MQTT'),
        'tenant': os.getenv('C8Y_BOOTSTRAP_TENANT'),
        'user': os.getenv('C8Y_BOOTSTRAP_USER'),
        'password': '...',  # os.getenv('C8Y_BOOTSTRAP_PASSWORD')
        'microserviceIsolation': os.getenv('C8Y_MICROSERVICE_ISOLATION')
    }

    return jsonify(environment_data)


@app.route('/tenant_auth')
def tenant_auth():
    '''Get auth of current request'''
    return tenant_user_auth()


@app.route('/service_auth')
def service_auth():
    return service_user_auth()


@app.route('/<tenant_id>/epl_files')
def epl_files(tenant_id):
    '''returns all epl_files of a subscribed tenant'''
    service_user = service_user_auth()
    tenant_url = get_url_for(tenant_id, service_user)
    tenant_service_user = tenant_service_auth(tenant_id)
    files = get_epl_files(tenant_url, tenant_service_user)
    return files


def tenant_user_auth():
    '''returns base64 encoded credentials of user'''
    tenant = request.authorization["username"].split('/')[0]
    user = request.authorization["username"].split('/')[0]
    password = request.authorization["password"]
    return base64_credentials(tenant, user, password)


def service_user_auth():
    '''returns base64 encoded credentials of service user'''
    tenant_id = request.authorization["username"].split('/')[0]
    return tenant_service_auth(tenant_id)


def tenant_service_auth(tenant_id):
    '''returns base64 encoded credentials of service user for a specific tenant'''
    service_user = get_subscriber_for(tenant_id)
    return base64_credentials(service_user["tenant"], service_user["name"], service_user["password"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
