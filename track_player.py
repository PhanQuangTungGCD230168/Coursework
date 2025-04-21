import tkinter as tk


import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import Create_track_list
from update_tracks import Update_tracks


def view_tracks_clicked():
    status_lbl.configure(text="View Tracks button was clicked!")
    TrackViewer(tk.Toplevel(window))

def create_track_list_licked():
    status_lbl.configure(text="Create Track List button was clicked!")
    create_track_list = Create_track_list()
    create_track_list.mainloop
    
def update_tracks_clicked():
    status_lbl.configure(text="Update lists button was clicked!")
    update_tracks = Update_tracks()
    update_tracks.mainloop

window = tk.Tk()
window.geometry("500x150")
window.title("JukeBox")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_list_licked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_tracks_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=7, pady=10, sticky=tk.S)

window.mainloop()
