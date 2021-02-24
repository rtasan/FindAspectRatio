# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aspect&BB Finder", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		MainSizer = wx.BoxSizer( wx.VERTICAL )

		self.Tabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AspectFinder = wx.Panel( self.Tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		AspSizer = wx.BoxSizer( wx.VERTICAL )

		self.AspMsg1 = wx.StaticText( self.AspectFinder, wx.ID_ANY, u"クリップボードに画像をコピーしてから実行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AspMsg1.Wrap( -1 )

		AspSizer.Add( self.AspMsg1, 0, wx.ALL, 5 )

		self.AspBtn1 = wx.Button( self.AspectFinder, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
		AspSizer.Add( self.AspBtn1, 0, wx.ALL, 5 )

		self.AspMsg2 = wx.StaticText( self.AspectFinder, wx.ID_ANY, u"アスペクト比  - : -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AspMsg2.Wrap( -1 )

		AspSizer.Add( self.AspMsg2, 0, wx.ALL, 5 )


		self.AspectFinder.SetSizer( AspSizer )
		self.AspectFinder.Layout()
		AspSizer.Fit( self.AspectFinder )
		self.Tabs.AddPage( self.AspectFinder, u"AspectFinder", False )
		self.BlackBar = wx.Panel( self.Tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		BBsizer = wx.BoxSizer( wx.VERTICAL )

		self.BBMsg1 = wx.StaticText( self.BlackBar, wx.ID_ANY, u"クリップボードに画像をコピーしてから実行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BBMsg1.Wrap( -1 )

		BBsizer.Add( self.BBMsg1, 0, wx.ALL, 5 )

		self.BBBtn1 = wx.Button( self.BlackBar, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
		BBsizer.Add( self.BBBtn1, 0, wx.ALL, 5 )

		self.BBMsg2 = wx.StaticText( self.BlackBar, wx.ID_ANY, u"黒帯: --%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BBMsg2.Wrap( -1 )

		BBsizer.Add( self.BBMsg2, 0, wx.ALL, 5 )


		self.BlackBar.SetSizer( BBsizer )
		self.BlackBar.Layout()
		BBsizer.Fit( self.BlackBar )
		self.Tabs.AddPage( self.BlackBar, u"BlackBarFinder", True )

		MainSizer.Add( self.Tabs, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.AspBtn1.Bind( wx.EVT_BUTTON, self.AspBtn1OnButtonClick )
		self.BBBtn1.Bind( wx.EVT_BUTTON, self.BBBtn1OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def AspBtn1OnButtonClick( self, event ):
		event.Skip()

	def BBBtn1OnButtonClick( self, event ):
		event.Skip()


