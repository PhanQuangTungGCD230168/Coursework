import tkinter as tk #Import tkinkter
import tkinter.scrolledtext as tkst #Import scrolled text display


import track_library as lib #Import a custom module to manage track data   
import font_manager as fonts #Import a custom module to manage font


def set_text(text_area, content): #display on scroll text function
    text_area.delete("1.0", tk.END) #delete all previous text
    text_area.insert(1.0, content) #display new text


class TrackViewer():
    def __init__(self, window):
        #Configure main window
        window.geometry("750x350")
        window.title("View Tracks")

        #Create a button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        
        #Create label for track number input
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        #Create field for track number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        #Create button to view inputted track
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        #Create a scrolledable text area to display tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, font=("Helvetica", 10))
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        #Create a text area to display inputted track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        #Create a label displays status message
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        #Run function when initiate window
        self.list_tracks_clicked()

    def view_tracks_clicked(self):                                                      #Create function for displaying track
        key = self.input_txt.get()                                                      #Get track number from input
        name = lib.get_name(key)                                                        #Get track detail from key
        if name is not None:                                                            #If input is valid
            artist = lib.get_artist(key)                                                #Get track's name
            rating = lib.get_rating(key)                                                #Get track's rating
            play_count = lib.get_play_count(key)                                        #Get track's play count
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"  #Details of track text
            set_text(self.track_txt, track_details)                                     #Display track details
        else:                                                                           #If input is invalid
            set_text(self.track_txt, f"Track {key} not found")                          #Display error message
        self.status_lbl.configure(text="View Track button was clicked!")                #Display status message

    def list_tracks_clicked(self):                                                      #Create function for listing all tracks
        track_list = lib.list_all()                                                     #Get details of all tracks
        set_text(self.list_txt, track_list)                                             #Display all tracks
        self.status_lbl.configure(text="List Tracks button was clicked!")               #Display status message

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
