from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# Replace these with your actual SharePoint site details
sharepoint_url = "https://yoursharepointsite.sharepoint.com"
username = "username here"
password = "password here"
site_url = "https://yoursharepointsite.sharepoint.com/sites/sitename-here"
folder_path = "Shared Documents/foldername"
local_save_path = "Download directory"

# Authenticate with SharePoint
authcookie = Office365(sharepoint_url, username=username, password=password).GetCookies()

# Access the SharePoint site
site = Site(site_url, version=Version.v365, authcookie=authcookie)

# Access the folder within the document library
folder = site.Folder(folder_path)

# Download the file
file_name = 'filename'
file_content = folder.get_file(file_name)

# Save the file locally
with open(local_save_path, 'wb') as file:
    file.write(file_content)

print(f"File '{file_name}' downloaded successfully to '{local_save_path}'")
