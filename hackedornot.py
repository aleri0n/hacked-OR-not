#!/usr/bin/env python
import requests
import json 
import os

email = raw_input('Enter your email: ') 
os.system('clear')
payload = {'q': email}
r = requests.get('https://hacked-emails.com/api', params=payload)
result = json.loads(r.text)
if r.status_code == 200:
   if result['status'] == 'found':
         print 'Warrning! Your email is', result['status'],'!'
         print ''
         print 'Title of leak:', result['data'][0]['title']
         print 'Date leaked:', result['data'][0]['date_leaked']
         print 'Total lines count:', result['data'][0]['source_lines']
         print 'Size of leak:', result['data'][0]['source_size'] % 1024, 'MB'
         print ''
         print 'Source Provider:', result['data'][0]['source_provider']
         print 'Source URL:', result['data'][0]['source_url']
         print 'Verified Leak?', result['data'][0]['is_vrf']
         if result['data'][0]['is_vrf'] == True:
            print 'You should change your password immediately!'
         else:
            print 'Not verified. Could be false positive...'         
         print ''
         print 'Leak available on:', result['data'][0]['source_network']
   elif result['status'] == 'notfound':
         print 'Congratulations! Found no result for: ',email
else:
         print 'An error occured. Something is wrong...'
         print 'Have you typed the email correctly? :('
