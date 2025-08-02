import struct
import sys

class CimgInt:
	def __init__(self, value, length):
		self.value = value
		self.length = length

	def to_bytes(self, endian="little"):
		return self.value.to_bytes(self.length, endian)

class CimgHeader:
	def __init__(self, magic_numbers, version, width, height):
		self.magic_numbers = magic_numbers
		self.version = version
		self.width = width
		self.height = height

	def to_bytes(self, endian="little"):
		header_data = self.magic_numbers + self.version.to_bytes(endian) + self.width.to_bytes(endian) + self.height.to_bytes(endian)
		return header_data

class Cimg:
	def __init__(self, header, data):
		self.header = header
		self.data = data

	def write_to_file(self, file_name):
		with open(file_name, 'wb') as f:
			f.write(self.header.to_bytes())
			for i in range(self.header.width.value*self.header.height.value):
				f.write(self.data)
			f.close()


image_file = 'image.cimg'

magic_numbers = b'BYTE'
version = 1
width = 1
height = 1
image_data = b'\x00' 

cimage = Cimg( CimgHeader( magic_numbers, CimgInt(version, 1), CimgInt(width, 1), CimgInt(height, 1) ), image_data )
cimage.write_to_file(image_file)

