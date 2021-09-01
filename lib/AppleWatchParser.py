"""
A simple class for parsing Apple Watch XML data.
Author: Zac DeMeo

"""

class AppleWatchParser:

	def __init__(self, xml_path, categories):
		"""
		Read in and parse raw Apple Watch XML data
		:param xml_path: Path to Apple Watch XMl file
		"""
		import xml.etree.ElementTree as ET

		self.categories = categories
		self.raw_data = ET.parse(xml_path)

		# Get data labels. Exploratory.
		data_labels = self.__get_labels()

		self.parsed_data = self.__parse()

		print('hi')

	def __parse(self):
		"""
		Parse all Apple Watch data from categories. Assumes that each entry has creationDate, value, and unit attributes.
		:param categories: List of categories to parse
		:return: Dictionary of
		"""

		from dateutil import parser

		temp = {}

		for child in self.raw_data.getroot():

			# First few entries don't have 'type' attributes and are useless for this data. Skip them.
			# Skip any types not defined in categories.
			if child.attrib.get('type') is None or child.attrib.get('type') not in self.categories:
				continue

			try:
				temp[child.attrib['type']].append([parser.parse(child.attrib['creationDate']),
				                                   float(child.attrib['value']),
				                                   child.attrib['unit']])
			except KeyError:
				temp[child.attrib['type']] = []
				temp[child.attrib['type']].append([parser.parse(child.attrib['creationDate']),
				                                   float(child.attrib['value']),
				                                   child.attrib['unit']])

		return temp

	def __get_labels(self):
		"""
		The Apple Watch categorizes each measurement into one of many categories.
		Returns a list of each of these categories.
		:return: List of type attributes
		"""

		temp = []

		for child in self.raw_data.getroot():
			try:
				if child.attrib['type'] not in temp:
					temp.append(child.attrib['type'])
			except KeyError:
				# Ignore missing keys
				pass

		return temp

	def to_csv(self, path):
		"""
		Writes all Apple Watch health categories into a corresponding CSV file.
		:param path: Directory to write CSV files to
		"""
		import os

		for category in self.categories:
			outpath = os.path.join(path, category + '.csv')

			with open(outpath, 'w') as f:
				f.write('Date,Value,Unit\n')  # Header
				for entry in self.parsed_data[category]:
					line = '{},{},{}\n'.format(str(entry[0]), str(entry[1]), str(entry[2]))
					f.write(line)


	def to_dataframe(self):
		pass
