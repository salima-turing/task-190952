import unittest
import pandas as pd


class DataLogger:
    def __init__(self):
        self.log = []

    def log_data(self, data):
        self.log.append(data)

    def detect_anomaly(self, threshold=100):
        # Calculate the mean of the last 3 values to detect anomalies
        mean_of_last_three = pd.Series(self.log[-3:]).mean()
        return any(abs(value - mean_of_last_three) > threshold for value in self.log[-1])


# Unit tests for DataLogger
class TestDataLogger(unittest.TestCase):
    def setUp(self):
        self.logger = DataLogger()

    def test_no_anomaly(self):
        # Dummy data: Series of data without any anomalies
        dummy_data = pd.Series([1, 2, 3, 4, 5, 6])
        self.logger.log_data(dummy_data)
        self.assertFalse(self.logger.detect_anomaly())

    def test_one_anomaly(self):
        # Dummy data: A single anomaly in the middle
        dummy_data = pd.Series([1, 2, 100, 4, 5, 6])
        self.logger.log_data(dummy_data)
        self.assertTrue(self.logger.detect_anomaly())

    def test_multiple_anomalies(self):
        # Dummy data: Multiple anomalies at the beginning and end
        dummy_data = pd.Series([-100, 1, 2, 1000, 4, 5, -200])
        self.logger.log_data(dummy_data)
        self.assertTrue(self.logger.detect_anomaly())

    def test_anomaly_with_different_threshold(self):
        # Dummy data: An anomaly with a custom threshold
        dummy_data = pd.Series([1, 2, 3, 4, 500, 6])
        self.logger.log_data(dummy_data)
        with self.assertRaises(ValueError):
            # This should raise a ValueError since 500 is greater than the default threshold (100)
            self.logger.detect_anomaly()
            self.assertTrue(self.logger.detect_anomaly(threshold=400))

    def test_empty_log(self):
        # Check for anomaly in an empty log
        self.assertFalse(self.logger.detect_anomaly())

if __name__ == '__main__':
    unittest.main()
