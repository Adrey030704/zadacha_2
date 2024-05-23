from dataLoader import DataLoader
from RCS import RCS
from resultWriter import ResultWriter
from plotter import Plotter
import numpy as np

def main():
    url = "https://jenyay.net/uploads/Student/Modelling/task_rcs_02.txt"
    filename = "task_rcs_02.txt"
    variant_number = 1
    
    loader = DataLoader(url, filename)
    loader.download_file()
    D, fmin, fmax = loader.parse_txt(variant_number)

    frequencies = np.linspace(fmin, fmax, num=500)
    rcs_calculator = RCS(D / 2)
    results = []
    for freq in frequencies:
        rcs = rcs_calculator.calculate_rcs(freq)
        results.append({"freq": freq, "lambda": 3e8 / freq, "rcs": rcs})

    writer = ResultWriter("rcs_results.xml")
    writer.write_to_xml(results)

    plotter = Plotter()
    plotter.plot_rcs_vs_frequency(results)

if __name__ == "__main__":
    main()
