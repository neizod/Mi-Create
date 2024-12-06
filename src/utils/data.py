# WatchData class
# ooflet <ooflet@proton.me>

import os
import json

import shutil
import xmltodict

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QMessageBox

class WatchData:
    def __init__(self):
        self.models = []
        self.modelID = {}
        self.modelSize = {}
        self.modelSourceList = {}
        self.modelSourceData = {}
        self.deviceId = [
            "xiaomi_color",
            "70mai_saphir",
            "xiaomi_color_sport",
            "xiaomi_color_2/s1/s2",
            "xiaomi_watch_s1_pro",
            "redmi/poco_watch",
            "xiaomi_band_7_pro",
            "redmi_watch_3",
            "redmi_band_pro",
            "xiaomi_band_8",
            "redmi_watch_2_lite",
            "xiaomi_band_8_pro",
            "redmi_watch_3_active",
            "xiaomi_watch_s3",
            "redmi_watch_4",
            "xiaomi_band_9"
        ]
        self.widgetId = [
            "widget"
            "widget_analog"
            "widget_arc"
            "widget_container"
            "widget_imagelist"
            "widget_num"
        ]
        self.propertyId = [
            "num_alignment",
            "widget_alpha",
            "widget_background_bitmap",
            "analog_bg_anchor_x",
            "analog_bg_anchor_y",
            "widget_bitmap",
            "widget_bitmaplist",
            "num_toggle_zeros",
            "imagelist_default_index",
            "num_digits",
            "arc_end_angle",
            "arc_image",
            "widget_size_height",
            "analog_hour_image",
            "analog_hour_anchor_x",
            "analog_hour_anchor_y",
            "analog_hour_smooth_motion",
            "imagelist_source",
            "arc_thickness",
            "analog_minute_image",
            "analog_minute_anchor_x",
            "analog_minute_anchor_y",
            "analog_minute_smooth_motion",
            "widget_name",
            "arc_radius",
            "arc_max_value",
            "arc_max_value_source",
            "arc_min_value",
            "arc_min_step_value",
            "arc_step_value",
            "arc_source",
            "arc_pos_x",
            "arc_pos_y",
            "analog_second_image",
            "analog_second_anchor_x",
            "analog_second_anchor_y",
            "widget_type",
            "num_spacing",
            "arc_start_angle",
            "num_source",
            "widget_visiblity_source",
            "widget_source",
            "widget_size_width",
            "widget_pos_x",
            "widget_pos_y"
        ]
        self.sourceId = [
            'time_hour',
            'time_hour_low',
            'time_hour_high',
            'time_minute',
            'time_minute_low',
            'time_minute_high',
            'time_second',
            'time_second_low',
            'time_second_high',
            'time_centi_second',
            'time_centi_second_low',
            'time_centi_second_high',
            'date_year',
            'date_year_digit1',
            'date_year_digit2',
            'date_year_digit3',
            'date_year_digit4',
            'date_month',
            'date_month_low',
            'date_month_high',
            'date_day',
            'date_day_low',
            'date_day_high',
            'date_week',
            'date_lunar_year',
            'date_lunar_month',
            'date_lunar_day',
            'date_week_string_short_cn',
            'date_week_string_full_cn',
            'date_week_string_full_pascal_en',
            'date_week_string_full_upper_en',
            'date_week_string_full_lower_en',
            'date_week_string_short_pascal_en',
            'date_week_string_short_upper_en',
            'date_week_string_short_lower_en',
            'date_month_string_short_cn',
            'date_month_string_full_pascal_en',
            'date_month_string_full_upper_en',
            'date_month_string_full_lower_en',
            'date_month_string_short_pascal_en',
            'date_month_string_short_upper_en',
            'date_month_string_short_lower_en',
            'misc_is_am',
            'misc_is_pm',
            'misc_is24_h',
            'health_step_count',
            'health_step_count_digit1',
            'health_step_count_digit2',
            'health_step_count_digit3',
            'health_step_count_digit4',
            'health_step_count_digit5',
            'health_step_progress',
            'health_step_kilo_meter',
            'health_heart_rate',
            'health_heart_rate_zone',
            'health_heart_rate_min',
            'health_heart_rate_max',
            'health_calorie',
            'health_calorie_value',
            'health_calorie_progress',
            'health_stand_count',
            'health_stand_progress',
            'health_oxygen_spo2',
            'health_pressure_index',
            'health_blood_diastolic_pressure_mmhg',
            'health_blood_systolic_pressure_mmhg',
            'health_blood_diastolic_pressure_kpa',
            'health_blood_systolic_pressure_kpa',
            'health_blood_pressure_unit',
            'health_sleep_duration',
            'health_sleep_duration_minute',
            'health_sleep_score',
            'health_sleep_quality',
            'health_sleep_target_progress',
            'health_exercise_duration',
            'health_exercise_progress',
            'health_energy_consumed',
            'health_misc_recovery_time',
            'health_misc_run_power_index',
            'health_misc_today_vitality_value',
            'health_misc_seven_days_vitality_value',
            'weather_current_sun_rise_hour',
            'weather_current_sun_rise_minute',
            'weather_current_sun_set_hour',
            'weather_current_sun_set_minute',
            'weather_temperature_unit',
            'weather_current_temperature',
            'weather_current_temperature_fahrenheit',
            'weather_current_temperature_feel',
            'weather_current_humidity',
            'weather_current_weather',
            'weather_current_wind_direction',
            'weather_current_wind_angle',
            'weather_current_wind_speed',
            'weather_current_wind_level',
            'weather_current_air_quality_index',
            'weather_current_air_quality_level',
            'weather_current_chance_of_rain',
            'weather_current_pressure',
            'weather_current_visibility',
            'weather_current_uv_index',
            'weather_current_dress_index',
            'weather_today_temperature_max',
            'weather_today_temperature_min',
            'weather_today_temperature_max_fahrenheit',
            'weather_today_temperature_min_fahrenheit',
            'weather_tomorrow_temperature_max',
            'weather_tomorrow_temperature_min',
            'weather_tomorrow_temperature_max_fahrenheit',
            'weather_tomorrow_temperature_min_fahrenheit',
            'system_status_battery',
            'system_status_charge',
            'system_status_disturb',
            'system_status_bluetooth',
            'system_status_wifi',
            'system_status_screen_lock',
            'system_sensor_fusion_altitude',
            'app_alarm_hour',
            'app_alarm_minute'
        ]
        self.previewData = {
            "Hour": "10",
            "Hour High": "1",
            "Hour Low": "0",
            "Minute": "08",
            "Minute High": "0",
            "Minute Low": "8",
            "Second": "56",
            "Second High": "5",
            "Second Low": "6",
            "Day": "21",
            "Day High": "2",
            "Day Low": "1",
            "Month": "05",
            "Month High": "0",
            "Month Low": "5",
            "Heart rate": "68",
            "Weather temp": "24", # celsius
            "Weather temp (C)": "24",
            "Weather temp (F)": "75",
            "Current step count": "7645",
            "Current step (percent)": "95",
            "Active Calorie": "465",
            "Active Calorie (percent)": "77",
            "Stand Up value": "11",
            "Stand Up percent": "65",
            "Battery percent": "80",
            "Battery percente": "80",
            "Week": "2"
        }

        self.update()

    def update(self):
        devicesPath = "data/devices.json"
        sourceListPath = "data/sources.json"
        
        self.models.clear()
        self.modelID.clear()
        self.modelSize.clear()
        self.modelSourceData.clear()
        self.modelSourceList.clear()

        with open(devicesPath, "r") as devicesFile:
            devices = json.load(devicesFile)

        with open(sourceListPath, "r") as sourceListFile:
            sources = json.load(sourceListFile)

        for deviceId, device in devices.items():
            self.models.append(device["string"])
            self.modelID[device["string"]] = deviceId
            self.modelSize[deviceId] = [device["width"], device["height"], device["radius"]]
            
        for deviceId, sources in sources.items():
            self.modelSourceData[deviceId] = sources
            self.modelSourceList[deviceId] = [source["string"] for source in sources]
            

    def updateDataFiles(self, compiler, deviceInfo):
        try:
            settings = QSettings("Mi Create", "Workspace")

            xml = []

            fprjDeviceIds = {
                "0": "xiaomi_color",
                "1": "xiaomi_color_sport",
                "2": "70mai_saphir",
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
                "362": "xiaomi_watch_s3",
                "365": "redmi_watch_4",
                "366": "xiaomi_band_9",
            }

            gmfSourceIDs = {
                "1000911": "0A11",
                "1001911": "1A11",
                "1001912": "1A12",
            }

            source_list = {}
            size_list = {}

            with open(deviceInfo, "r") as device_info:
                xml = xmltodict.parse(device_info.read())    

            for device in xml["DeviceList"]["DeviceInfo"]:
                device_size_listing = {
                    "width": int(device["@Width"]),
                    "height": int(device["@Height"]),
                    "radius": int(device["@Radius"]),
                    "preview": {
                        "width": 0,
                        "height": 0,
                        "radius": 0
                    }
                }
                size_list[fprjDeviceIds[device["@Type"]]] = device_size_listing

                source_list[fprjDeviceIds[device["@Type"]]] = []
                for source in device["SourceDataList"]["SRC"]:
                    source_listing = {
                        "string": source["@Name"],
                        "id_fprj": source["@ID"],
                        "id_gmf": gmfSourceIDs["@ID"] or "",
                        "tip": source["@Tip"]
                    }
                    source_list[fprjDeviceIds[device["@Type"]]].append(source_listing)

            with open("data/sources.json", "w") as source_list_file:
                source_list_file.write(json.dumps(source_list, indent=4))

            with open("data/devices.json", "w") as watch_sizes_file:
                watch_sizes_file.write(json.dumps(size_list, indent=4))

            shutil.copyfile(compiler, os.path.join(os.getcwd(), "compiler/compile.exe"))
            self.update()
            settings.setValue("compilerVersion", "custom")
            QMessageBox.information(None, "Data File Update", "Compiler updated successfully. Please restart the program.")
        except Exception as e:
            QMessageBox.critical(None, "Data File Update", "Failed to update: "+str(e))

    def getCompilerVersion(self):
        settings = QSettings("Mi Create", "Workspace")
        if settings.value("compilerVersion") is None:
            version = "m0tral-v4.16"
        else:
            version = settings.value("compilerVersion")
        return version

    def getWatchModel(self, id):
        return self.watchID[id]