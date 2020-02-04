from seq import Sequence
from score import Scorer

class DPMatrix():
    """Dynamic Programming Matrix Class"""

    def __init__ ( self, seqh, seqv, scorer ):

        if not isinstance( seqh, Sequence ):
            raise TypeError( "Invalid Horizontal Sequence Type" )

        if not isinstance( seqv, Sequence ):
            raise TypeError( "Invalid Vertical Sequence Type" )

        if not isinstance( scorer, Scorer ):
            raise TypeError( "Invalid Scorer Type" )

        self.seqh   = seqh
        self.seqv   = seqv
        self.scorer = scorer

        self.dimh = len( seqh ) + 1
        self.dimv = len( seqv ) + 1

        self.dp_matrix = [ [ -9999 for h in range( self.dimh ) ]
                           for v in range( self.dimv ) ]

        self.run_sw()

    def run_sw ( self ):

        # Fill Off-Grid Squares
        for h in range( self.dimh ):
            self.dp_matrix[0][h] = -h

        for v in range( self.dimv ):
            self.dp_matrix[v][0] = -v

        # Fill On-Grid Squares
        for r, v in enumerate( self.seqv ):
            for c, h in enumerate( self.seqh ):
                r_p = r + 1
                c_p = c + 1
                self.dp_matrix[r_p][c_p] = self.scorer.calc_square_value( self.dp_matrix[r_p][c_p-1], self.dp_matrix[r_p-1][c_p], self.dp_matrix[r_p-1][c_p-1], h, v  )

    def __str__ ( self ):
        str_builder = ""

        if len( self.dp_matrix ) <= 1:
            return str_builder

        # Print horizontal sequence on the top of the grid
        str_builder += "   "
        for n in self.seqh:
            str_builder += format( n, ">2s" ) + " "
        str_builder += "\n"

        # Print the rows starting with the appropriate
        # character of the vertical sequence
        for i, r in enumerate( self.dp_matrix[1:] ):
            str_builder += format( self.seqv[i], ">2s" ) + " "
            for v in r[1:]:
                str_builder += format(str(v),">2s") + " "
            str_builder += '\n'

        # Remove last '\n' and return
        return str_builder[:-1]

