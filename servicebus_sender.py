#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show sending message(s) to a Service Bus Queue asynchronously.
"""

import os
import asyncio
from azure.servicebus import Message
from azure.servicebus import ServiceBusClient

CONNECTION_STR = 'Endpoint=sb://project3-servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1pK05VrVBDELBog4+2TNmgOSrmu8L3LWp+ASbFrsc3Y='
QUEUE_NAME = 'notificationqueue'


def main():
    from azure.servicebus import ServiceBusClient
    from azure.servicebus import QueueClient, Message
    # Create the QueueClient
    queue_client = QueueClient.from_connection_string(CONNECTION_STR, QUEUE_NAME)
    # Send a test message to the queue
    for i in range (0,5):
        msg = Message(b'1')
        print('Sending')
        queue_client.send(msg)
        print("Send message is done.")

main()

