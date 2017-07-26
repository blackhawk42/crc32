#!/usr/bin/env python3

import sys
import zlib
import getopt

def crc32(filename, chunk_size=1024):
	crc = 0
	with open(filename, "rb") as f:
		while True:
			data = f.read(chunk_size)
			if not data:
				break
			crc = zlib.crc32(data, crc) & 0xffffffff
	return '{:08X}'.format(crc)

if __name__ == "__main__":
	options = ''
	long_options = []
	opts, args = getopt.gnu_getopt(sys.argv[1:], options, long_options)
	
	for f in args:
		print('{}: {}'.format(f, crc32(f) ))
