import os
import sys
import wx
from AspBBFinderMainFrameChild import AspBBFinderMainFrameChild


if __name__ == '__main__':
	app = wx.App(False)
	frame = AspBBFinderMainFrameChild(None)
	frame.Show(True)
	app.MainLoop()