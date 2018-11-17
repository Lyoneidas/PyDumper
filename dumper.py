import json
import time
import datetime
import sys
import os
from PBar.progressBar import ProgressBar

def dumper(_from, to):
	w=open(to, "w")
	size = os.path.getsize(_from)
	step = long(len(open(_from).readline()))
	t = size/step
	_bar = ProgressBar(total = t)
	with open(_from, "r") as f:
		for line in f:
			_bar.move()
			_bar.log()
			obj_str = line.split()[2]#Getting the actual bid/ask data
			obj = json.loads(obj_str)#Load the bid/ask data into Json object
			timestamp = str(obj['timestamp'])
			product = obj['product']

			#Start handling ask list
			asks = obj['asks']
			ask_seq = 1
			for k,v in asks.items():
				ask_name = 'ask'+`ask_seq`
				price = float('%.4f'%float(k))
				size = v
				if ask_seq != 1:
					w.write('\n')
				w.write(`timestamp` + ',' + product + ',' + ask_name + ',' + `price` + ',' + `size`)
				ask_seq+=1

			w.write('\n')

			#handling bid list
			bids = obj['bids']
			bid_seq = 1
			for k,v in bids.items():
				bid_name = 'bid'+`bid_seq`
				price = float('%.4f'%float(k))
				size = v
				if bid_seq != 1:
					w.write('\n')
				w.write(`timestamp` + ',' + product + ',' + bid_name + ',' + `price` + ',' + `size`)
				bid_seq+=1
	w.close()
	f.close()

conf_file = sys.argv[2] if (len(sys.argv)> 1 and (sys.argv[1] == '-c' or sys.argv[1] == '-C')) else 'config.json'
conf = json.loads(open(conf_file, "r").read())
from_dump = conf['from']
to_dump = conf['to']
dumper(from_dump, to_dump)
