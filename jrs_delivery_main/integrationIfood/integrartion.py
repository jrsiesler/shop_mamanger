from .models import IntegrationConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys
import json
import requests as rq
import logging
import datetime
import time

token = ''
token_expires = datetime.datetime.now()
integration_base_url = ''
client_id = ''
client_secret = ''

def delete_old_job_executions(max_age=604_800):
  logging.info('delete_old_job_executions')
  DjangoJobExecution.objects.delete_old_job_executions(max_age)

def job_pooling():
    logging.info('job_pooling()')
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 30 seconds
    scheduler.add_job(
        pooling_events_ifood, 
        'interval', 
        seconds=30, 
        name='integration_ifood_pooling', 
        id='integration_ifood_pooling',
        jobstore='default',
        max_instances=1,
        replace_existing=True,)
    # run this job every 1 hour
    scheduler.add_job(
        delete_old_job_executions, 
        'interval', 
        hours=1, 
        name='delete_old_job_executions',
        id='delete_old_job_executions',
        jobstore='default',
        max_instances=1,
        replace_existing=True,)
    try:
        logging.info("Starting scheduler...")
        register_events(scheduler)
        scheduler.start()
    except KeyboardInterrupt:
        logging.info("Stopping scheduler...")
        scheduler.shutdown()
        logging.info("Scheduler shut down successfully!")

def get_integration_config():
    logging.info('get_integration_config()')
    global integration_base_url
    global client_id
    global client_secret
    config = IntegrationConfig.get_current_config()
    integration_base_url = config.integration_base_url
    client_id = str(config.client_id)
    client_secret = config.client_secret


def get_token(client, secret):
    logging.info('get_token()')
    global token
    global token_expires
    try:
        if (token == '' or token_expires<=datetime.datetime.now()):
            logging.info('entrou no if')
            urlAuth = integration_base_url + '/authentication/v1.0/oauth/token'
            payload='grantType=client_credentials&clientId=' + client + '&clientSecret=' + secret
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = rq.request("POST", urlAuth, headers=headers, data=payload)
            json_data = json.loads(response.text)
            token = json_data.get('accessToken')
            expires = json_data.get('expiresIn')
            token_expires = (datetime.datetime.now() + datetime.timedelta(seconds=(expires-30)))
            logging.info(token)
            logging.info(token_expires)
        else:
            logging.info('entrou no else')
            None

    except Exception as e:
        raise Exception('Erro ao obter token: ' + e)
        logging.error(e)



def pooling_events_ifood():
    logging.info('pooling_events_ifood()')
    try:
        if (token_expires<=datetime.datetime.now()):
            logging.info('buscando novo token')
            get_token(client_id, client_secret)
        
        url = integration_base_url + '/order/v1.0/events:polling'
        payload={}
        headers = {
            'Authorization': 'Bearer ' + token
        }
        response = rq.request("GET", url, headers=headers, data=payload)
        logging.info(response)
        logging.info(response.status_code)
        if response.status_code == 204:
            logging.info('entoru no if')
        elif response.status_code == 200:
            logging.info('entrou no else')
            json_data = json.loads(response.text)
            for record in json_data:
                logging.info('record:')
                logging.info(record)
                event_id = record.get('id')
                code = record.get('code')
                full_code = record.get('fullCode')
                order_id = record.get('orderId')
                merchant_id = record.get('merchantId')
                created_at = record.get('createdAt')
                logging.info(event_id)
                logging.info(code)
                logging.info(full_code)
                logging.info(order_id)
                logging.info(merchant_id)
                logging.info(created_at)
    except Exception as e:
        raise Exception('Erro ao realizar pooling no ifood: ' + e)
        logging.error(e)

def start_ifood_integration():
    logging.info('start_ifood_integration')
    get_integration_config()
    logging.info(token)
    logging.info(token_expires)
    get_token(client_id, client_secret)
    