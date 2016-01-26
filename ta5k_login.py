#python ta5k general library

import logging
import time
import telnetlib
import re

#define some logging
logging.basicConfig(format='%(asctime)s %(message)s', filename='ta5k_login.log', level=logging.DEBUG, filemode='w')

class loginCli():
    """
        connect to a shelf
    """
    def __init__(self):
        #class initialization
        self.timeout = 120
        self.prompt = '(^|\\n)\S+[>#]$'


    def login(self, ip, method='telnet'):

        if method.lower() == 'telnet':
            self.session = telnetlib.Telnet(ip)
            self.session.read_until('Username:')
            self.session.write('ADMIN\n')
            self.session.read_until('Password:')
            self.session.write('PASSWORD\n')
            self.session.read_until('>')
            self.session.write('enable\n')
            self.session.read_until('#')
            self.session.write('term len 0\n')
            self.session.read_until('#')
        else:
            logging.info('login method not supported')

    def perform_command(self, command):
        #self.session.read_until('#')
        self.session.write(command + '\n')
        response = self.session.read_until('#')
        return response

class commandBank():
    """
        bank of generalized ta5k commands that are often used with returned responses
    """
    def __init__(self, session):
        #class initialization
        self.timeout = 120

    #build out functions for basic commands and parse the output returning maybe json/dict/other that
    #users can use to do things with


if __name__ == '__main__':
    my_session = loginCli()
    my_session.login('10.213.253.36')
    command = my_session.perform_command('show interfaces gigabit-ethernet 1/0/1@1/3/1 performance-statistics 15')
    print command

    