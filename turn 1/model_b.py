import unittest
import pandas as pd

class DataLogger:
	def __init__(self):
		self.log = []

	def log_data(self, data):
		self.log.append(data)

	def detect_anomaly(self, threshold=100):
		if not self.log:
			raise ValueError("Log is empty")
		return any(abs(value) > threshold for value in self.log[-1])


class TestDataLogger(unittest.TestCase):

	def setUp(self):
		self.logger = DataLogger()

	def test_no_anomaly(self):
		dummy_data = pd.Series([1, 2, 3, 4, 5])
		self.logger.log_data(dummy_data)
		self.assertFalse(self.logger.detect_anomaly())

	def test_one_anomaly(self):
		dummy_data = pd.Series([1, 2, 100, 4, 5])
		self.logger.log_data(dummy_data)
		self.assertTrue(self.logger.detect_anomaly())

	def test_multiple_anomalies(self):
		dummy_data = pd.Series([-100, 1, 2, 1000, 4, 5, -200])
		self.logger.log_data(dummy_data)
		self.assertTrue(self.logger.detect_anomaly())

	def test_anomaly_with_custom_threshold(self):
		dummy_data = pd.Series([1, 2, 3, 4, 500, 6])
		self.logger.log_data(dummy_data)
		self.assertTrue(self.logger.detect_anomaly(threshold=400))

	def test_detect_anomaly_empty_log(self):
		with self.assertRaises(ValueError):
			self.logger.detect_anomaly()

if __name__ == '__main__':
	unittest.main()
