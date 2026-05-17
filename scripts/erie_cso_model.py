import arcpy
import os

print("ArcPy is working.")

arcpy.env.overwriteOutput = True

project_folder = r"C:\Users\hveisi\OneDrive - UWSP\GIS\Erie_CSO_EJ_Analysis"

gdb = os.path.join(project_folder, "Erie_CSO_EJ_Analysis.gdb")

arcpy.env.workspace = gdb

print("Workspace set to:")
print(arcpy.env.workspace)