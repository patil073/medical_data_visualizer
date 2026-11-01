import unittest
import medical_data_visualizer
import matplotlib as mpl

class DataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_cat_plot(self):
        actual = len(self.fig.axes)
        self.assertEqual(actual, 2, "Expected two axes in catplot figure.")
        
    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertEqual(type(fig), mpl.figure.Figure, "Expected heatmap return type to be a matplotlib Figure.")

if __name__ == "__main__":
    unittest.main()