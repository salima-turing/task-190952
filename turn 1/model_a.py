import unittest
import pandas as pd
from scipy import stats

class TestAnomalyDetection(unittest.TestCase):
	def setUp(self):
		# Dummy data for testing
		self.data = pd.DataFrame({
			'timestamp': ['2023-07-28 00:00', '2023-07-28 00:01', '2023-07-28 00:02', '2023-07-28 00:03', '2023-07-28 00:04'],
			'value': [100, 120, 80, 110, 150]
		})
		self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])

		self.threshold = 1.5

	def test_detect_simple_anomaly(self):
		z_scores = stats.zscore(self.data['value'])
		anomalies = self.data[(z_scores > self.threshold) | (z_scores < -self.threshold)]

		expected_anomalies = pd.DataFrame({
			'timestamp': ['2023-07-28 00:02'],
			'value': [80]
		})
		expected_anomalies['timestamp'] = pd.to_datetime(expected_anomalies['timestamp'])
		pd.testing.assert_frame_equal(anomalies.reset_index(drop=True), expected_anomalies, "Anomaly detection failed")

	if __name__ == '__main__':
		unittest.main()
