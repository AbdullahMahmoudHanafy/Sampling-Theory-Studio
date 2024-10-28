import numpy as np
import pyqtgraph as pg

class FrequencyPlotController:
    def __init__(self, main):
        self.main = main
        
    def plot_frequency_domain(self):
        # Get data from the displayed signal
        signal = np.array(self.main.displayed_signal.y_data)
        sampling_rate = self.main.displayed_signal.sampling_freq * 2
        number_of_samples = len(signal)
        
        # Calculate FFT
        fft_data = np.fft.fftshift(np.fft.fft(signal))
        X_mag = np.abs(fft_data)
        f = np.linspace(sampling_rate/-2, sampling_rate/2, number_of_samples)

        # Clear previous plot
        self.main.frequency_domain_plot.clear()
        
        # Add Nyquist frequency markers
        nyquist = sampling_rate/2
        self.main.frequency_domain_plot.addLine(x=nyquist, pen='r')
        self.main.frequency_domain_plot.addLine(x=-nyquist, pen='r')
        
        # Plot magnitude spectrum
        self.main.frequency_domain_plot.plot(f, X_mag, pen='b')
        self.main.frequency_domain_plot.plot(f[np.argmax(X_mag)], np.max(X_mag), symbol='x', symbolPen='y')
        
        # Set labels
        self.main.frequency_domain_plot.setLabel('bottom', 'Frequency (Hz)')
        self.main.frequency_domain_plot.setLabel('left', 'Magnitude')


# import sys
# import numpy as np
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtWidgets

# #hard_coded_x_data = [0.0, 0.008, 0.016, 0.024, 0.032, 0.04, 0.048, 0.056, 0.064, 0.072, 0.08, 0.088, 0.096, 0.104, 0.112, 0.12, 0.128, 0.136, 0.144, 0.152, 0.16, 0.168, 0.176, 0.184, 0.192, 0.2, 0.208, 0.216, 0.224, 0.232, 0.24, 0.248, 0.256, 0.264, 0.272, 0.28, 0.288, 0.296, 0.304, 0.312, 0.32, 0.328, 0.336, 0.344, 0.352, 0.36, 0.368, 0.376, 0.384, 0.392, 0.4, 0.408, 0.416, 0.424, 0.432, 0.44, 0.448, 0.456, 0.464, 0.472, 0.48, 0.488, 0.496, 0.504, 0.512, 0.52, 0.528, 0.536, 0.544, 0.552, 0.56, 0.568, 0.576, 0.584, 0.592, 0.6, 0.608, 0.616, 0.624, 0.632, 0.64, 0.648, 0.656, 0.664, 0.672, 0.68, 0.688, 0.696, 0.704, 0.712, 0.72, 0.728, 0.736, 0.744, 0.752, 0.76, 0.768, 0.776, 0.784, 0.792, 0.8, 0.808, 0.816, 0.824, 0.832, 0.84, 0.848, 0.856, 0.864, 0.872, 0.88, 0.888, 0.896, 0.904, 0.912, 0.92, 0.928, 0.936, 0.944, 0.952, 0.96, 0.968, 0.976, 0.984, 0.992, 1.0, 1.008, 1.016, 1.024, 1.032, 1.04, 1.048, 1.056, 1.064, 1.072, 1.08, 1.088, 1.096, 1.104, 1.112, 1.12, 1.128, 1.136, 1.144, 1.152, 1.16, 1.168, 1.176, 1.184, 1.192, 1.2, 1.208, 1.216, 1.224, 1.232, 1.24, 1.248, 1.256, 1.264, 1.272, 1.28, 1.288, 1.296, 1.304, 1.312, 1.32, 1.328, 1.336, 1.344, 1.352, 1.36, 1.368, 1.376, 1.384, 1.392, 1.4, 1.408, 1.416, 1.424, 1.432, 1.44, 1.448, 1.456, 1.464, 1.472, 1.48, 1.488, 1.496, 1.504, 1.512, 1.52, 1.528, 1.536, 1.544, 1.552, 1.56, 1.568, 1.576, 1.584, 1.592, 1.6, 1.608, 1.616, 1.624, 1.632, 1.64, 1.648, 1.656, 1.664, 1.672, 1.68, 1.688, 1.696, 1.704, 1.712, 1.72, 1.728, 1.736, 1.744, 1.752, 1.76, 1.768, 1.776, 1.784, 1.792, 1.8, 1.808, 1.816, 1.824, 1.832, 1.84, 1.848, 1.856, 1.864, 1.872, 1.88, 1.888, 1.896, 1.904, 1.912, 1.92, 1.928, 1.936, 1.944, 1.952, 1.96, 1.968, 1.976, 1.984, 1.992, 2.0, 2.008, 2.016, 2.024, 2.032, 2.04, 2.048, 2.056, 2.064, 2.072, 2.08, 2.088, 2.096, 2.104, 2.112, 2.12, 2.128, 2.136, 2.144, 2.152, 2.16, 2.168, 2.176, 2.184, 2.192, 2.2, 2.208, 2.216, 2.224, 2.232, 2.24, 2.248, 2.256, 2.264, 2.272, 2.28, 2.288, 2.296, 2.304, 2.312, 2.32, 2.328, 2.336, 2.344, 2.352, 2.36, 2.368, 2.376, 2.384, 2.392, 2.4, 2.408, 2.416, 2.424, 2.432, 2.44, 2.448, 2.456, 2.464, 2.472, 2.48, 2.488, 2.496, 2.504, 2.512, 2.52, 2.528, 2.536, 2.544, 2.552, 2.56, 2.568, 2.576, 2.584, 2.592, 2.6, 2.608, 2.616, 2.624, 2.632, 2.64, 2.648, 2.656, 2.664, 2.672, 2.68, 2.688, 2.696, 2.704, 2.712, 2.72, 2.728, 2.736, 2.744, 2.752, 2.76, 2.768, 2.776, 2.784, 2.792, 2.8, 2.808, 2.816, 2.824, 2.832, 2.84, 2.848, 2.856, 2.864, 2.872, 2.88, 2.888, 2.896, 2.904, 2.912, 2.92, 2.928, 2.936, 2.944, 2.952, 2.96, 2.968, 2.976, 2.984, 2.992, 3.0, 3.008, 3.016, 3.024, 3.032, 3.04, 3.048, 3.056, 3.064, 3.072, 3.08, 3.088, 3.096, 3.104, 3.112, 3.12, 3.128, 3.136, 3.144, 3.152, 3.16, 3.168, 3.176, 3.184, 3.192, 3.2, 3.208, 3.216, 3.224, 3.232, 3.24, 3.248, 3.256, 3.264, 3.272, 3.28, 3.288, 3.296, 3.304, 3.312, 3.32, 3.328, 3.336, 3.344, 3.352, 3.36, 3.368, 3.376, 3.384, 3.392, 3.4, 3.408, 3.416, 3.424, 3.432, 3.44, 3.448, 3.456, 3.464, 3.472, 3.48, 3.488, 3.496, 3.504, 3.512, 3.52, 3.528, 3.536, 3.544, 3.552, 3.56, 3.568, 3.576, 3.584, 3.592, 3.6, 3.608, 3.616, 3.624, 3.632, 3.64, 3.648, 3.656, 3.664, 3.672, 3.68, 3.688, 3.696, 3.704, 3.712, 3.72, 3.728, 3.736, 3.744, 3.752, 3.76, 3.768, 3.776, 3.784, 3.792, 3.8, 3.808, 3.816, 3.824, 3.832, 3.84, 3.848, 3.856, 3.864, 3.872, 3.88, 3.888, 3.896, 3.904, 3.912, 3.92, 3.928, 3.936, 3.944, 3.952, 3.96, 3.968, 3.976, 3.984, 3.992, 4.0, 4.008, 4.016, 4.024, 4.032, 4.04, 4.048, 4.056, 4.064, 4.072, 4.08, 4.088, 4.096, 4.104, 4.112, 4.12, 4.128, 4.136, 4.144, 4.152, 4.16, 4.168, 4.176, 4.184, 4.192, 4.2, 4.208, 4.216, 4.224, 4.232, 4.24, 4.248, 4.256, 4.264, 4.272, 4.28, 4.288, 4.296, 4.304, 4.312, 4.32, 4.328, 4.336, 4.344, 4.352, 4.36, 4.368, 4.376, 4.384, 4.392, 4.4, 4.408, 4.416, 4.424, 4.432, 4.44, 4.448, 4.456, 4.464, 4.472, 4.48, 4.488, 4.496, 4.504, 4.512, 4.52, 4.528, 4.536, 4.544, 4.552, 4.56, 4.568, 4.576, 4.584, 4.592, 4.6, 4.608, 4.616, 4.624, 4.632, 4.64, 4.648, 4.656, 4.664, 4.672, 4.68, 4.688, 4.696, 4.704, 4.712, 4.72, 4.728, 4.736, 4.744, 4.752, 4.76, 4.768, 4.776, 4.784, 4.792, 4.8, 4.808, 4.816, 4.824, 4.832, 4.84, 4.848, 4.856, 4.864, 4.872, 4.88, 4.888, 4.896, 4.904, 4.912, 4.92, 4.928, 4.936, 4.944, 4.952, 4.96, 4.968, 4.976, 4.984, 4.992, 5.0, 5.008, 5.016, 5.024, 5.032, 5.04, 5.048, 5.056, 5.064, 5.072, 5.08, 5.088, 5.096, 5.104, 5.112, 5.12, 5.128, 5.136, 5.144, 5.152, 5.16, 5.168, 5.176, 5.184, 5.192, 5.2, 5.208, 5.216, 5.224, 5.232, 5.24, 5.248, 5.256, 5.264, 5.272, 5.28, 5.288, 5.296, 5.304, 5.312, 5.32, 5.328, 5.336, 5.344, 5.352, 5.36, 5.368, 5.376, 5.384, 5.392, 5.4, 5.408, 5.416, 5.424, 5.432, 5.44, 5.448, 5.456, 5.464, 5.472, 5.48, 5.488, 5.496, 5.504, 5.512, 5.52, 5.528, 5.536, 5.544, 5.552, 5.56, 5.568, 5.576, 5.584, 5.592, 5.6, 5.608, 5.616, 5.624, 5.632, 5.64, 5.648, 5.656, 5.664, 5.672, 5.68, 5.688, 5.696, 5.704, 5.712, 5.72, 5.728, 5.736, 5.744, 5.752, 5.76, 5.768, 5.776, 5.784, 5.792, 5.8, 5.808, 5.816, 5.824, 5.832, 5.84, 5.848, 5.856, 5.864, 5.872, 5.88, 5.888, 5.896, 5.904, 5.912, 5.92, 5.928, 5.936, 5.944, 5.952, 5.96, 5.968, 5.976, 5.984, 5.992, 6.0, 6.008, 6.016, 6.024, 6.032, 6.04, 6.048, 6.056, 6.064, 6.072, 6.08, 6.088, 6.096, 6.104, 6.112, 6.12, 6.128, 6.136, 6.144, 6.152, 6.16, 6.168, 6.176, 6.184, 6.192, 6.2, 6.208, 6.216, 6.224, 6.232, 6.24, 6.248, 6.256, 6.264, 6.272, 6.28, 6.288, 6.296, 6.304, 6.312, 6.32, 6.328, 6.336, 6.344, 6.352, 6.36, 6.368, 6.376, 6.384, 6.392, 6.4, 6.408, 6.416, 6.424, 6.432, 6.44, 6.448, 6.456, 6.464, 6.472, 6.48, 6.488, 6.496, 6.504, 6.512, 6.52, 6.528, 6.536, 6.544, 6.552, 6.56, 6.568, 6.576, 6.584, 6.592, 6.6, 6.608, 6.616, 6.624, 6.632, 6.64, 6.648, 6.656, 6.664, 6.672, 6.68, 6.688, 6.696, 6.704, 6.712, 6.72, 6.728, 6.736, 6.744, 6.752, 6.76, 6.768, 6.776, 6.784, 6.792, 6.8, 6.808, 6.816, 6.824, 6.832, 6.84, 6.848, 6.856, 6.864, 6.872, 6.88, 6.888, 6.896, 6.904, 6.912, 6.92, 6.928, 6.936, 6.944, 6.952, 6.96, 6.968, 6.976, 6.984, 6.992, 7.0, 7.008, 7.016, 7.024, 7.032, 7.04, 7.048, 7.056, 7.064, 7.072, 7.08, 7.088, 7.096, 7.104, 7.112, 7.12, 7.128, 7.136, 7.144, 7.152, 7.16, 7.168, 7.176, 7.184, 7.192, 7.2, 7.208, 7.216, 7.224, 7.232, 7.24, 7.248, 7.256, 7.264, 7.272, 7.28, 7.288, 7.296, 7.304, 7.312, 7.32, 7.328, 7.336, 7.344, 7.352, 7.36, 7.368, 7.376, 7.384, 7.392, 7.4, 7.408, 7.416, 7.424, 7.432, 7.44, 7.448, 7.456, 7.464, 7.472, 7.48, 7.488, 7.496, 7.504, 7.512, 7.52, 7.528, 7.536, 7.544, 7.552, 7.56, 7.568, 7.576, 7.584, 7.592, 7.6, 7.608, 7.616, 7.624, 7.632, 7.64, 7.648, 7.656, 7.664, 7.672, 7.68, 7.688, 7.696, 7.704, 7.712, 7.72, 7.728, 7.736, 7.744, 7.752, 7.76, 7.768, 7.776, 7.784, 7.792, 7.8, 7.808, 7.816, 7.824, 7.832, 7.84, 7.848, 7.856, 7.864, 7.872, 7.88, 7.888, 7.896, 7.904, 7.912, 7.92, 7.928, 7.936, 7.944, 7.952, 7.96, 7.968, 7.976, 7.984, 7.992]
# hard_coded_y_data = [0.72549, 0.67059, 0.6098, 0.55098, 0.5, 0.4549, 0.4098, 0.3902, 0.37451, 0.35882, 0.3549, 0.34902, 0.3549, 0.36471, 0.3549, 0.36471, 0.37451, 0.37059, 0.3902, 0.3902, 0.3902, 0.39412, 0.40392, 0.40392, 0.4, 0.39412, 0.38431, 0.38431, 0.38039, 0.3902, 0.40392, 0.41961, 0.41961, 0.42549, 0.42549, 0.4, 0.3902, 0.40392, 0.41961, 0.42941, 0.43529, 0.42941, 0.41569, 0.4098, 0.41569, 0.41961, 0.40392, 0.34902, 0.6549, 1.5039, 1.5039, 1.5039, 0.66078, 0.42941, 0.41961, 0.40392, 0.38431, 0.34902, 0.33922, 0.3549, 0.38039, 0.38039, 0.3902, 0.40392, 0.39412, 0.40392, 0.42941, 0.43529, 0.43922, 0.46078, 0.48431, 0.51569, 0.55098, 0.60588, 0.6549, 0.69608, 0.72549, 0.74118, 0.75098, 0.74118, 0.71569, 0.66471, 0.60588, 0.5451, 0.47451, 0.42941, 0.38431, 0.3451, 0.31961, 0.3098, 0.3098, 0.3098, 0.30392, 0.29412, 0.3, 0.32941, 0.32941, 0.32353, 0.33922, 0.32941, 0.33529, 0.33922, 0.33922, 0.33922, 0.33922, 0.33529, 0.32941, 0.31961, 0.32941, 0.33529, 0.33922, 0.3549, 0.36471, 0.3451, 0.33529, 0.31373, 0.3098, 0.31373, 0.32941, 0.31961, 0.33529, 0.3098, 0.3098, 0.30392, 0.3098, 0.31373, 0.26471, 0.4549, 1.2078, 1.5039, 1.5039, 0.82549, 0.33529, 0.31373, 0.33529, 0.31373, 0.3098, 0.30392, 0.3098, 0.31373, 0.3098, 0.33529, 0.33529, 0.34902, 0.36471, 0.37451, 0.40392, 0.42549, 0.44902, 0.48039, 0.51569, 0.57059, 0.6098, 0.67647, 0.73137, 0.77647, 0.8, 0.8, 0.8, 0.77647, 0.71569, 0.65098, 0.58431, 0.50588, 0.43529, 0.37059, 0.32941, 0.2902, 0.25882, 0.23922, 0.22941, 0.23922, 0.2549, 0.26471, 0.28431, 0.30392, 0.32941, 0.3451, 0.3549, 0.37059, 0.38039, 0.38431, 0.39412, 0.38431, 0.38431, 0.38039, 0.37451, 0.37059, 0.36471, 0.35882, 0.37451, 0.38431, 0.38039, 0.35882, 0.34902, 0.31373, 0.3098, 0.31961, 0.33529, 0.33922, 0.33529, 0.33529, 0.32353, 0.32941, 0.33529, 0.3451, 0.3, 0.25882, 0.71569, 1.5039, 1.5039, 1.3784, 0.51961, 0.40392, 0.4098, 0.37059, 0.3549, 0.33529, 0.3549, 0.37059, 0.37451, 0.36471, 0.38039, 0.38039, 0.38039, 0.4, 0.41961, 0.41961, 0.46078, 0.47451, 0.50588, 0.52549, 0.5902, 0.61961, 0.67647, 0.72157, 0.75098, 0.77647, 0.77059, 0.77059, 0.7451, 0.6902, 0.62941, 0.56471, 0.50588, 0.4549, 0.41569, 0.3902, 0.36471, 0.3451, 0.33529, 0.32941, 0.33529, 0.32353, 0.33922, 0.35882, 0.36471, 0.37451, 0.36471, 0.38039, 0.38431, 0.39412, 0.40392, 0.38039, 0.39412, 0.39412, 0.38039, 0.37451, 0.37059, 0.37451, 0.3902, 0.4, 0.39412, 0.3902, 0.38039, 0.3549, 0.31961, 0.3451, 0.35882, 0.37451, 0.37059, 0.37451, 0.33922, 0.34902, 0.33922, 0.34902, 0.3549, 0.26863, 0.44902, 1.1765, 1.5039, 1.5039, 0.81569, 0.4549, 0.42941, 0.4, 0.36471, 0.34902, 0.33922, 0.34902, 0.37059, 0.35882, 0.38039, 0.39412, 0.40392, 0.41569, 0.41961, 0.42941, 0.44902, 0.47059, 0.4902, 0.51961, 0.56471, 0.6, 0.6451, 0.69608, 0.7451, 0.77647, 0.79608, 0.79608, 0.78039, 0.74118, 0.7, 0.65098, 0.58431, 0.52549, 0.48039, 0.4549, 0.42941, 0.41569, 0.4, 0.3902, 0.3902, 0.40392, 0.41569, 0.4098, 0.41961, 0.42549, 0.41961, 0.42549, 0.41569, 0.42549, 0.42549, 0.41569, 0.4098, 0.40392, 0.39412, 0.40392, 0.4, 0.38039, 0.40392, 0.4098, 0.40392, 0.41569, 0.39412, 0.37451, 0.36471, 0.35882, 0.35882, 0.36471, 0.3549, 0.35882, 0.34902, 0.33922, 0.33529, 0.33529, 0.3451, 0.27451, 0.42941, 1.0922, 1.5039, 1.5039, 0.89608, 0.35882, 0.33922, 0.3549, 0.33529, 0.3098, 0.31373, 0.3098, 0.31961, 0.33529, 0.32941, 0.3451, 0.3549, 0.35882, 0.37059, 0.37451, 0.3902, 0.41961, 0.4451, 0.48039, 0.52941, 0.57059, 0.61961, 0.68627, 0.72549, 0.74118, 0.7451, 0.7549, 0.72549, 0.68627, 0.61569, 0.56471, 0.49412, 0.41961, 0.37059, 0.34902, 0.32941, 0.3, 0.30392, 0.28431, 0.2902, 0.28431, 0.3, 0.3098, 0.30392, 0.32941, 0.33529, 0.33529, 0.33529, 0.33922, 0.3549, 0.3549, 0.3549, 0.3549, 0.34902, 0.33922, 0.3451, 0.34902, 0.3549, 0.36471, 0.37059, 0.37059, 0.37451, 0.33529, 0.31961, 0.33529, 0.33922, 0.3451, 0.32353, 0.32353, 0.30392, 0.3, 0.3098, 0.3098, 0.2902, 0.2549, 0.65098, 1.5039, 1.5039, 1.4627, 0.50588, 0.32941, 0.35882, 0.36471, 0.37059, 0.35882, 0.33529, 0.33529, 0.34902, 0.37059, 0.38039, 0.4, 0.39412, 0.40392, 0.41961, 0.42549, 0.42941, 0.4549, 0.49412, 0.52941, 0.57451, 0.63529, 0.69608, 0.76078, 0.7902, 0.82549, 0.81176, 0.79608, 0.76078, 0.70588, 0.63529, 0.58039, 0.50588, 0.46078, 0.40392, 0.38039, 0.3549, 0.3451, 0.33529, 0.32941, 0.33529, 0.33529, 0.3451, 0.3549, 0.35882, 0.3549, 0.38039, 0.38039, 0.3902, 0.40392, 0.39412, 0.4, 0.39412, 0.40392, 0.3902, 0.38039, 0.36471, 0.35882, 0.38039, 0.4, 0.4098, 0.4, 0.4098, 0.38431, 0.3549, 0.34902, 0.3451, 0.37451, 0.36471, 0.37059, 0.35882, 0.3451, 0.33922, 0.33922, 0.33922, 0.27451, 0.26471, 0.94118, 1.5039, 1.5039, 1.1059, 0.48039, 0.41961, 0.38431, 0.3549, 0.32941, 0.31961, 0.32941, 0.34902, 0.3451, 0.36471, 0.37451, 0.37059, 0.38039, 0.3902, 0.40392, 0.41961, 0.43922, 0.46471, 0.4902, 0.53922, 0.58039, 0.62549, 0.68627, 0.70588, 0.74118, 0.75098, 0.76667, 0.75098, 0.7098, 0.6549, 0.6098, 0.5549, 0.49412, 0.43922, 0.40392, 0.39412, 0.38039, 0.37451, 0.35882, 0.37059, 0.36471, 0.37059, 0.36471, 0.38039, 0.38431, 0.3902, 0.39412, 0.4, 0.4, 0.39412, 0.4098, 0.4098, 0.40392, 0.4, 0.39412, 0.3902, 0.38039, 0.3902, 0.4098, 0.42941, 0.43922, 0.43529, 0.41961, 0.4, 0.40392, 0.41569, 0.43922, 0.42941, 0.42941, 0.42549, 0.41961, 0.41569, 0.42549, 0.42941, 0.36471, 0.3549, 0.99216, 1.5039, 1.5039, 1.1471, 0.5098, 0.43529, 0.42549, 0.40392, 0.38431, 0.36471, 0.35882, 0.38039, 0.37451, 0.38431, 0.3902, 0.4, 0.40392, 0.41961, 0.42941, 0.4451, 0.44902, 0.47451, 0.5098, 0.53529, 0.57059, 0.62941, 0.68039, 0.7098, 0.73137, 0.7451, 0.7451, 0.72549, 0.69608, 0.64118, 0.58039, 0.51961, 0.46078, 0.4, 0.37059, 0.34902, 0.33529, 0.31373, 0.30392, 0.3098, 0.3098, 0.3098, 0.32353, 0.33529, 0.32941, 0.33529, 0.33922, 0.34902, 0.33529, 0.3451, 0.3451, 0.32941, 0.33529, 0.33529, 0.3098, 0.32941, 0.3549, 0.34902, 0.3549, 0.34902, 0.3549, 0.31961, 0.3098, 0.3098, 0.3098, 0.32941, 0.31961, 0.31961, 0.32941, 0.3, 0.31373, 0.31373, 0.32353, 0.25882, 0.49412, 1.3569, 1.5039, 1.5039, 0.68039, 0.3, 0.32941, 0.33529, 0.31373, 0.28431, 0.28431, 0.3098, 0.31961, 0.31373, 0.31961, 0.32941, 0.33922, 0.3549, 0.37451, 0.3902, 0.40392, 0.4451, 0.48039, 0.5098, 0.55098, 0.60588, 0.66078, 0.7098, 0.7451, 0.76667, 0.77059, 0.7549, 0.72549, 0.67059, 0.6, 0.51961, 0.43922, 0.38039, 0.32941, 0.29412, 0.27451, 0.26471, 0.26471, 0.26863, 0.28431, 0.30392, 0.31373, 0.31961, 0.32941, 0.3451, 0.33922, 0.36471, 0.37451, 0.37451, 0.38039, 0.36471, 0.37059, 0.3451, 0.33922, 0.33529, 0.33529, 0.33922, 0.37059, 0.38039, 0.38039, 0.37059, 0.38039, 0.33922, 0.32353, 0.33529, 0.33922, 0.3549, 0.35882, 0.34902, 0.33529, 0.32941, 0.32941, 0.33922, 0.3549, 0.26863, 0.59608, 1.5039, 1.5039, 1.5039, 0.60588, 0.4098, 0.39412, 0.37451, 0.34902, 0.34902, 0.3451, 0.35882, 0.3549, 0.36471, 0.3902, 0.38039, 0.38431, 0.40392, 0.4098, 0.40392, 0.46078, 0.48431, 0.5, 0.52941, 0.57059, 0.6098, 0.68039, 0.71569, 0.75098, 0.76667, 0.77647, 0.76667, 0.73529, 0.6902, 0.62941, 0.57059, 0.5098, 0.46471, 0.41961, 0.3902, 0.35882, 0.3549, 0.34902, 0.33922, 0.3451, 0.3549, 0.36471, 0.35882, 0.35882, 0.37451, 0.38039, 0.3902, 0.40392, 0.4098, 0.4, 0.39412, 0.38431, 0.38039, 0.37059, 0.36471, 0.37451, 0.3902, 0.40392, 0.41569, 0.40392, 0.4, 0.38039, 0.3549, 0.3549, 0.34902, 0.37451, 0.38431, 0.37059, 0.34902, 0.33922, 0.3549, 0.34902, 0.35882, 0.27843, 0.26471, 0.92157, 1.5039, 1.5039, 1.0412, 0.47059, 0.41569, 0.38039, 0.37451, 0.34902, 0.33529, 0.31961, 0.34902, 0.3549, 0.3451, 0.38039, 0.38431, 0.3902, 0.40392, 0.41569, 0.42549, 0.43922, 0.46471, 0.49412, 0.53922, 0.58039, 0.62549, 0.67647, 0.70588, 0.74118, 0.7549, 0.75098, 0.73529, 0.70588, 0.66078, 0.60588, 0.55098, 0.50588, 0.46078, 0.42941, 0.4098, 0.40392, 0.40392, 0.4, 0.40392, 0.42549, 0.42941, 0.43529, 0.4451, 0.44902, 0.44902, 0.4451, 0.4451, 0.44902, 0.44902, 0.43922, 0.43529, 0.43529, 0.42549, 0.41961, 0.41961, 0.41569, 0.42941, 0.43922, 0.43529, 0.42941, 0.41961, 0.3902, 0.38039, 0.38039, 0.39412, 0.40392, 0.3902, 0.38431, 0.38039, 0.35882, 0.36471, 0.35882, 0.37451, 0.29412, 0.65098, 1.5039, 1.5039, 1.5039, 0.55098, 0.35882, 0.38039, 0.3549, 0.33922, 0.32941, 0.33922, 0.33922, 0.33529, 0.33922, 0.3451, 0.35882, 0.35882, 0.37451, 0.38039, 0.3902, 0.4098, 0.42941, 0.4549, 0.49412, 0.53922, 0.58431, 0.63529, 0.68039, 0.70588, 0.72157, 0.73137, 0.72157, 0.68627, 0.64118, 0.58431, 0.50588, 0.4549, 0.40392, 0.35882, 0.33529, 0.3098, 0.2902, 0.29412, 0.2902, 0.28431, 0.3098, 0.30392, 0.3, 0.31961, 0.33922, 0.33529, 0.33922, 0.3549, 0.3451, 0.3549, 0.34902, 0.33922, 0.33529, 0.33922, 0.32941, 0.33529, 0.33529, 0.34902, 0.35882, 0.3549, 0.3451, 0.31373, 0.3098, 0.31373, 0.31961, 0.33529, 0.32353, 0.32941, 0.3098]


# max_freq = 62  # Hz
# sampling_rate = 124  

# number_of_samples = 1000
# signal = np.array(hard_coded_y_data)
# signal = signal - np.mean(signal)

# # Calculate FFT
# fft_data = np.fft.fftshift(np.fft.fft(signal))
# X_mag = np.abs(fft_data)
# f = np.linspace(sampling_rate/-2, sampling_rate/2, number_of_samples)

# # Initialize PyQtGraph application
# app = QtWidgets.QApplication([])
# win = pg.GraphicsLayoutWidget()
# win.setWindowTitle('FFT Visualization with Aliasing')

# p1 = win.addPlot(title="Magnitude Spectrum")

# # Plot data
# p1.plot(f, X_mag, pen='b')
# p1.setLabel('bottom', 'Frequency (Hz)')
# p1.setLabel('left', 'Magnitude')

# win.show()
# sys.exit(QtWidgets.QApplication.exec())
