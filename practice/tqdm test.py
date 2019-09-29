from urllib.parse import urlencode

APP_ID = 7049864
BASE_URL = 'https://oauth.vk.com/authorize'
token = ''
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'offline',
    'response_type': 'token',
    'v': '5.101'
}

# print('?'.join((BASE_URL, urlencode(auth_data))))

TOKEN = 'e1cbc591030b2f83107f5a060e4a11ed97ade5e309bfb1d16f29f39dcbf31caeabf2982a58eb8afd65ed9'

from tqdm import tqdm
import time
import sys

for i in tqdm(range(10)):
    time.sleep(0.5)


pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.4)
    pbar.set_description("Processing %s" % char)

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)

pbar = tqdm(total=100, file=sys.stdout)
for i in range(10):
    time.sleep(0.2)
    pbar.update(10)
pbar.close()


