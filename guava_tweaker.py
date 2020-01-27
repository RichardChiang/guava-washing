import cv2

class GuavaTweaker:
    def __init__(self, window_name='image'):
        self.window_name = window_name
        self.threshold_names = ['threshold-lblue', 'threshold-dblue', 'threshold-red', 'threshold-green']

    # need a function that doesnt do anything like me
    def nada(*args):
        pass

    def debug(self):
        window = self.window_name

        # create trackbars for each color's threshold
        for variable_name in self.threshold_names:
            cv2.createTrackbar(variable_name, window, 0, 100, self.nada)
