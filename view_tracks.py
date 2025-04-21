import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import ImageTk, Image
from tkinter import ttk

import track_library as lib
import font_manager as fonts


def set_text(text_area, content): #display on scroll text function
    text_area.delete("1.0", tk.END) #delete all previous text
    text_area.insert(1.0, content) #display new text


class TrackViewer():
    def __init__(self, window):
        window.geometry("750x350")
        window.title("View Tracks")
        
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky=tk.NW, padx=10, pady=10)

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        self.lb_photo = tk.Label(window)
        self.lb_photo.grid(row=1, column=3, sticky=tk.S)
        
    def view_tracks_clicked(self):
        try:
            track_number = int(self.input_txt.get())
            key = "%02d" % track_number
            name = lib.get_name(key)
            if name is not None:
                artist = lib.get_artist(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
                set_text(self.track_txt, track_details)
                self.open_image(key)   
                self.status_lbl.configure(text="View Track button was clicked!")         
            else:
                set_text(self.track_txt, f"Track {key} not found")
        except ValueError:
            set_text(self.track_txt, "Invalid number input")
            
    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")
        
    def open_image(self,key):
        self.image_tk = Image.open(f"_Track_{key}.jpg").resize((120,120))
        self.image_tk = ImageTk.PhotoImage(self.image_tk)
        self.lb_photo.config(image=self.image_tk)

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
