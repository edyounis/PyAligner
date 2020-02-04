# Todo:
# Make a proper python package
# Add __str__ __repr__ funcs to objects
# Add Documentation + Proper comments

import os
import argparse
from seq import Sequence
from score import Scorer
from matrix import DPMatrix

# def smith_waterman ( seq1, seq2, scorer ):
# 	h_dim = len( seq1 )
# 	v_dim = len( seq2 )

#     dp_matrix = DPMatrix( seq1, seq2 )

# 	dp_matrix = [ [ 0 for v in range( v_dim ) ] for h in range( h_dim ) ]

# 	def print_dp_matrix( dp_matrix ):
# 		for r in dp_matrix:
# 			print( r )

# 	for h in range( 1, h_dim ):
# 		dp_matrix[h][0] = -h

# 	for v in range( 1, v_dim ):
# 		dp_matrix[0][v] = -v

# 	max_value = -1000000

# 	for r, h in enumerate( seq1 ):
# 	    for c, v in enumerate( seq2 ):
# 	        r_p = r + 1
# 	        c_p = c + 1
# 	        onef  = dp_matrix[r_p-1][c_p-1]
# 	        onef += scorer.match if h == v else scorer.mismatch

# 	        twof = max( dp_matrix[r_p-1][c_p], dp_matrix[r_p][c_p-1] ) + scorer.gap

# 	        dp_matrix[r_p][c_p] = max( twof, onef )
# 	        if ( dp_matrix[r_p][c_p] > max_value ):
# 	            max_value = dp_matrix[r_p][c_p]

# 	print_dp_matrix( dp_matrix )
# 	print( max_value )

if __name__ == "__main__":
	description = "Smith-Waterman Algorithm with X-Drop"
	parser = argparse.ArgumentParser( description = description )

	parser.add_argument( "input1", type = argparse.FileType(),
						 help = "Sequence File 1" )

	parser.add_argument( "input2", type = argparse.FileType(),
						 help = "Sequence File 2" )

	parser.add_argument( "-x", "--xdrop", type = int, default = 7,
						 help = "X-Drop Value" )

	parser.add_argument( "-m", "--match_score", type = int, default = 1,
						 help = "Match Score" )

	parser.add_argument( "-i", "--mismatch_score", type = int, default = -1,
						 help = "Mismatch Score" )

	parser.add_argument( "-g", "--gap_score", type = int, default = -1,
						 help = "Gap Score" )

	parser.add_argument( "-a", "--affine_score", type = int, default = None,
						 help = "Affine Gap Score" )

	args = parser.parse_args()

	seq1 = Sequence( args.input1.read() )
	seq2 = Sequence( args.input2.read() )

	scorer = Scorer( args.match_score, args.mismatch_score,
					 args.gap_score, args.xdrop, args.affine_score )

	dp_matrix = DPMatrix( seq1, seq2, scorer )
	print( dp_matrix )


