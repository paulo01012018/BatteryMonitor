#!/usr/bin/python
# *****BatteryMonitor Getdata from battery cells getdata.py*****
# Copyright (C) 2017 Simon Richard Matthews
# Project loaction https://github.com/simat/BatteryMonitor
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from config import config
#import smbus
#from Adafruit_I2C import Adafruit_I2C
import Adafruit_ADS1x15
for i in config['AtoDs']:
  exec(i + '=' + config['AtoDs'][i])

class Raw:
  # compile analog capture code to save CPU time
  vin = []
  for i in sorted(config['VoltageInputs']):
    vin = vin + [compile(config['VoltageInputs'][i], '<string>', 'eval')]
  #  vin = vin + [config['VoltageInputs'][i]]
  #for i in config['CurrentInputs']:
  #  config['CurrentInputs'][i] = compile(config['CurrentInputs'][i], '<string>', 'eval')
  iin = []
  for i in sorted(config['CurrentInputs']):
    iin = iin + [compile(config['CurrentInputs'][i], '<string>', 'eval')]

  rawi = [0.0 for i in iin]
  rawv = [ 0.0 for i in range(len(vin)+1)]

  def x(self):
    """ Get data for A/Ds, calibrate, covert and place in list variables"""

    for i in range(len(self.vin)):
      self.rawv[i+1] = eval(self.vin[i])/1000 # A to D 1 to 4 in volts
    for i in range(len(self.iin)):
      self.rawi[i] = eval(self.iin[i])
