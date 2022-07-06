#!/usr/bin/env python3.9

# import logging

# integer = 50
# string = "The number is"

# try:
#     print(string + integer)
# except TypeError as t_err:
#     logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(t_err))
# except ValueError as v_err:
#     logging.warning("Error - {}. Your message".format(v_err))


import logging
import boto3
from botocore.exceptions import ClientError
integer = 50
string = "The number is"
try:
    client = boto3.client('translate')
    print(string + integer)
except ClientError as e:
    logging.warning("<your msg> {}".format(e))
