import tkinter as tk
from tkinter import ttk,filedialog
import requests
import os

#https://us.download.nvidia.com/Windows/552.12/552.12-notebook-win10-win11-64bit-international-dch-whql.exe
class Downloader:
    def __init__(self):
        self.filepath=""
        self.window = tk.Tk()
        self.window.title("Internet Downloader")

        self.url_label = tk.Label(text="Enter URL")
        self.url_label.pack()

        self.url_entry = tk.Entry()
        self.url_entry.pack()

        self.browse_button = tk.Button(text="Browse",command=self.browse_file) 
        self.browse_button.pack()
        self.download = tk.Button(text="Download",command=self.download)
        self.download.pack()
        self.window.geometry("800x350")
        # self.start_button = tk.Button(text="Start", command=self.download)
        # self.start_button.pack(side=tk.LEFT)

        # self.pause_button = tk.Button(text="Pause", command=self.pause_download)
        # self.pause_button.pack(side=tk.LEFT)
        
        self.progress_bar = ttk.Progressbar(self.window,orient="horizontal",maximum=100,length=300,mode="determinate")
        self.progress_bar.pack()
        self.percentage = tk.Label(text=self.progress_bar['value'])
        self.percentage.pack()
        self.window.mainloop()
        

    def browse_file(self):
        filepath = filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1].split("?")[0])
        self.filepath = filepath

    def download(self):
        url = self.url_entry.get()
        response = requests.get(url,stream=True)
        totalFileSize = 100
        if (response.headers.get("content-length")):
            totalFileSize = int(response.headers.get("content-length"))
        block_size = 10000
        self.progress_bar["value"]=0
        fileName = self.url_entry.get().split("/")[-1].split("?")[0]
        if not self.filepath:
            self.filepath = os.path.join(os.path.expanduser('~'), 'Downloads', fileName)

        with open(self.filepath, "wb") as f:
            downloaded = 0
            for data in response.iter_content(block_size):
                f.write(data)
                downloaded += len(data)
                progress = (downloaded / totalFileSize) * 100
                self.progress_bar["value"] = progress
                self.percentage.config(text=f"{progress:.2f}%")
                self.window.update() 
    def start_download(self):
        # Implement the start download functionality
        pass

    def pause_download(self):
        # Implement the pause download functionality
        pass

Downloader()