#! python3
# coding: utf-8

blist = [1,2,3,255]

# bytes can't change
the_bytes = bytes(blist)
print(the_bytes)

# bytearray can change
the_bytes_array = bytearray(blist)
print(the_bytes_array)

# pay attention to the results
the_bytes2 = bytes(range(0, 256))
the_bytes_array2 = bytearray(range(0, 256))
print(the_bytes2)
print(the_bytes_array2)

#----------------- use struct to transform the binary data ------------------#
print('\n\nuse struct to transform the binary data\n\n')
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
	   b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
	# the '>' express big-endian
	# every 'L' express a unsigned long number
	width, height = struct.unpack('>LL', data[16:24])
	# the previous sentences can be replace by the follow
	# width, height = struct.unpack('>2L', data[16:24])
 
	print('Valid PNG, width', width, 'height', height)
else:
	print('Not a valid PNG')

########################## sign ###################################
#
#	<		little-endian
#	>		big-endian
#
########################## sign ###################################

########################## format sign ############################
#	sign		description						bytes
#	
#	x			jump a byte 					1
#	b			signed byte 					1
#	B			unsigned byte					1
#	h			short int						2
#	H			unsigned short int				2
#	i			int								4
#	I			unsigned int					4
#	l			long							4
#	L			unsigned long					4
#	Q			unsigned long long				8
#	f			float							4
#	d			double							8
#	p			number and character			1 + number
#	s			character						number
#
########################## format sign ############################

try:
	from construct import Struct, Magic, UBInt32, Const, String
	fmt = Struct('png',
			 Magic(b'\x89PNG\r\n\x1a\n'),
			 UBInt32('length'),
			 Const(String('type', 4), b'IHDR'),
			 UBInt32('width'),
			 UBInt32('height')
			)
	result = fmt.parse(data)
	print(result)
except:
	print(" construct error ")


# transform bytes and strings
import binascii
print(binascii.hexlify(valid_png_header))

print(binascii.unhexlify(binascii.hexlify(valid_png_header)))

