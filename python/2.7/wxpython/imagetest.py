#!/usr/local/bin/python2.7

# Code from http://wiki.wxpython.org/AnotherTutorial

import wx

class Colours(wx.Dialog):
  def __init__(self, parent, id, title):

    wx.Dialog.__init__(self, parent, id, title, size=(300, 300))
    vbox = wx.BoxSizer(wx.VERTICAL)
    self.pnl1 = wx.Panel(self, -1)
    self.pnl2 = wx.Panel(self, -1)
    self.pnl3 = wx.Panel(self, -1)
    self.pnl4 = wx.Panel(self, -1)
    self.pnl5 = wx.Panel(self, -1)
    self.pnl6 = wx.Panel(self, -1)
    self.pnl7 = wx.Panel(self, -1)
    self.pnl8 = wx.Panel(self, -1)

    gs = wx.GridSizer(4,2,3,3)
    gs.AddMany([ (self.pnl1, 0 ,wx.EXPAND),
                 (self.pnl2, 0, wx.EXPAND),
                 (self.pnl3, 0, wx.EXPAND),
                 (self.pnl4, 0, wx.EXPAND),
                 (self.pnl5, 0, wx.EXPAND),
                 (self.pnl6, 0, wx.EXPAND),
                 (self.pnl7, 0, wx.EXPAND),
                 (self.pnl8, 0, wx.EXPAND) ])

    vbox.Add(gs, 1, wx.EXPAND | wx.TOP, 5)
    self.SetSizer(vbox)
    self.SetColors()
    self.Centre()
    self.ShowModal()
    self.Destroy()

  def SetColors(self):
    self.pnl1.SetBackgroundColour(wx.BLACK)
    self.pnl2.SetBackgroundColour(wx.Colour(139,105,20))
    self.pnl3.SetBackgroundColour(wx.RED)
    self.pnl4.SetBackgroundColour('#0000FF')
    self.pnl5.SetBackgroundColour('sea green')
    self.pnl6.SetBackgroundColour('midnight blue')
    self.pnl7.SetBackgroundColour(wx.LIGHT_GREY)
    self.pnl8.SetBackgroundColour('plum')

print "The container is working properly if a window shows eight color blocks."

app = wx.App(0)
Colours(None, -1, 'Colours')
app.MainLoop()
