import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib

from random import shuffle

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)
    
class Create_track_list(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Track List")
        self.geometry("560x270")

        self.lb_title = tk.Label(self,text="Playlist",font=("Arial",20,"bold"))
        self.lb_title.grid(row=0,column=0,columnspan=10,sticky=tk.N)
        
        self.lb_track = tk.Label(self,text="Track Number:",font=("Helvetica", 15))
        self.lb_track.grid(row=1,column=0,sticky=tk.E)
        
        self.track_number = tk.Entry(self,width=3)
        self.track_number.grid(row=1,column=1,sticky=tk.W)
        
        self.add_track_btn = tk.Button(self, text="Add Track", command=self.add_track,font=("Helvetica", 15))
        self.add_track_btn.grid(row=2, column=0, sticky=tk.N)
        
        self.lb_list = tk.Label(self, text="Current Playlist:",font=("Helvetica", 12))
        self.lb_list.grid(row=2, column=6, sticky=tk.SW,padx=10)

        self.lb_state =tk.Label(self,text="",font=("Helvetica", 12))
        self.lb_state.grid(row=5,column=6, columnspan=5, sticky=tk.E)

        self.list_text_box = tkst.ScrolledText(self, width=40, height=5, wrap="none", font=("Helvetica", 12))
        self.list_text_box.grid(row=3, column=6, columnspan=5, sticky="NE", padx=10)

        self.play_all_btn = tk.Button(self,text="Play All", command=self.play_tracks_list,font=("Helvetica", 15))
        self.play_all_btn.grid(row=3,column=0, sticky=tk.S)

        self.reset_btn = tk.Button(self,text="Reset List", command=self.reset_list,font=("Helvetica", 15))
        self.reset_btn.grid(row=3,column=0, sticky=tk.N)
        
        self.shuffle_btn = tk.Button(self, text="Shuffle",command=self.shuffle_list,font=("Helvetica", 15))
        self.shuffle_btn.grid(row=4,column=0,sticky=tk.N)
        
        self.play_list = []
        
        self.detail = ""
        
        self.print_detail()
        
    def add_track(self):
        try :
            tracknum = int(self.track_number.get())
            key = "%02d" % tracknum
            name = lib.get_name(key)
            if name is not None:
                if key in self.play_list:
                    self.lb_state.configure(text="Track already in list")
                else:
                    self.play_list.append(key)
                    self.lb_state.configure(text=f"Track {key} added")
                    self.print_detail()
            else:
                self.lb_state.configure(text="Track does not exist")
            self.print_detail()
        except ValueError:
            self.lb_state.configure(text="Invalid input")

    def play_tracks_list(self):
        if len(self.play_list) == 0:
            self.lb_state.configure(text="Playlist is empty")
        else:
            for key in self.play_list:
                lib.increment_play_count(key)
            self.print_detail()
            self.lb_state.configure(text="Played all tracks")

    def reset_list(self):
        if len(self.play_list) == 0:
            self.lb_state.configure(text="Playlist is empty")
        else:
            self.play_list = []
            self.detail = ""
            self.print_detail()
            self.lb_state.configure(text="Playlist has been reset")

    def shuffle_list(self):
        if len(self.play_list) == 0:
            self.lb_state.configure(text="Playlist is empty")
        elif len(self.play_list) == 1:
            self.lb_state.configure(text="There is only one track")
        else:            
            shuffle(self.play_list)
            self.print_detail()
            self.lb_state.configure(text="Playlist has been shuffled")
        
    def print_detail(self):
        tracks_detail =''
        for key in self.play_list:
            name = lib.get_name(key)
            artist = lib.get_artist(key)
            play_count = lib.get_play_count(key) 
            tracks_detail += f"{name} - {artist}. Played: {play_count}\n"
        self.detail = tracks_detail
        set_text(self.list_text_box, self.detail)
        
if __name__== "__main__":
    create_track_list = Create_track_list()
    create_track_list.mainloop()
