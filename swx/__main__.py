# Todo:
# Make a proper python package
# Add __str__ __repr__ funcs to objects
# Add Documentation + Proper comments
# Add Affine Gap
# Add Tests

import os
import argparse
from swx import Sequence, Scorer, DPMatrix

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
	print( dp_matrix.calc_match_seq() )
