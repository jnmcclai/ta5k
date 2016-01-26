#python ta5k general library
#developed with ver python 2.7.7

import ta5k_login
import logging
import json
import time
import re

#define some logging
logging.basicConfig(format='%(asctime)s %(message)s', filename='ta5k_gen.log', level=logging.DEBUG, filemode='w')

class ta5kGen():
    """
        bank of ta5k commands with generic responses
    """
    def __init__(self, session):
        #class initialization
        self.timeout = 120
        self.session = session


    def show_red(self, module):
        """
        show redundancy <shelf>/<slot>

        args: {
                    session: login session to perform the command within
                    module: the module/slot for 'show redundancy <shelf>/<slot>'
              }
        """
        output = dict()
        response = self.session.perform_command('show redundancy 1/{0}'.format(module))
        """
        analyze the response string
        """
        #split the response by line -> this creates a list
        response = response.split("\r\n")
        #kill the first and last values in the list
        del response[0]; del response[-1]
        #run through each line and split by :
        for element in response:
            #split by colon
            element = element.split(":")
            #format -> remove extra spaces, tolower, replaces spaces with underscores
            key = element[0].strip()
            key = key.lower()
            key = key.replace(" ","_")
            value = element[1].strip()
            #build dictionary
            output[key] = value
        #return dictionary/json with information
        return output 


            def show_red(self, module):
        """
        show redundancy <shelf>/<slot>

        args: {
                    session: login session to perform the command within
                    module: the module/slot for 'show redundancy <shelf>/<slot>'
              }
        """
        output = dict()
        response = self.session.perform_command('show redundancy 1/{0}'.format(module))
        """
        analyze the response string
        """
        #split the response by line -> this creates a list
        response = response.split("\r\n")
        #kill the first and last values in the list
        del response[0]; del response[-1]
        #run through each line and split by :
        for element in response:
            #split by colon
            element = element.split(":")
            #format -> remove extra spaces, tolower, replaces spaces with underscores
            key = element[0].strip()
            key = key.lower()
            key = key.replace(" ","_")
            value = element[1].strip()
            #build dictionary
            output[key] = value
        #return dictionary/json with information
        return output 

        
if __name__ == '__main__':
    print ta5kGen().show_red

    