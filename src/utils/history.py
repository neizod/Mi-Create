# History System
# ooflet <ooflet@proton.me>

# Uses Qt's Command-based history system

import logging
from typing import Any
from PyQt6.QtGui import QUndoCommand, QUndoStack

class History:
    def __init__(self):
        self.undoStack = QUndoStack()

class CommandAddWidget(QUndoCommand):
    def __init__(self, widget, commandFunc, posX, posY, properties, description):
        super(CommandAddWidget, self).__init__(description)
        self.widget = widget
        self.commandFunc = commandFunc
        self.posX = posX
        self.posY = posY
        self.properties = properties

    def redo(self):
        self.commandFunc("redo", self.widget, self.posX, self.posY, self.properties)

    def undo(self):
        self.commandFunc("undo", self.widget, self.posX, self.posY, self.properties)

class CommandDeleteWidget(QUndoCommand):
    def __init__(self, widget, commandFunc, description):
        super(CommandDeleteWidget, self).__init__(description)
        self.widget = widget
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc("redo", self.widget)

    def undo(self):
        self.commandFunc("undo", self.widget)

class CommandPasteWidget(QUndoCommand):
    def __init__(self, clipboard, commandFunc, description):
        super(CommandPasteWidget, self).__init__(description)
        self.clipboard = clipboard
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc("redo", self.clipboard)

    def undo(self):
        self.commandFunc("undo", self.clipboard)

class CommandModifyWidgetLayer(QUndoCommand):
    def __init__(self, widgetList, changeType, commandFunc, description):
        super(CommandModifyWidgetLayer, self).__init__(description)
        self.widgetList = widgetList
        self.changeType = changeType
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc("redo", self.changeType, self.widgetList)

    def undo(self):
        self.commandFunc("undo", self.changeType, self.widgetList)

class CommandModifyProjectData(QUndoCommand):
    def __init__(self, prevData, newData, commandFunc, description):
        logging.debug(f"prevdata {prevData}, newdata {newData}")
        super(CommandModifyProjectData, self).__init__(description)
        self.prevData = prevData
        self.newData = newData
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc(self.newData)

    def undo(self):
        self.commandFunc(self.prevData)

class CommandModifyProperty(QUndoCommand):
    def __init__(self, name, property, previousValue, currentValue, commandFunc, description):
        super(CommandModifyProperty, self).__init__(description)
        self.name = name
        self.property = property
        self.previousValue = previousValue
        self.currentValue = currentValue
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc(self.name, self.property, self.currentValue)

    def undo(self):
        if self.property == "widget_name":
            self.commandFunc(self.currentValue, self.property, self.previousValue)
        else:
            self.commandFunc(self.name, self.property, self.previousValue)

class CommandModifyPosition(QUndoCommand):
    def __init__(self, previousPosition, currentPosition, commandFunc, description):
        super(CommandModifyPosition, self).__init__(description)
        self.prevPos = previousPosition
        self.currentPos = currentPosition
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc(self.currentPos)

    def undo(self):
        self.commandFunc(self.prevPos)

class CommandModifyAlignment(QUndoCommand):
    def __init__(self, prevPosList, alignment, nameList, commandFunc, description):
        super(CommandModifyAlignment, self).__init__(description)
        self.prevPosList = prevPosList
        self.alignment = alignment
        self.nameList = nameList
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc("redo", self.alignment, self.nameList)

    def undo(self):
        self.commandFunc("undo", self.prevPosList, self.nameList)

class CommandChangeTheme(QUndoCommand):
    def __init__(self, previousTheme, currentTheme, commandFunc, description):
        super(CommandChangeTheme, self).__init__(description)
        self.previousTheme = previousTheme
        self.currentTheme = currentTheme
        self.commandFunc = commandFunc

    def redo(self):
        self.commandFunc(self.currentTheme)

    def undo(self):
        self.commandFunc(self.previousTheme)
