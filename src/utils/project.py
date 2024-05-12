# Watchface Projects
# tostr 2024

# XiaomiProject uses the official Xiaomi watchface format.
# FprjProject uses m0tral's XML format for use with m0tral's compiler.
# GMFProject uses GiveMeFive's JSON based format for use with GMF's compiler

# The project classes are abstractions to assist with modularity and ease of use.

# Note that getWidget function must return a dict
# Avoid manually changing values in the project's data, always use functions

# Processes like compilation are handled by Qt's QProcess class because it is discreet and robust. 
# If you are planning to port the code over to your own project, make sure you either:
# - install PyQt/PySide libraries if you are fine with the extra bloat
# - port to Python's subprocess

import os
import traceback
import logging
import json
import xmltodict
import xml
import xml.dom.minidom as minidom

from pathlib import Path
from pprint import pprint
from copy import deepcopy
from PyQt6.QtCore import QProcess

supportedOneFileVersion = "1.0"
logging.basicConfig(level=logging.DEBUG)

class WatchData:
    def __init__(self):
        super().__init__()
    
        self.models = []
        self.modelID = {}
        self.modelSize = {}
        self.modelSourceList = {}
        self.modelSourceData = {}
        self.shapeId = {
            "27":"AnalogDisplay",
            "30":"Image",
            "31":"ImageList",
            "32":"DigitalNumber"
        }
        dataPath = os.path.join(os.getcwd(), "data", "DeviceInfo.db")

        with open(dataPath, "r") as file:
            deviceInfo = xmltodict.parse(file.read())
            for x in deviceInfo["DeviceList"]["DeviceInfo"]:
                self.models.append(x["@Name"])
                self.modelID[x["@Name"]] = x["@Type"]
                self.modelSize[x["@Type"]] = [int(x["@Width"]), int(x["@Height"]), int(x["@Radius"])]
                self.modelSourceData[x["@Type"]] = x["SourceDataList"]["SRC"]
                self.modelSourceList[x["@Type"]] = []
                for y in x["SourceDataList"]["SRC"]:
                    self.modelSourceList[x["@Type"]].append(y["@Name"])

    def getWatchModel(self, id):
        return self.watchID[id]
    
class ProjectTools:
    def __init__(self):
        pass

class FprjProject:  
    def __init__(self):
        self.data = None
        self.widgets = None

        self.name = None
        self.directory = None
        self.dataPath = None
        self.imageDirectory = None

        self.deviceIds = {
            "0": "xiaomi_color",
            "1": "xiaomi_color_sport",
            "3": "xiaomi_color_2/s1/s2",
            "4": "xiaomi_watch_s1_pro",
            "5": "redmi/poco_watch",
            "6": "xiaomi_band_7_pro",
            "7": "redmi_watch_3",
            "8": "redmi_band_pro",
            "9": "xiaomi_band_8",
            "10": "redmi_watch_2_lite",
            "11": "xiaomi_band_8_pro",
            "12": "redmi_watch_3_active",
            "12": "redmi_watch_3_active",
            "362": "xiaomi_watch_s3",
            "365": "redmi_watch_4",
            "366": "xiaomi_band_9",
        }

        self.widgetIds = {
            "27": "widget_analog",
            "29": "widget_arc",
            "30": "widget",
            "31": "widget_imagelist",
            "32": "widget_num",
            "42": "widget_arc" # progress arc plus, prefer using this
        }

        self.propertyIds = {
            "@Alignment": "num_alignment",
            "@Alpha": "widget_alpha",
            "@Background_ImageName": "analog_background",
            "@BgImage_rotate_xc": "analog_bg_anchor_x",
            "@BgImage_rotate_yc": "analog_bg_anchor_y",
            "@Bitmap": "widget_image",
            "@BitmapList": "widget_imagelist",
            "@Blanking": "num_hide_zeros",
            "@DefaultIndex": "imagelist_default_index",
            "@Digits": "num_digits",
            "@EndAngle": "arc_end_angle",
            "@Foreground_ImageName": "arc_image",
            "@Height": "widget_height",
            "@HourHand_ImageName": "analog_hour_image",
            "@HourImage_rotate_xc": "analog_hour_anchor_x",
            "@HourImage_rotate_yc": "analog_hour_anchor_y",
            "@HourhandCorrection_En": "analog_hour_smooth_motion",
            "@Index_Src": "imagelist_source",
            "@Line_Width": "arc_thickness",
            "@MinuteHand_Image": "analog_minute_image",
            "@MinuteImage_rotate_xc": "analog_minute_anchor_x",
            "@MinuteImage_rotate_yc": "analog_minute_anchor_y",
            "@MinutehandCorrection_En": "analog_minute_smooth_motion",
            "@Name": "widget_name",
            "@Radius": "arc_radius",
            "@Range_Max": "arc_max_value",
            "@Range_Max_Src": "arc_max_value_source",
            "@Range_Min": "arc_min_value",
            "@Range_MinStep": "arc_min_step_value",
            "@Range_Step": "arc_step_value",
            "@Range_Val_Src": "arc_source",
            "@Rotate_xc": "arc_pos_x",
            "@Rotate_yc": "arc_pos_y",
            "@SecondHand_Image": "analog_second_image",
            "@SecondImage_rotate_xc": "analog_second_anchor_x",
            "@SecondImage_rotate_yc": "analog_second_anchor_y",
            "@Shape": "widget_type",
            "@Spacing": "num_spacing",
            "@StartAngle": "arc_start_angle",
            "@Value_Src": "num_source",
            "@Visible_Src": "widget_visiblity_source",
            "@Width": "widget_size_width",
            "@X": "widget_pos_x",
            "@Y": "widget_pos_y",
            "WidgetType": "WidgetType"
        }

        self.watchFileBlank = {
            "FaceProject": {
                "@DeviceType": "",
                "Screen": {
                    "@Title": "",
                    "@Bitmap": "",
                    "Widget": ""
                }
            }
        }

    def fromBlank(self, path, device, name):
        try:
            template = self.watchFileBlank
            template["FaceProject"]["@DeviceType"] = str(device)
            folder = os.path.join(path, name)
            os.makedirs(os.path.join(folder, "images"))
            os.makedirs(os.path.join(folder, "output"))
            with open(os.path.join(folder, f"{name}.fprj"), "x", encoding="utf8") as fprj:
                rawXml = xmltodict.unparse(template)
                dom = minidom.parseString(rawXml)
                prettyXml = dom.toprettyxml()
                fprj.write(prettyXml)

            self.data = template
            self.widgets = template["FaceProject"]["Screen"].get("Widget")

            self.name = os.path.basename(path)
            self.directory = os.path.dirname(path)
            self.dataPath = os.path.join(folder, f"{name}.fprj")
            self.imageDirectory = os.path.join(folder, "images")

            return True, os.path.join(folder, f"{name}.fprj")
        except Exception as e:
            return False, str(e), traceback.format_exc()
        
    def fromExisting(self, path):
        projectDir = os.path.dirname(path)
        try:
            with open(path, "r", encoding="utf8") as project:
                xmlsource = project.read()
                parse = xmltodict.parse(xmlsource)
                print(parse)
                if parse.get("FaceProject"):
                    imagesDir = os.path.join(projectDir, "images")
                    if not parse["FaceProject"]["Screen"].get("Widget"):
                        parse["FaceProject"]["Screen"]["Widget"] = []
                    if type(parse["FaceProject"]["Screen"]["Widget"]) == dict:
                        parse["FaceProject"]["Screen"]["Widget"] = [parse["FaceProject"]["Screen"]["Widget"]]

                    self.data = parse
                    self.widgets = parse["FaceProject"]["Screen"].get("Widget")
                    
                    self.name = os.path.basename(path)
                    self.directory = projectDir
                    self.dataPath = path
                    self.imageDirectory = imagesDir

                    self.convertToStandard()

                    return True, "Success"
                else:
                    return False, "Not a FaceProject!", ""
        except Exception as e:
            return False, str(e), traceback.format_exc()
        
    
        
    def getDeviceType(self):
        return self.data["FaceProject"]["@DeviceType"]
        
    def getAllWidgets(self, type=None, theme=None): # type and theme are for theme support someday over the rainbow
        return self.widgets
    
    def convertToStandard(self):
        for index, widget in enumerate(self.widgets):
            widgetCopy = widget.copy()
            for key, value in widget.items():
                print(key)
                widgetCopy[self.propertyIds[key]] = value
                del widgetCopy[key]
                if self.propertyIds[key] == "widget_type":
                    widgetCopy[self.propertyIds[key]] = self.widgetIds[value]
            self.widgets[index] = widgetCopy
        
    
    def convertToFprj(self):
         for widget in self.widgets:
             for key, value in widget.items():
                 widget[[k for k, v in self.propertyIds.items() if v == key][0]] = value # get key from value in list comprehension
                 del widget[key]

    def getWidget(self, name):
        widget = list(filter(lambda widget: widget["widget_name"] == name, self.widgets))
        if len(widget) == 0:
            return None
        else:
            return widget[0]
    
    def getProperty(self, name, property):
        widget = list(filter(lambda widget: widget["widget_name"] == name, self.widgets))
        if len(widget) == 0:
            return None
        else:
            return widget[0].get(property)
    
    def getTitle(self):
        return self.data["FaceProject"]["Screen"]["@Title"]

    def setProperty(self, name, property, value):
        widget = list(filter(lambda widget: widget["widget_name"] == name, self.widgets))
        if len(widget) == 0:
            return "Widget does not exist!"
        else:
            widget[0][property] = value

    def setWidgetPos(self, name, posX, posY):
        widget = list(filter(lambda widget: widget["widget_name"] == name, self.widgets))
        if len(widget) == 0:
            return "Widget does not exist!"
        else:
            widget[0]["@X"] = posX
            widget[0]["@Y"] = posY
        
    def setTitle(self, value):
        self.data["FaceProject"]["Screen"] = value

    def toString(self, data):
        raw = xmltodict.unparse(data)
        dom = xml.dom.minidom.parseString(raw)
        pretty_xml = dom.toprettyxml()

        return pretty_xml

    def save(self):
        self.convertToFprj()

        raw = xmltodict.unparse(self.data)
        dom = xml.dom.minidom.parseString(raw)
        pretty_xml = dom.toprettyxml()

        try:
            with open(self.dataPath, "w", encoding="utf8") as file:
                file.write(pretty_xml)
            return True, "success"
            
        except Exception as e:
            return False, e        

    def compile(self, path, location, compilerLocation):
        logging.info("Compiling project "+path)
        process = QProcess()
        process.setProgram(compilerLocation)
        process.setArguments(["compile", path, location, str.split(os.path.basename(path), ".")[0]+".face", "0"])
        process.start()
        return process
    
    def decompile(self, path, location, compilerLocation):
        logging.info("Decompiling project "+path)
        process = QProcess()
        process.setWorkingDirectory(location)
        process.setProgram(compilerLocation)
        process.setArguments(path)
        process.start()
        return process
    
class XiaomiProject:
    def __init__(self):
        # TODO
        # Get manifest.xml parsed properly and resources

        # NOTE
        # There are 2 important files
        # - description.xml located at top level
        # - manifest.xml located at /resources

        self.descriptionBlank = """
        <?xml version="1.0" encoding="utf-8"?>
        <watch>
            <name></name>
            <deviceType></deviceType>
            <version>5.0</version>
            <pkgName></pkgName>
            <size></size>
            <author></author>
            <description></description>
            <romVersion>1</romVersion>
            <imageCompression>true</imageCompression>
            <watchFaceLanguages>false</watchFaceLanguages>
            <langData></langData>
            <_recolorEnable>false</_recolorEnable>
            <recolorTable>undefined</recolorTable>
            <nameCHT></nameCHT>
            <nameEN></nameEN>
        </watch>
        """

        self.manifestBlank = """
        <?xml version="1.0" encoding="utf-8"?>
        <Watchface width="" height="" editable="false" id="" _recolorEnable="" recolorTable="" compressMethod="" name="">
            <Resources>
            </Resources>
            <Theme type="normal" name="default" bg="" isPhotoAlbumWatchface="false" preview="">
            </Theme>
        </Watchface>
        """
        
        self.description = None
        self.manifest = None
        
    def fromBlank(self):
        pass
        
    def fromExisting(self, folder):
        def joinPath(path, file):
            # on the rare off chance that windows does not like forward slashes, just replace all forward slashes
            # with backslashes
            return path+"/"+file

        logging.info("Opening "+folder)

        # Get file locations

        # folders
        self.previewFolder = joinPath(folder, "preview")
        self.resourceFolder = joinPath(folder, "resources")

        logging.info("Parsing description.xml & manifest.xml")

        # xml source files
        with open(joinPath(folder, "description.xml"), "r", encoding="utf8") as descFile:
            self.description = xmltodict.parse(descFile.read())

        with open(joinPath(self.resourceFolder, "manifest.xml"), "r", encoding="utf8") as manifestFile:
            self.manifest = xmltodict.parse(manifestFile.read())["Watchface"]

    def getResource(self, name):
        return 
        
    def getAllWidgets(self, type, theme):
        pprint(self.manifest)
        return self.manifest["Theme"]

    def getWidget(self, theme, name):
        widgets = self.manifest["Theme"]["Layout"]
        return [ widgets for widget in widgets if widget.get(name) == theme ]

    def save(self, folder):
        pass

class GMFProject:
    def __init__(self):
        pass