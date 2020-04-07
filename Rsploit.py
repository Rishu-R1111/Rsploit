#!/usr/bin/env python3

import os
import subprocess as subp
from modules.misc import misc
from modules.exfil import exfil
from modules.reverse_shell import rshell

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

version = '1.0.0'

def banner():
	os.system('clear')
	banner = r'''
                                                                                                                                     
RRRRRRRRRRRRRRRRR                                                         lllllll                    iiii          tttt          
R::::::::::::::::R                                                        l:::::l                   i::::i      ttt:::t          
R::::::RRRRRR:::::R                                                       l:::::l                    iiii       t:::::t          
RR:::::R     R:::::R                                                      l:::::l                               t:::::t          
  R::::R     R:::::R                     ssssssssss   ppppp   ppppppppp    l::::l    ooooooooooo   iiiiiiittttttt:::::ttttttt    
  R::::R     R:::::R                   ss::::::::::s  p::::ppp:::::::::p   l::::l  oo:::::::::::oo i:::::it:::::::::::::::::t    
  R::::RRRRRR:::::R                  ss:::::::::::::s p:::::::::::::::::p  l::::l o:::::::::::::::o i::::it:::::::::::::::::t    
  R:::::::::::::RR   --------------- s::::::ssss:::::spp::::::ppppp::::::p l::::l o:::::ooooo:::::o i::::itttttt:::::::tttttt    
  R::::RRRRRR:::::R  -:::::::::::::-  s:::::s  ssssss  p:::::p     p:::::p l::::l o::::o     o::::o i::::i      t:::::t          
  R::::R     R:::::R ---------------    s::::::s       p:::::p     p:::::p l::::l o::::o     o::::o i::::i      t:::::t          
  R::::R     R:::::R                       s::::::s    p:::::p     p:::::p l::::l o::::o     o::::o i::::i      t:::::t          
  R::::R     R:::::R                 ssssss   s:::::s  p:::::p    p::::::p l::::l o::::o     o::::o i::::i      t:::::t    tttttt
RR:::::R     R:::::R                 s:::::ssss::::::s p:::::ppppp:::::::pl::::::lo:::::ooooo:::::oi::::::i     t::::::tttt:::::t
R::::::R     R:::::R                 s::::::::::::::s  p::::::::::::::::p l::::::lo:::::::::::::::oi::::::i     tt::::::::::::::t
R::::::R     R:::::R                  s:::::::::::ss   p::::::::::::::pp  l::::::l oo:::::::::::oo i::::::i       tt:::::::::::tt
RRRRRRRR     RRRRRRR                   sssssssssss     p::::::pppppppp    llllllll   ooooooooooo   iiiiiiii         ttttttttttt  
                                                       p:::::p                                                                   
                                                       p:::::p                                                                   
                                                      p:::::::p                                                                  
                                                      p:::::::p                                                                  
                                                      p:::::::p                                                                  
                                                      ppppppppp                                                                  
                                                                                                                                 
	print(G + banner + W)
	print(G + '[+]' + C + ' Created By : ' + W + 'thewhiteh4t')
	print(G + '[+]' + C + ' Version    : ' + W + version)

def main():
	print('\n' + G + '[+]' + C + ' Choose Target : ' + W + '\n')
	print(G + '[1]' + C + ' Windows' + W)
	while True:
		choice = input(G + '\nfs > ' + W)

		if choice == '1':
			win()
		elif choice == 'exit' or choice == 'quit':
			quit()
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def win():
	print('\n', end='')
	print(G + '[1]' + C + ' exfil' + W)
	print(G + '[2]' + C + ' reverse_shell' + W)
	print(G + '[3]' + C + ' misc' + W)
	
	while True:
		win_choice = input(G + '\nfs[windows] > ' + W)
		
		if win_choice == '1':
			exfil(win)
		elif win_choice == '2':
			rshell(win)
		elif win_choice == '3':
			misc(win)
		elif win_choice == 'clear':
			os.system('clear')
		elif win_choice == 'back':
			return main()
		elif win_choice == 'help':
			return win()
		elif win_choice == '':
			pass
		elif win_choice == 'exit' or win_choice == 'quit':
			quit()
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def quit():
	distro = subp.Popen(['uname', '-r'], stdout = subp.PIPE)
	distro = distro.communicate()[0].decode()
	if 'ARCH' in distro:
		subp.call(['systemctl', 'stop', 'sshd.service'])
	else:
		subp.call(['systemctl', 'stop', 'ssh.service'])
	subp.call(['pkill', 'php'])
	exit()

try:
	banner()
	main()
except KeyboardInterrupt:
	print(R + '[-]' + C + ' Keyboard Interrupt.' + W + '\n')
	quit()
