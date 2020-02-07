class Sequence():
	"""Nucleotide Sequence Class"""

	def __init__ ( self, seq_string ):
		if not isinstance( seq_string, str ):
			raise TypeError( "Invalid Sequence String Type" )

		seq_string = self.sanitize_seq_string( seq_string )

		if not self.is_valid_seq_string( seq_string ):
			raise ValueError( "Invalid Sequence String" )

		self.seq_string = seq_string

	def sanitize_seq_string ( self, seq_string ):
		while seq_string[-1] == '\n':
			seq_string = seq_string[:-1]

		while seq_string[-1] == '\r':
			seq_string = seq_string[:-1]

		return seq_string.upper()

	def is_valid_seq_string ( self, seq_string ):
		return all( [ self.is_valid_nucleotide( c ) for c in seq_string ] )

	def is_valid_nucleotide ( self, char ):
		return char == "A" or char == "C" or char == "T" or char == "G"

	def __iter__ ( self ):
		return self.seq_string.__iter__()

	def __len__ ( self ):
		return len( self.seq_string )

	def __setitem__ ( self, key, item ):
		self.seq_string[ key ] = item

	def __getitem__ ( self, key ):
		return self.seq_string[ key ]


