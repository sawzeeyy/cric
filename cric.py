#!/usr/bin/env python3
# Author: Shuaib Oladigbolu
# Twitter: @_sawzeeyy

import argparse
import json
import os
from datetime import datetime

parser = argparse.ArgumentParser(
    description='This tool converts raw cookies to a\
        browser importable format'
)
parser.add_argument(
    '-d', '--domain', required=True,
    help='Domain name(s) or text file containing a list of domains'
)
parser.add_argument(
    '-i', '--input', required=True,
    help='Text file containing the raw cookies'
)
parser.add_argument(
    '-t', '--timestamp', required=False,
    help='The time the cookie will expire'
)
parser.add_argument(
    '-o', '--output', required=False,
    help='JSON file containing the browser importable cookies'
)
parser.add_argument(
    '-b', '--browser', required=False, default='chrome',
    help='Name of browser to use its cookie format'
)

args = parser.parse_args()
timestamp = 4724524800 if args.timestamp is None else args.timestamp
cookies = open(args.input).readlines()[0]
cookies = cookies.split('; ')
cookies = [dict(dict(zip(['name', 'value'], i.split('=')))) for i in cookies]
browser = args.browser.lower() if args.browser.lower() \
    in ['chrome', 'firefox'] else 'chrome'
export, count = [], 0

if args.domain.split('.')[-1] == 'txt':
    try:
        domains = open(args.domain).readlines()
    except:
        print('[!] Error! {} not found'.format(args.domain))
        exit()
    domains = [i.strip() for i in domains]
    output = ''.join(args.domain.split('/')[-1].split('.')[0])+'.json'
else:
    domains = args.domain.split(',')
    output = '.'.join(domains[1].split('.')[:-1])+'.json'

output = output if args.output is None else args.output
output = output if '/' in output else os.getcwd() + '/' + output
cric_path = os.path.dirname(os.path.realpath(__file__))
cric_path = '/'.join(cric_path.split('/')[:-1])

with open(cric_path + '/template.json') as template:
    temp_cookie = json.load(template)[browser]

for cookie in cookies:
    # You may specify timestamp
    # It's set to Tuesday, 19 September 2119 00:00:00 by default
    for domain in domains:
        count += 1
        if browser == 'chrome':
            temp_cookie.update({
                "domain": ".{}".format(domain),
                "expirationDate": timestamp,
                "name": cookie['name'],
                "value": cookie['value'],
                "id": count
            })
        elif browser == 'firefox':
            temp_cookie.update({
                "Host raw": "https://{}".format(domain),
                "Expires raw": timestamp,
                "Expires": str(datetime.fromtimestamp(timestamp)),
                "Name raw": cookie['name'],
                "Content": cookie['value'],
                "Content raw": cookie['value']
            })
        export.append(dict(temp_cookie))

export = json.dumps(export, indent=2)
with open(output, 'w') as browser_cookies:
    browser_cookies.write(export)
print('[✓] Success! Cookies saved to {}'.format(output))