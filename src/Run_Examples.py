# Import modules
import groupdocs_conversion_cloud
from Common_Utilities.Utils import Common_Utilities

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
Common_Utilities.host_url = "http://api.groupdocs.cloud"  # Put your Host URL here
Common_Utilities.app_sid = "d215ce72-1609-4282-8d55-5810942236fb"
Common_Utilities.app_key = "715d18b0afef2f303882c769921fe05a"
Common_Utilities.myStorage = "MyStorage"

# #########################################
# print("Executing Upload Test Files...")
# Common_Utilities.Upload_Test_Files()
# #########################################

###########################################
#******* Execute Examples *******
print("*** Executing examples...")
#******* Execute Examples *******
###########################################

#########################################
print("*** Executing Get_Supported_File_Formats...")
#########################################

print("* Executing Conversion_Python_Get_All_Supported_Formats...")
from Supported_File_Formats.Conversion_Python_Get_All_Supported_Formats import Conversion_Python_Get_All_Supported_Formats
Conversion_Python_Get_All_Supported_Formats.Run()

# print("* Executing Conversion_Python_Get_All_Supported_Formats_For_Document...")
# from Supported_File_Formats.Conversion_Python_Get_All_Supported_Formats_For_Document import Conversion_Python_Get_All_Supported_Formats_For_Document
# Conversion_Python_Get_All_Supported_Formats_For_Document.Run()

# print("* Executing Conversion_Python_Get_All_Supported_Formats_For_Extension...")
# from Supported_File_Formats.Conversion_Python_Get_All_Supported_Formats_For_Extension import Conversion_Python_Get_All_Supported_Formats_For_Extension
# Conversion_Python_Get_All_Supported_Formats_For_Extension.Run()

# ##########################################
# print("*** Executing Working_With_Storage...")
# ##########################################

# print("* Executing Conversion_Python_Storage_Exist...")
# from Working_With_Storage.Conversion_Python_Storage_Exist import Conversion_Python_Storage_Exist
# Conversion_Python_Storage_Exist.Run()

# print("* Executing Conversion_Python_Object_Exists...")
# from Working_With_Storage.Conversion_Python_Object_Exists import Conversion_Python_Object_Exists
# Conversion_Python_Object_Exists.Run()

# print("* Executing Conversion_Python_Get_File_Versions...")
# from Working_With_Storage.Conversion_Python_Get_File_Versions import Conversion_Python_Get_File_Versions
# Conversion_Python_Get_File_Versions.Run()

# print("* Executing Conversion_Python_Get_Disc_Usage...")
# from Working_With_Storage.Conversion_Python_Get_Disc_Usage import Conversion_Python_Get_Disc_Usage
# Conversion_Python_Get_Disc_Usage.Run()

# ##########################################
# print("*** Executing Working_With_Folder...")
# ##########################################

# print("* Executing Conversion_Python_Create_Folder...")
# from Working_With_Folder.Conversion_Python_Create_Folder import Conversion_Python_Create_Folder
# Conversion_Python_Create_Folder.Run()

# print("* Executing Conversion_Python_Copy_Folder...")
# from Working_With_Folder.Conversion_Python_Copy_Folder import Conversion_Python_Copy_Folder
# Conversion_Python_Copy_Folder.Run()

# print("* Executing Conversion_Python_Get_Files_List...")
# from Working_With_Folder.Conversion_Python_Get_Files_List import Conversion_Python_Get_Files_List
# Conversion_Python_Get_Files_List.Run()

# print("* Executing Conversion_Python_Move_Folder...")
# from Working_With_Folder.Conversion_Python_Move_Folder import Conversion_Python_Move_Folder
# Conversion_Python_Move_Folder.Run()

# print("* Executing Conversion_Python_Delete_Folder...")
# from Working_With_Folder.Conversion_Python_Delete_Folder import Conversion_Python_Delete_Folder
# Conversion_Python_Delete_Folder.Run()

# ##########################################
# print("*** Executing Working_With_Files...")
# ##########################################

# print("* Executing Conversion_Python_Upload_File...")
# from Working_With_Files.Conversion_Python_Upload_File import Conversion_Python_Upload_File
# Conversion_Python_Upload_File.Run()

# print("* Executing Conversion_Python_Download_File...")
# from Working_With_Files.Conversion_Python_Download_File import Conversion_Python_Download_File
# Conversion_Python_Download_File.Run()

# print("* Executing Conversion_Python_Copy_File...")
# from Working_With_Files.Conversion_Python_Copy_File import Conversion_Python_Copy_File
# Conversion_Python_Copy_File.Run()

# print("* Executing Conversion_Python_Move_File...")
# from Working_With_Files.Conversion_Python_Move_File import Conversion_Python_Move_File
# Conversion_Python_Move_File.Run()

# print("* Executing Conversion_Python_Delete_File...")
# from Working_With_Files.Conversion_Python_Delete_File import Conversion_Python_Delete_File
# Conversion_Python_Delete_File.Run()

##########################################
print("*** Executing Working_With_Conversions...")
##########################################

print("* Executing Conversion_Python_Convert_To_Any_Format...")
from Working_With_Conversions.Conversion_Python_Convert_To_Any_Format import Conversion_Python_Convert_To_Any_Format
convertOptions = groupdocs_conversion_cloud.JpgConvertOptions()
Conversion_Python_Convert_To_Any_Format.Run("jpg", convertOptions)

# print("* Executing Conversion_Python_Convert_To_Any_Format_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Any_Format_Stream import Conversion_Python_Convert_To_Any_Format_Stream
# convertOptions = groupdocs_conversion_cloud.JpgConvertOptions()
# Conversion_Python_Convert_To_Any_Format_Stream.Run("jpg", convertOptions)

# print("* Executing Conversion_Python_Convert_To_Cells...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Cells import Conversion_Python_Convert_To_Cells
# Conversion_Python_Convert_To_Cells.Run()

# print("* Executing Conversion_Python_Convert_To_Cells_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Cells_Stream import Conversion_Python_Convert_To_Cells_Stream
# Conversion_Python_Convert_To_Cells_Stream.Run()

# print("* Executing Conversion_Python_Convert_To_Html...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Html import Conversion_Python_Convert_To_Html
# Conversion_Python_Convert_To_Html.Run()

# print("* Executing Conversion_Python_Convert_To_Html_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Html_Stream import Conversion_Python_Convert_To_Html_Stream
# Conversion_Python_Convert_To_Html_Stream.Run()

# print("* Executing Conversion_Python_Convert_To_Images...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Images import Conversion_Python_Convert_To_Images
# Conversion_Python_Convert_To_Images.Run()

# print("* Executing Conversion_Python_Convert_To_Images_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Images_Stream import Conversion_Python_Convert_To_Images_Stream
# Conversion_Python_Convert_To_Images_Stream.Run()

# print("* Executing Conversion_Python_Convert_To_Pdf...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Pdf import Conversion_Python_Convert_To_Pdf
# Conversion_Python_Convert_To_Pdf.Run()

# print("* Executing Conversion_Python_Convert_To_Pdf_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Pdf_Stream import Conversion_Python_Convert_To_Pdf_Stream
# Conversion_Python_Convert_To_Pdf_Stream.Run()

# print("* Executing Conversion_Python_Convert_To_Slides...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Slides import Conversion_Python_Convert_To_Slides
# Conversion_Python_Convert_To_Slides.Run()

# print("* Executing Conversion_Python_Convert_To_Slides_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Slides_Stream import Conversion_Python_Convert_To_Slides_Stream
# Conversion_Python_Convert_To_Slides_Stream.Run()

# print("* Executing Conversion_Python_Convert_To_Text...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Text import Conversion_Python_Convert_To_Text
# Conversion_Python_Convert_To_Text.Run()

# print("* Executing Conversion_Python_Convert_To_Text_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Text_Stream import Conversion_Python_Convert_To_Text_Stream
# Conversion_Python_Convert_To_Text_Stream.Run()

# print("* Executing Conversion_Python_Convert_To_Words...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Words import Conversion_Python_Convert_To_Words
# Conversion_Python_Convert_To_Words.Run()

# print("* Executing Conversion_Python_Convert_To_Words_Stream...")
# from Working_With_Conversions.Conversion_Python_Convert_To_Words_Stream import Conversion_Python_Convert_To_Words_Stream
# Conversion_Python_Convert_To_Words_Stream.Run()
