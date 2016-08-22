#!/usr/bin/env python
import requests, json, os

print ''
print ''
print '  |    |         W3LC0M3           |    |  '
print '  |    |                           |    |  '
print ' .........................................'
print '|                                         |'
print '|    HackedORNot                          |'
print '|           v1.1                          |'
print '|                           By Aleri0n    |'
print '|                                         |'
print ' .........................................'
print '  |    |                           |    |'
print '  |    |         W3LC0M3           |    |'
print ''
print ''

email = raw_input('Enter your email: ')
if os.name == "posix":
        os.system('clear')
        print ''
        print ''
        print '  |    |  PL3@S3 W@1T... L0@D1NG.  |    |  '
        print '  |    |                           |    |  '
        print ' .........................................'
        print '|                                         |'
        print '|    HackedORNot                          |'
        print '|           v1.1                          |'
        print '|                           By Aleri0n    |'
        print '|                                         |'
        print ' .........................................'
        print '  |    |                           |    |'
        print '  |    |  PL3@S3 W@1T... L0@D1NG.  |    |'
        print ''
        print ''

elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
        print ''
        print ''
        print '  |    |  PL3@S3 W@1T... L0@D1NG.  |    |  '
        print '  |    |                           |    |  '
        print ' .........................................'
        print '|                                         |'
        print '|    HackedORNot                          |'
        print '|           v1.1                          |'
        print '|                           By Aleri0n    |'
        print '|                                         |'
        print ' .........................................'
        print '  |    |                           |    |'
        print '  |    |  PL3@S3 W@1T... L0@D1NG.  |    |'
        print ''
        print ''

else:
    print '\n' * numlines


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
         print ''
         print ''
if r.status_code == 200:
    if result['status'] == 'notfound':
         print 'Congratulations! Found no result for: ',email
         print ''
         print ''
else:
         print 'An error occured. Something is wrong...'
         print 'Have you typed the email correctly? :('
         print ''
         print ''
 
