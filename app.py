import tkinter as tk
import pymongo

# MONGO DB SETUP
client = pymongo.MongoClient("mongodb+srv://robin:admin123456@robinsglobalachat.p5nljje.mongodb.net/?appName=RobinsGlobalaChat")
db = client["PyChat"]
messages_collection = db["messages"]

root = tk.Tk()
root.title("MonogChat")
root.geometry("800x800")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# a function to send code to the database
def send_message():
    if entry.get():
       messages_collection.insert_one({"text": entry.get()})
       entry .delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

message_label = tk.Label(root, text="Messages: ", justify="left")
message_label.pack()

def fetch_messages():
    messages = messages_collection.find().sort("_id")
    message_label.config(text="Messages: \n" + "\n".join(f" - {m['text']}" for m in messages) )
    root.after(2000, fetch_messages)


fetch_messages()
root.mainloop()


# Visuella
# Steg 1, Tryck på source control ikonen till vänster
# Steg 2, append changes
# Steg 3, skriv en kommentar
# steg 4, tryck på commit
# steg 5, tryck på push


# Terminal
# Steg 1, Git status
# Steg 2, git add .
# Steg 3, skriv: git commit -m "någoin kommentar om något" sen enter
# steg 4, skriv: git push