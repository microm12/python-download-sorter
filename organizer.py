import os 
import shutil

extensions_folders = {
#No name
    'noname' : "/Users/Mark/Downloads/Other/",
#Audio
    '.aif' : "/Users/Mark/Downloads/Media/Audio/",
    '.cda' : "/Users/Mark/Downloads/Media/Audio/",
    '.mid' : "/Users/Mark/Downloads/Media/Audio/",
    '.midi' : "/Users/Mark/Downloads/Media/Audio/",
    '.mp3' : "/Users/Mark/Downloads/Media/Audio/",
    '.mpa' : "/Users/Mark/Downloads/Media/Audio/",
    '.ogg' : "/Users/Mark/Downloads/Media/Audio/",
    '.wav' : "/Users/Mark/Downloads/Media/Audio/",
    '.wma' : "/Users/Mark/Downloads/Media/Audio/",
    '.wpl' : "/Users/Mark/Downloads/Media/Audio/",
    '.m3u' : "/Users/Mark/Downloads/Media/Audio/",
#Text
    '.txt' : "/Users/Mark/Downloads/Text/",
    '.doc' : "/Users/Mark/Downloads/Text/",
    '.docx' : "/Users/Mark/Downloads/Text/",
    '.odt ' : "/Users/Mark/Downloads/Text/",
    '.pdf': "/Users/Mark/Downloads/Text/",
    '.rtf': "/Users/Mark/Downloads/Text/",
    '.tex': "/Users/Mark/Downloads/Text/",
    '.wks ': "/Users/Mark/Downloads/Text/",
    '.wps': "/Users/Mark/Downloads/Text/",
    '.wpd': "/Users/Mark/Downloads/Text/",
#Video
    '.3g2': "/Users/Mark/Downloads/Media/Videos/",
    '.3gp': "/Users/Mark/Downloads/Media/Videos/",
    '.avi': "/Users/Mark/Downloads/Media/Videos/",
    '.flv': "/Users/Mark/Downloads/Media/Videos/",
    '.h264': "/Users/Mark/Downloads/Media/Videos/",
    '.m4v': "/Users/Mark/Downloads/Media/Videos/",
    '.mkv': "/Users/Mark/Downloads/Media/Videos/",
    '.mov': "/Users/Mark/Downloads/Media/Videos/",
    '.mp4': "/Users/Mark/Downloads/Media/Videos/",
    '.mpg': "/Users/Mark/Downloads/Media/Videos/",
    '.mpeg': "/Users/Mark/Downloads/Media/Videos/",
    '.rm': "/Users/Mark/Downloads/Media/Videos/",
    '.swf': "/Users/Mark/Downloads/Media/Videos/",
    '.vob': "/Users/Mark/Downloads/Media/Videos/",
    '.wmv': "/Users/Mark/Downloads/Media/Videos/",
#Images
    '.ai': "/Users/Mark/Downloads/Media/Images/",
    '.bmp': "/Users/Mark/Downloads/Media/Images/",
    '.gif': "/Users/Mark/Downloads/Media/Images/",
    '.ico': "/Users/Mark/Downloads/Media/Images/",
    '.jpg': "/Users/Mark/Downloads/Media/Images/",
    '.jpeg': "/Users/Mark/Downloads/Media/Images/",
    '.png': "/Users/Mark/Downloads/Media/Images/",
    '.ps': "/Users/Mark/Downloads/Media/Images/",
    '.psd': "/Users/Mark/Downloads/Media/Images/",
    '.svg': "/Users/Mark/Downloads/Media/Images/",
    '.tif': "/Users/Mark/Downloads/Media/Images/",
    '.tiff': "/Users/Mark/Downloads/Media/Images/",
    '.CR2': "/Users/Mark/Downloads/Media/Images/",
#Internet
    '.asp': "/Users/Mark/Downloads/Other/",
    '.aspx': "/Users/Mark/Downloads/Other/",
    '.cer': "/Users/Mark/Downloads/Other/",
    '.cfm': "/Users/Mark/Downloads/Other/",
    '.cgi': "/Users/Mark/Downloads/Other/",
    '.pl': "/Users/Mark/Downloads/Other/",
    '.css': "/Users/Mark/Downloads/Other/",
    '.htm': "/Users/Mark/Downloads/Other/",
    '.js': "/Users/Mark/Downloads/Other/",
    '.jsp': "/Users/Mark/Downloads/Other/",
    '.part': "/Users/Mark/Downloads/Other/",
    '.php': "/Users/Mark/Downloads/Other/",
    '.rss': "/Users/Mark/Downloads/Other/",
    '.xhtml': "/Users/Mark/Downloads/Other/",
#Compressed
    '.7z': "/Users/Mark/Downloads/Other/Zips/",
    '.arj': "/Users/Mark/Downloads/Other/Zips/",
    '.deb': "/Users/Mark/Downloads/Other/Zips/",
    '.pkg': "/Users/Mark/Downloads/Other/Zips/",
    '.rar': "/Users/Mark/Downloads/Other/Zips/",
    '.rpm': "/Users/Mark/Downloads/Other/Zips/",
    '.tar.gz': "/Users/Mark/Downloads/Other/Zips/",
    '.z': "/Users/Mark/Downloads/Other/Zips/",
    '.zip': "/Users/Mark/Downloads/Other/Zips/",
#Disc
    '.bin': "/Users/Mark/Downloads/Other/",
    '.dmg': "/Users/Mark/Downloads/Other/",
    '.iso': "/Users/Mark/Downloads/Other/",
    '.toast': "/Users/Mark/Downloads/Other/",
    '.vcd': "/Users/Mark/Downloads/Other/",
#Data
    '.csv': "/Users/Mark/Downloads/Programming/",
    '.dat': "/Users/Mark/Downloads/Programming/",
    '.db': "/Users/Mark/Downloads/Programming/",
    '.dbf': "/Users/Mark/Downloads/Programming/",
    '.log': "/Users/Mark/Downloads/Programming/",
    '.mdb': "/Users/Mark/Downloads/Programming/",
    '.sav': "/Users/Mark/Downloads/Programming/",
    '.sql': "/Users/Mark/Downloads/Programming/",
    '.tar': "/Users/Mark/Downloads/Programming/",
    '.xml': "/Users/Mark/Downloads/Programming/",
    '.json': "/Users/Mark/Downloads/Programming/",
#Executables
    '.apk': "/Users/Mark/Downloads/Other/Executables/",
    '.bat': "/Users/Mark/Downloads/Other/Executables/",
    '.com': "/Users/Mark/Downloads/Other/Executables/",
    '.exe': "/Users/Mark/Downloads/Other/Executables/",
    '.gadget': "/Users/Mark/Downloads/Other/Executables/",
    '.jar': "/Users/Mark/Downloads/Other/Executables/",
    '.wsf': "/Users/Mark/Downloads/Other/Executables/",
#Fonts
    '.fnt': "/Users/Mark/Downloads/Other/",
    '.fon': "/Users/Mark/Downloads/Other/",
    '.otf': "/Users/Mark/Downloads/Other/",
    '.ttf': "/Users/Mark/Downloads/Other/",
#Presentations
    '.key': "/Users/Mark/Downloads/Text/",
    '.odp': "/Users/Mark/Downloads/Text/",
    '.pps': "/Users/Mark/Downloads/Text/",
    '.ppt': "/Users/Mark/Downloads/Text/",
    '.pptx': "/Users/Mark/Downloads/Text/",
#Programming
    '.c': "/Users/Mark/Downloads/Programming/",
    '.class': "/Users/Mark/Downloads/Programming/",
    '.dart': "/Users/Mark/Downloads/Programming/",
    '.py': "/Users/Mark/Downloads/Programming/",
    '.sh': "/Users/Mark/Downloads/Programming/",
    '.swift': "/Users/Mark/Downloads/Programming/",
    '.html': "/Users/Mark/Downloads/Programming/",
    '.h': "/Users/Mark/Downloads/Programming/",
#Spreadsheets
    '.ods' : "/Users/Mark/Downloads/Text/",
    '.xlr' : "/Users/Mark/Downloads/Text/",
    '.xls' : "/Users/Mark/Downloads/Text/",
    '.xlsx' : "/Users/Mark/Downloads/Text/",
#System
    '.bak' : "/Users/Mark/Downloads/Other/",
    '.cab' : "/Users/Mark/Downloads/Other/",
    '.cfg' : "/Users/Mark/Downloads/Other/",
    '.cpl' : "/Users/Mark/Downloads/Other/",
    '.cur' : "/Users/Mark/Downloads/Other/",
    '.dll' : "/Users/Mark/Downloads/Other/",
    '.dmp' : "/Users/Mark/Downloads/Other/",
    '.drv' : "/Users/Mark/Downloads/Other/",
    '.icns' : "/Users/Mark/Downloads/Other/",
    '.ini' : "/Users/Mark/Downloads/Other/",
    '.lnk' : "/Users/Mark/Downloads/Other/",
    '.msi' : "/Users/Mark/Downloads/Other/",
    '.sys' : "/Users/Mark/Downloads/Other/",
    '.tmp' : "/Users/Mark/Downloads/Other/",
}

folder_to_track = '/Users/Mark/Downloads/'

folders = ['Text', 'Media', 'Other', 'Programming', 'Media/Images', 'Media/Videos', 'Media/Audio', 'Other/Zips', 'Other/Executables']
for folder in folders:
    if not os.path.exists(folder_to_track + folder):
        os.mkdir(folder_to_track + folder)

for file in os.listdir(folder_to_track):
    if file not in folders and file != 'desktop.ini':
        try:
            extension = str(os.path.splitext(file)[1])
            path = extensions_folders[extension]
        except Exception:
            extension='noname'
            path=extensions_folders[extension]
        path+= file
        shutil.move(folder_to_track + file, path)
