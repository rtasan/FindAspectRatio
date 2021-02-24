import os
import sys
import wx
from MyProject1MainChild import MyProject1MainChild



if __name__ == '__main__':
	app = wx.App(False)
	frame = MyProject1MainChild(None)
	frame.Show(True)
	app.MainLoop()