from optparse import OptionParser
from Graphs import Graph
import  CalLig as lig


#if weights contained bennett_std, pleas display bennett_std before other weights
class optParser():
    def __init__(self, fakeArgs):
        parser = OptionParser()
        parser.add_option('-f', '--file', dest='file', help='Input file containing pairwise energy data', default='thrombin.txt')
        parser.add_option('-r', '--ref', dest='ref',help='Reference molecule for calculating the energy for other molecules. Default: The first molecule in the data file',
                          default='')
        parser.add_option('-e', '--ref_ene', dest='ref_ene', help='Energy for the reference molecule. Default: 0.00',
                          default=0.00, type=float)
        parser.add_option('-w', '--weight', dest='weight', help='Weight option: no(original cycle closure), bar(if weights contained bennett_std). Default: 0',
                          default="no")
        if fakeArgs:
            self.option, self.args = parser.parse_args(fakeArgs)
        else:
            self.option, self.args = parser.parse_args()

if __name__ == '__main__':
    opts = optParser('')
    #fakeArgs = "-f bace_run1_0_with_w -r 3A -e -8.83 -w bar"  # only keep this for test purpose
    #opts = optParser(fakeArgs.strip().split())  # only keep this for test purpose
    g = Graph(opts.option.file, opts.option.weight)
    g.getAllCyles()
    if len(g.cycles)== 0:
        print("No cycle in this graph.")
        exit()
    g.iterateCycleClosure(minimum_cycles=2)
    g.printEnePairs()
    node_map=lig.set_node_map(g)
    ref_node = g.V.index(opts.option.ref)
    no_ref_error = lig.cal_node_noref_error(g.V, node_map)
    ref_node_err, path = lig.cal_node_ref_error(ref_node, g.V, node_map)
    mol_ene = lig.calcMolEnes(opts.option.ref_ene, g, path)
    lig.printMol(g.V,mol_ene,ref_node_err,no_ref_error)


