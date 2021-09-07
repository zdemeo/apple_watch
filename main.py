from lib.AppleWatchParser import AppleWatchParser


def main():

	# Path to Apple Watch XML file
	watch_xml = 'export.xml'

	# Directory where .CSVs are dumped out to
	csv_directory = '.'

	# Data categories to parse. Will ignore any categories not defined here.
	# NOTE: No other categories have been tested other than the ones below.
	categories_to_parse = ['HKQuantityTypeIdentifierBodyMass', 'HKQuantityTypeIdentifierOxygenSaturation',
						   'HKQuantityTypeIdentifierStepCount',
						   'HKQuantityTypeIdentifierDistanceWalkingRunning',
						   'HKQuantityTypeIdentifierAppleExerciseTime', 'HKQuantityTypeIdentifierDistanceCycling',
						   'HKQuantityTypeIdentifierRestingHeartRate',
						   'HKQuantityTypeIdentifierWalkingHeartRateAverage',
						   'HKQuantityTypeIdentifierAppleStandTime', 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN',
						   'HKCategoryTypeIdentifierSleepAnalysis', 'HKQuantityTypeIdentifierActiveEnergyBurned', 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN']

	watch_data = AppleWatchParser(watch_xml, categories_to_parse)
	watch_data.to_csv(csv_directory)


if __name__ == '__main__':
	main()
