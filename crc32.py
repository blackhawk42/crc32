#!/usr/bin/env python3.6

import sys
import zlib
import getopt

def crc32(filename, chunk_size=1024):
	"""Generates CRC32 of a file and outputs it's hexadecimal value
	in a string. Because it does it by chunks, it can read large
	files without running out of memory"""

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
