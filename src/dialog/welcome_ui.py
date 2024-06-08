# Form implementation generated from reading ui file 'c:\Users\Justin\Mi-Create\src\dialog\welcome.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 500)
        Dialog.setMinimumSize(QtCore.QSize(750, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/MiCreate48x48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideBar = QtWidgets.QFrame(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy)
        self.SideBar.setMinimumSize(QtCore.QSize(200, 0))
        self.SideBar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.SideBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.SideBar.setObjectName("SideBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SideBar)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ApplicationLogo = QtWidgets.QLabel(parent=self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ApplicationLogo.sizePolicy().hasHeightForWidth())
        self.ApplicationLogo.setSizePolicy(sizePolicy)
        self.ApplicationLogo.setText("")
        self.ApplicationLogo.setPixmap(QtGui.QPixmap(":/Images/MiCreate48x48.png"))
        self.ApplicationLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ApplicationLogo.setObjectName("ApplicationLogo")
        self.verticalLayout.addWidget(self.ApplicationLogo)
        self.ApplicationName = QtWidgets.QLabel(parent=self.SideBar)
        self.ApplicationName.setStyleSheet("QLabel { font-size: 14pt;}")
        self.ApplicationName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ApplicationName.setObjectName("ApplicationName")
        self.verticalLayout.addWidget(self.ApplicationName)
        self.ApplicationVersion = QtWidgets.QLabel(parent=self.SideBar)
        self.ApplicationVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ApplicationVersion.setObjectName("ApplicationVersion")
        self.verticalLayout.addWidget(self.ApplicationVersion)
        self.line = QtWidgets.QFrame(parent=self.SideBar)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.NewProject = QtWidgets.QPushButton(parent=self.SideBar)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.NewProject.setIcon(icon)
        self.NewProject.setObjectName("NewProject")
        self.verticalLayout.addWidget(self.NewProject)
        self.OpenProject = QtWidgets.QPushButton(parent=self.SideBar)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.OpenProject.setIcon(icon)
        self.OpenProject.setObjectName("OpenProject")
        self.verticalLayout.addWidget(self.OpenProject)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.settings = QtWidgets.QToolButton(parent=self.SideBar)
        icon = QtGui.QIcon.fromTheme("preferences-desktop")
        self.settings.setIcon(icon)
        self.settings.setIconSize(QtCore.QSize(16, 16))
        self.settings.setObjectName("settings")
        self.verticalLayout.addWidget(self.settings)
        self.horizontalLayout.addWidget(self.SideBar)
        self.ContentPanel = QtWidgets.QFrame(parent=Dialog)
        self.ContentPanel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.ContentPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ContentPanel.setObjectName("ContentPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContentPanel)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ProjectList = QtWidgets.QListWidget(parent=self.ContentPanel)
        self.ProjectList.setStyleSheet("background-color: transparent")
        self.ProjectList.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.ProjectList.setObjectName("ProjectList")
        self.verticalLayout_2.addWidget(self.ProjectList)
        self.horizontalLayout.addWidget(self.ContentPanel)
        self.ContentPanel.raise_()
        self.SideBar.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Welcome"))
        self.ApplicationName.setText(_translate("Dialog", "Mi Create"))
        self.ApplicationVersion.setText(_translate("Dialog", "Version"))
        self.NewProject.setText(_translate("Dialog", "New Project"))
        self.OpenProject.setText(_translate("Dialog", "Open Project"))
        self.settings.setText(_translate("Dialog", "Settings"))
