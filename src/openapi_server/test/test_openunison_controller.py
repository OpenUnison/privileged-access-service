import unittest

from flask import json

from openapi_server.models.access_verification_response import AccessVerificationResponse  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOpenunisonController(BaseTestCase):
    """OpenunisonController integration test stubs"""

    def test_verify_access(self):
        """Test case for verify_access

        Verify user access to a cluster
        """
        query_string = [('user_id', 'user_id_example'),
                        ('cluster_id', 'cluster_id_example'),
                        ('ticket_number', 'ticket_number_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/verify-access',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
