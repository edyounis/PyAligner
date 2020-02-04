class Scorer():
	"""Scorer Class"""

	def __init__ ( self, match, mismatch, gap, affine = None ):

		if not isinstance( match, int ):
			raise TypeError( "Invalid Match Score Type" )

		if not isinstance( mismatch, int ):
			raise TypeError( "Invalid Mismatch Score Type" )

		if not isinstance( gap, int ):
			raise TypeError( "Invalid Gap Score Type" )

		if affine is not None and not isinstance( affine, int ):
			raise TypeError( "Invalid Affine Gap Score Type" )

		self.match    = match
		self.mismatch = mismatch
		self.gap      = gap
		self.affine   = affine

	def calc_square_value ( self, left_score, above_score, diag_score,
							nuch, nucv ):

		potential_values = []

		if nuch == nucv:
			potential_values.append( diag_score + self.match )
		else:
			potential_values.append( diag_score + self.mismatch )

		potential_values.append( left_score + self.gap )
		potential_values.append( above_score + self.gap )

		return max( potential_values )