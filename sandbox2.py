#example python test case

import ta5k_login
import ta5k_gen


#initialize variables
ip = '10.213.253.40'
module = 'a'

#open session
session = ta5k_login.loginCli()
session.login(ip)

#pass session for method calls
command = ta5k_gen.ta5kGen(session)


print command.show_red('a')['my_slot']







