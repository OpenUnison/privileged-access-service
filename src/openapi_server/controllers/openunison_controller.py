import connexion
from datetime import date, datetime, timedelta, timezone
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.access_verification_response import AccessVerificationResponse  # noqa: E501
from openapi_server.models.pam_task_detail import PamTaskDetail
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server import util


def verify_access(user_id, cluster_id, ticket_number):  # noqa: E501
    """Verify user access to a cluster

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :param cluster_id: 
    :type cluster_id: str
    :param ticket_number: The record number, format should be INC1234567 for Ticket records and CHG1234567 for Change records.
    :type ticket_number: str

    :rtype: Union[AccessVerificationResponse, Tuple[AccessVerificationResponse, int], Tuple[AccessVerificationResponse, int, Dict[str, str]]
    """
    if ticket_number.lower() == 'inc1234567':
        # return an incident
        return AccessVerificationResponse([PamTaskDetail('TASK-1234', (datetime.now(timezone.utc) + timedelta(0,30)).strftime("%Y-%m-%dT%H:%M:%S+00:00")   )]), 200
        
        #return AccessVerificationResponse([PamTaskDetail('TASK-1234', (datetime.now(timezone.utc) + timedelta(30)).strftime("%Y-%m-%dT%H:%M:%S+00:00")   )])
    else:
        return ErrorResponse("Could not find incident " + ticket_number), 404
    return 'do some magic!'
