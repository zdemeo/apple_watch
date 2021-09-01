from lib.AppleWatchParser import AppleWatchParser


def main():
    # Path to Apple Watch XML file
    watch_xml = 'export.xml'

    # Data categories to parse. Will ignore any categories not defined here.
    categories_to_parse = ['HKQuantityTypeIdentifierBodyMass', 'HKQuantityTypeIdentifierOxygenSaturation', 'HKQuantityTypeIdentifierStepCount',
                           'HKQuantityTypeIdentifierDistanceWalkingRunning', 'HKQuantityTypeIdentifierAppleExerciseTime', 'HKQuantityTypeIdentifierDistanceCycling',
                           'HKQuantityTypeIdentifierRestingHeartRate', 'HKQuantityTypeIdentifierWalkingHeartRateAverage',
                           'HKQuantityTypeIdentifierAppleStandTime', 'HKDataTypeSleepDurationGoal', 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN']

    watch_data = AppleWatchParser(watch_xml, categories_to_parse)
    watch_data.to_csv('.')


if __name__ == '__main__':
    main()