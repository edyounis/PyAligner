class Scorer():
	"""Scorer Class"""

	def __init__ ( self, match, mismatch, gap, xdrop, affine = None ):

		if not isinstance( match, int ):
			raise TypeError( "Invalid Match Score Type" )

		if not isinstance( mismatch, int ):
			raise TypeError( "Invalid Mismatch Score Type" )

		if not isinstance( gap, int ):
			raise TypeError( "Invalid Gap Score Type" )

		if not isinstance( xdrop, int ):
			raise TypeError( "Invalid X-Drop Value Type" )

		if affine is not None and not isinstance( affine, int ):
			raise TypeError( "Invalid Affine Gap Score Type" )

		self.match    = match
		self.mismatch = mismatch
		self.gap      = gap
		self.xdrop    = xdrop
		self.affine   = affine

	def calc_sq_value ( self, left_score, above_score, diag_score,
					    nuch, nucv, max_score ):

		potential_values = []

		if diag_score != "X":
			if nuch == nucv:
				potential_values.append( diag_score + self.match )
			else:
				potential_values.append( diag_score + self.mismatch )

		if left_score != "X":
			potential_values.append( left_score + self.gap )

		if above_score != "X":
			potential_values.append( above_score + self.gap )

		if len( potential_values ) == 0:
			return "X"

		res = max( potential_values )

		if res <= max_score - self.xdrop:
			res = "X"

		return res