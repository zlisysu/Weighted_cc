Please ensure that your input file contains at least three columns: two for mutation ligands and their pair-wise energy.

If you want obtain more rigorous cycle closure error, please list std calculated by BAR as the 4th column in your input file. 

Example:



1. Example with only three data columns: ligand1, ligand2 and pair-wise energy(Shown as Example/example_without_w)

Usage:
python wcc_main.py -f Example/example_without_w -r 1d -e -9.52

output: 
Node    dG_cc     cc_ref_error no_ref_error
 1d    -9.5200       0.0000       0.7335   
 6e    -9.7275       0.8600       0.7335   
  .	      .		     	.			 .
  .       .             .            .    
  .       .             .            . 
 6b    -10.6310      1.2100       0.7335   

2. Example with five data columns: ligand1, ligand2, pair-wise energy, bar_std, slide_std(Shown as Example/example_with_w)

Usage:
python wcc_main.py -f Example/example_with_w -r 1d -e -9.52

output: 
Node    dG_cc       dG_wcc1      dG_wcc2    cc_ref_error no_ref_error
 1d    -9.5200      -9.5200      -9.5200       0.0000       0.7335   
 6e    -9.7275      -10.6095     -9.5864       0.8600       0.7335   
  .	      .		     	.			 .			  .			   .
  .       .             .            .    		  .			   .
  .       .             .            . 			  .            .
 6b    -10.6310     -11.2172     -10.4665      1.2100       0.7335   

 


If you want obtain pair-wise results after calculation, add "-p yes" in instruction.