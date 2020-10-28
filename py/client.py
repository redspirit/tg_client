from telethon import TelegramClient, events, sync
from http.server import BaseHTTPRequestHandler, HTTPServer

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 1902353
api_hash = '38306976eb0d10a6cbec59366fdd04b6'

client = TelegramClient('session_name', api_id, api_hash)




@client.on(events.NewMessage(incoming=True, outgoing=False, from_users='GenerativeBeast2Bot'))
async def handler(event):
	print(event.raw_text)



#client.start()

# client.send_message('GenerativeBeast2Bot', 'как дела???')

#client.run_until_disconnected()


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        '''Reads post request body'''
        self._set_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))


host = ''
port = 8001
HTTPServer((host, port), HandleRequests).serve_forever()