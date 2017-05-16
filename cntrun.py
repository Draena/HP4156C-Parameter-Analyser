# designed to be run from terminal or interactive editor ie ipython
# runs a standard set of transfer and output measurements
# designed to characterize a backgated CNT FET on a silicon substrate

import parameter_analyser as pa
import sys
device = pa.initialize_device()
def run_transfer_series(device, fname, savedir):
    pa.define_transfer_smu()
    pa.measure_transfer(device, fname, savedir, -10, 10, 0.1, 0.1, 0, 1)
    pa.measure_transfer(device, fname, savedir, -20, 20, 0.1, 0.1, 0, 1)
    pa.measure_transfer(device, fname, savedir, -10, 10, 0.1, 0.01, 0, 1)
    pa.measure_transfer(device, fname, savedir, -20, 20, 0.1, 0.01, 0, 1)
    pa.measure_output(device, fname, savedir, -5, 5, 0.1, -20, 5, 9)

if __name__ == "__main__":
    run_transfer_series(device,"test_[INFO].csv","")
