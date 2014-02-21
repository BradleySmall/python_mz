"""
	Author: Bradley M. Small
	All work is my own, and copyright (c) 2014 is retained. 
	This code is provided as a testing exercise solely for evaluating me for employment. 

"""
import bisect
class Range:
	"""
	Class for managing tracked ranges
	It contains a list to hold tuples which represent ranges
	It allows:
		adding new tracked ranges
		deleting existing tracked ranges
		querying the existance of a tracked range

	Ranges are all-in or all-out. There is no special case for handling overlapping ranges
	or even fully encompassed ranges. 1,10 though it encompases 2,9 will not query true for 
	it.	This design will have the most efficiency by being able to compare tuples using the 
	list's comparisons. 
	
	However, if that were the intent changes would have to be made to test the tuple 
	to see if it encloses the range. Handling the encompassed list could use a class 
	rather than a tuple, and that class would have comparison operator. Rules would still 
	have to be clarified for partially encompassed ranges vs fully encompassed ranges. 
	Such as 1,5 and 6,10 exist and you want to track 3,9 as opposed to 2,4. 

	These use-cases may require something along the lines of PartiallyIncludedRange or 
	FullyIncludedRange. 
	"""

	def __init__ (self):
		"""
		construction will simply create an empty member list
		"""
		self.TrackedRanges = []
		self.isSorted = True

	def __del__ (self):
		"""
		destruction will simply delete that list
		"""
		del self.TrackedRanges[:]
	
##	# helper to handle contained ranges if later desired
##	def _Contains(self, rangeStart, rangeStop, start, stop):
##		if rangeStart <=start && rangeStop >= stop:
##			return True
##		else:
##			return False

	def AddRange(self, start, stop):
		"""
		If a range already exists return false for failure
		When it doesn't already exist then add it and return true
		
		Depending on use-case false may be a warning ignored rather than a fatal error
		that is left to the consumer
		"""

##     	# this is how it could be changed to handle contained ranges
##		for (RangeStart, RangeStop) in self.TrackedRanges:
##			if self._Contains(RangeStart, RangeStop, start, stop):
##				return False #already there short circuit
##
##		self.TrackedRanges.append( (start,stop) )
##		return True

		# Start tracking the given range
		try:
			if (start, stop) not in self.TrackedRanges:
				self.TrackedRanges.append( (start,stop) )
				self.isSorted = False
				return True
			else:
				return False
		except MemoryError:
			# in this case I would think it most appropriate to simply
			# raise the memory error because the user would have a 
			# difficult time differentiating between not adding because
			# it is already there, and not adding because the system was
			# out of memory. However, this allows for expansion with 
			# a known possible error condition and can be expanded as
			# necessary.
			return False

	def DeleteRange(self, start, stop):
		"""
		If a range doesn't exist return false for failure
		When it does already exist then remove it and return true
		
		Depending on use-case false may be a warning ignored rather than a fatal error
		that is left to the consumer
		"""
##     	# this is how it could be changed to handle contained ranges
##		Deletions would either have to be maintained as they are since 
##		removing partial ranges would have to result in additional ranges
## 		being added. For example 1,10 exists. Removing 3,5 would require
## 		adding 1,2 and 6,10. Though programatically do-able it appears to
##		the author that such would involve business logic outside the definition
##		of this design specification.

		if self.isSorted == False:
			self.TrackedRanges.sort()
			self.isSorted = True

		position = bisect.bisect_left(self.TrackedRanges, (start, stop))
		if len(self.TrackedRanges) == position:
			return False
		else:
			if self.TrackedRanges[position] == (start, stop):
				self.TrackedRanges.remove( (start,stop) )
				return True
			else:
				return False

		# Stop tracking the given range 
#		if (start, stop) in self.TrackedRanges:
#			self.TrackedRanges.remove( (start,stop) )
		# the next 3 lines could be removed or replaced with a pass
		# to effect a noop for removing non-existing ranges
		# hoever, their existance makes the unit_tests more 
		# reasonable, and one gains the flexibility of merely 
		# ignoring the return value 
#			return True
#		else:
#			return False
 	
	def QueryRange(self, start, stop):
		"""
		If a range doesn't exist return false for failure
		When it does exist then return true
		"""
		if self.isSorted == False:
			self.TrackedRanges.sort()
			self.isSorted = True

		position = bisect.bisect_left(self.TrackedRanges, (start, stop))
		if len(self.TrackedRanges) == position:
			return False
		else:
			if self.TrackedRanges[position] == (start, stop):
				return True
			else:
				return False

##     	# this is how it could be changed to handle contained ranges
##		for (RangeStart, RangeStop) in self.TrackedRanges:
##			if self._Contains(RangeStart, RangeStop, start, stop):
##				return True
##		
##		return False

 		# Check whether the entire given range is being tracked
#		if (start, stop) in self.TrackedRanges:
#			return True
#		else:
#			return False

##def main ():
##	"""
##	"""
##	myRange = Range()
##
##	myRange.AddRange(1,10)
##	if myRange.QueryRange(1,10):
##		print "Yest it is"
##	else:
##		print "No it isn't"
##
### Notice Ignored return value = noop
##	myRange.DeleteRange(1,10)
##
##	if myRange.QueryRange(1,10):
##		print "Yest it is"
##	else:
##		print "No it isn't"
##
##
##	return 0
##
##
##if 0 == main():
##	print 'Success'
##else:
##	print 'Fail'
##
