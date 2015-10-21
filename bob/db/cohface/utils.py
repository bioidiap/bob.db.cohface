#!/usr/bin/env python
# encoding: utf-8
# Andre Anjos <andre.anjos@idiap.ch>
# Thu  1 Oct 11:00:44 CEST 2015

'''Utilities for Remote Photo-Plethysmography Benchmarking'''

import os
import numpy
import bob.io.video
import bob.ip.draw
import bob.ip.facedetect
from .detect_peaks import detect_peaks

def estimate_average_heartrate(s, sampling_frequency):
  '''Estimates the average heart rate taking as base the input signal and its
  sampling frequency.

  This method will use :py:func:`detect_peaks` to figure out the
  peaks in the noisy signal defined at ``s``.

  Returns:

    float: The estimated average heart-rate in beats-per-minute
    peaks: A 1D numpy.ndarray with the peak points

  '''

  min_distance = 60 * sampling_frequency / 120 #BPM

  peaks = detect_peaks(s, mpd=min_distance)
  instantaneous_rates = (sampling_frequency * 60) / numpy.diff(peaks)

  # remove instantaneous rates which are lower than 30, higher than 240
  selector = (instantaneous_rates>30) & (instantaneous_rates<240)
  return float(numpy.nan_to_num(instantaneous_rates[selector].mean())), peaks


def plot_signal(s, sampling_frequency):
  '''Estimates the heart rate taking as base the input signal and its sampling
  frequency, plots QRS peaks discovered on the base signal.

  This method will use the Pam-Tompkins detector available the MNE package to
  clean-up and estimate the heart-beat frequency based on the ECG sensor
  information provided.

  Returns:

    float: The estimated average heart-rate in beats-per-minute

  '''
  import matplotlib.pyplot as plt

  avg, peaks = estimate_average_heartrate(s, sampling_frequency)

  ax = plt.gca()
  ax.plot(numpy.arange(0, len(s)/sampling_frequency, 1/sampling_frequency),
          s, label='Raw signal');
  xmin, xmax, ymin, ymax = plt.axis()
  ax.vlines(peaks / sampling_frequency, ymin, ymax, colors='r', label='Peak Detector')
  plt.xlim(0, len(s)/sampling_frequency)
  plt.ylabel('uV')
  plt.xlabel('time (s)')
  plt.title('Average heart-rate = %d bpm' % avg)
  ax.grid(True)
  ax.legend(loc='best', fancybox=True, framealpha=0.5)

  return avg, peaks


def annotate_video(video, annotations, output, thickness=3,
        color=(255, 0, 0)):
  '''Annotates the input video with the detected bounding boxes'''

  directory = os.path.dirname(output)
  if not os.path.exists(directory): os.makedirs(directory)

  writer = bob.io.video.writer(output, height=video.height, width=video.width,
          framerate=video.frame_rate, codec=video.codec_name)
  for k, frame in enumerate(video):
    bb = annotations.get(k)
    if bb is not None:
      for t in range(thickness):
        bob.ip.draw.box(frame, bb.topleft, bb.size, color)
    writer.append(frame)
  del writer


def explain_heartrate(obj, dbdir, output):
  '''Explains why the currently chosen heart-rate is what it is'''

  import matplotlib
  matplotlib.use('agg')
  import matplotlib.pyplot as plt
  from matplotlib.backends.backend_pdf import PdfPages

  directory = os.path.dirname(output)
  if not os.path.exists(directory): os.makedirs(directory)

  # plots
  estimates = []
  pp = PdfPages(output)
  for k, channel in enumerate(('EXG1', 'EXG2', 'EXG3')):
    plt.figure(figsize=(12,4))
    signal, freq = bdf_load_signal(obj.make_path(dbdir), channel)
    avg_hr, peaks = plot_signal(signal, freq, channel)
    estimates.append(avg_hr)
    pp.savefig()
  estimated = chooser(estimates)
  pp.close()
