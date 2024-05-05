# encoding: utf-8

###########################################################################################################
#
#
# General Plugin
#
# Read the docs:
# https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################


import objc
from GlyphsApp import GSCallbackHandler, FILTER_FLAT_KERNING
from GlyphsApp.plugins import GeneralPlugin


class MKKernFlattener(GeneralPlugin):

	@objc.python_method
	def settings(self):
		GSCallbackHandler.addCallback_forOperation_(self, FILTER_FLAT_KERNING)

	@objc.typedSelector(b'@@:@@o^@')
	def filterFlatKerning_font_error_(self, flatKerning, font, error):
		from KernFlattener import filterKernPairs
		try:
			return filterKernPairs(flatKerning, font), None
		except:
			import traceback
			print(traceback.format_exc())
		return None, None

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
