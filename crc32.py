#!/usr/bin/env python3.6

import sys
import os.path
import zlib
import getopt

usage = "usage: {} [-h|--help] FILE_1 [... FILE_N]".format(os.path.basename(sys.argv[0]))

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
	options = 'h'
	long_options = ["help"]
	opts, args = getopt.gnu_getopt(sys.argv[1:], options, long_options)
	for opt, arg in opts:
		if opt in ["-h", "--help"]:
			print(usage)
			sys.exit(0)
	
	if not args:
		print(usage, file=sys.stderr)
		exit(2)
	
	for f in args:
		print('{}: {}'.format(f, crc32(f) ))
