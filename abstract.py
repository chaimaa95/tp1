#!/user/bin/env python
# -*- coding utf-8 -*-

class WinGet:
  def paint(type):
    pass
class Button(WinGet):
  def paint(self):
    pass
class WinButton(Button):
  def paint(self):print("     Windows Button")
class LinuxButton(Button):
  def paint(self):print("      Linux Button")
class Button(WinGet):
  def paint(self):
    pass
class Edit(WinGet):
  def paint(self):
    pass
class WinEdit(Edit):
  def paint(self):print("     Windows Edit")
class LinuxEdit(Edit):
  def paint(self):print("      Linux Edit")
class GuiFactory:
  def createGui(type):
    pass
class WinGuiFactory(GuiFactory):
  def createGui(type):
    if type=="Button":return WinButton()
    elif type=="Edit":return WinEdit()
    else:return None
class LinuxGuiFactory(GuiFactory):
  def createGui(type):
    if type=="Button":return LinuxButton()
    elif type=="Edit":return LinuxEdit()
    else:return None
if __name__ == '__main__':
  print("++++++++++++++++++++++++++++++")
  print("        Windows:              ")
  print("++++++++++++++++++++++++++++++")
  for type in ("Button","Edit"):
    windows=WinGuiFactory.createGui(type)
    windows.paint()
  print("++++++++++++++++++++++++++++++")
  print("          Linux:             ")
  print("++++++++++++++++++++++++++++++")
  for type in ("Button","Edit"):
      linux=LinuxGuiFactory.createGui(type)
      linux.paint()