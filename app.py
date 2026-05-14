from prometheus_client import Counter,generate_latest
from flask import Flask
import socket
import os
import psutil
import subprocess

app = Flask(__name__)
#create metric

REQUEST_COUNT = Counter(
	'app_requests_total',
	'Total App Requests'

)
	


@app.route('/')
def home():

	REQUEST_COUNT.inc()

	hostname = socket.gethostname()
	#	ip = "127.0.0.1"     ---tem fix--
	try:
	    ip = scoket.gethostbyname(hostname)
	except:
	    ip = "IP NOT FOUND"

	cpu = psutil.cpu_percent(interval = 1)
	ram = psutil.virtual_memory().percent
	disk = psutil.disk_usage('/').percent
	boot = psutil.boot_time()
	net = psutil.net_io_counters()
	run = psutil.pids()

	#ping test

	ping = subprocess.run(
		["ping","-c","1","google.com"],
		capture_output = True,
		text = True
	)
	if ping.returncode == 0:
	   ping_status = "UP"
	else:
	   ping_status = "DOWN"

	#DNS TEST

	try:
	    dns_ip =socket.gethostbyname("google.com")
	except:
	    dns_ip = "DNS FAILED"



	#posrt Check
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = sock.connect_ex(("google.com",80))

	if result == 0:
            post_status = "OPEN"
	else:
	    post_status = "CLOSED"


	


	return f"""
	<h1>Devop network moniter</h1>
	<p><b>Hostname:</b> {hostname}</p>
	<p><b>IP Address:</b>{ip}</p>
	<p><b>System:</b> {os.name}</p>
	<p><b>CPU:</b> {cpu}</p>
	<p><b>RAM:</b> {ram}</p>
	<p><b>Boot:</b> {boot}</p>
	<p><b>Net: </b> {net}</p>
	<p><b>Runnning processes:</b> {run}</p>
	<p><b>DISK:</b> {disk}</p>
	<h2>Network Moniter</h>
	<p><b> Ping Status: </b> {ping_status} </p>
	<p><b> DNS Resolution:</b> {dns_ip }</p>
	<p><b> Port 80 Status : </b> {post_status}</p>
	"""

@app.route('/metrics')
def metrics():
	return generate_latest()


if __name__ == '__main__':
   app.run(host = '0.0.0.0',port = 5000)
	
