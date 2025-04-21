import tkinter as tk

import track_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class Update_tracks(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Update Tracks")
        self.geometry("590x260")
        
        self.lb_title = tk.Label(self,text="Configure Track's Rating",font=("Arial",20, "bold"))
        self.lb_title.grid(row=0,column=0,columnspan=6,pady=10,sticky=tk.S)

        self.lb_tracknum = tk.Label(self,text="Enter Track Number:",font=("Helvetica", 15))
        self.lb_tracknum.grid(row=1,column=0)
        
        self.number_entry = tk.Entry(self,width=5)
        self.number_entry.grid(row=1,column=1,padx=15,sticky=tk.W)

        self.lb_rating = tk.Label(self,text="Enter New Rating:",font=("Helvetica", 15))
        self.lb_rating.grid(row=2,column=0, sticky=tk.W)
        
        self.rating_input = tk.Entry(self, width=5)
        self.rating_input.grid(row=2, column=1, padx=15, sticky=tk.W)
        
        self.lb_text = tk.Label(self, text="Track detail:", font=("Helvetica", 12))
        self.lb_text.grid(row=1, column=5, sticky=tk.SW)
        
        self.text_box = tk.Text(self, width=26, height=5, wrap="none", font=("Helvetica", 15))
        self.text_box.grid(row=2, column=5, columnspan=5)

        self.update_btn = tk.Button(self,text="Update Rating",font=("Helvetica", 15),command=self.update_track)
        self.update_btn.grid(row=3,column=0)

    def update_track(self):
        try:
            new_rating = int(self.rating_input.get())
            if new_rating > 5 or new_rating < 0:
                set_text(self.text_box, "Rating must be a number\nfrom 1 to 5")
                return
        except ValueError:
            set_text(self.text_box, "Invalid rating input\nPlease try using numbers\nlike '1' or '01'")
            return
        try:
            track_number = int(self.number_entry.get())
            key = "%02d" % track_number
            name = lib.get_name(key)
            lib.set_rating(key,new_rating) 
            if name is not None:
                artist = lib.get_artist(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
                set_text(self.text_box, track_details)
            else:
                set_text(self.text_box, f"Track {key} not found")
        except ValueError:
            set_text(self.text_box, "Invalid number input\nPlease try using numbers\nlike '1' or '01'")
        
if __name__ == "__main__":
    update_tracks = Update_tracks()
    update_tracks.mainloop()
