#!/usr/bin/python

""" """

import logging
    
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def evaluate_pom(repository):
    """
    :param repository:
    """
    pass

def install_api(repository):
    """
    :param repository:
    """
    pass

def handler(event, context):
    """
    :param event:
    :param context:
    """
    judge = Judge() # TODO : Use credential.
    score = judge.score(evaluate_pom)
    # TODO : Check score first.
    judge.with_fork(install_api)
    return '' # TODO : Return JSON object result ?