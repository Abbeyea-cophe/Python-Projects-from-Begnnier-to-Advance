from pytube import YouTube
import tkinter as tk
from tkinter import filedialog



def downloadVideo(url, savePath):
    try :
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = 'mp4')
        highestResStream = streams.get_highest_resolution()
        highestResStream.download(output_path = savePath)
        print('Videos download successfully!')
    except Exception as e:
        print(e)
        

def openFileDialog( ):
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
        
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    
    videoUrl = input('Please enter a YouTube url: ')
    saveDir = openFileDialog()
    
    if not saveDir:
        downloadVideo(videoUrl, saveDir)    
    else:
        print('No folder selected. Please select a folder to save the video.')

        
