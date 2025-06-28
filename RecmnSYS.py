import tkinter as tk
from tkinter import messagebox, simpledialog

user_credentials = {
    "Amit": "amit123",
    "Priya": "priya123",
    "Rahul": "rahul123",
    "Sneha": "sneha123",
    "Vikas": "vikas123",
    "Neha": "neha123",
    "Arjun": "arjun123",
    "Divya": "divya123",
    "Ravi": "ravi123",
    "Pooja": "pooja123",
    "Karan": "karan123",
    "Simran": "simran123",
    "Manish": "manish123",
    "Anjali": "anjali123",
    "Raj": "raj123",
    "Isha": "isha123",
    "Saurabh": "saurabh123",
    "Khushi": "khushi123",
    "Nikhil": "nikhil123",
    "Tanya": "tanya123"
}

users = {
    "Amit": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "Avatar": 4, "Avengers: Endgame": 5,
        "The Dark Knight": 5, "Parasite": 4, "Your Name": 5, "Attack on Titan": 5, "The Prestige": 4,
        "KGF": 4, "Baahubali": 5, "Asuran": 4, "Kantara": 5, "Joker": 5, "Spider-Man: Into the Spider-Verse": 5
    },
    "Priya": {
        "The Notebook": 5, "La La Land": 4, "Titanic": 5, "Little Women": 5, "Pride and Prejudice": 5,
        "Your Name": 5, "Weathering With You": 5, "The Pursuit of Happyness": 5, "Hidden Figures": 5,
        "Parasite": 5, "Spider-Man: Homecoming": 4, "Doctor Strange": 4, "Black Panther": 4, "Interstellar": 4,
        "The Matrix": 5, "Avatar": 5
    },
    "Rahul": {
        "Inception": 5, "The Dark Knight": 5, "The Matrix": 5, "Fight Club": 5, "Pulp Fiction": 5,
        "John Wick": 5, "Mad Max: Fury Road": 5, "Tenet": 4, "Interstellar": 5, "Avatar": 5,
        "Avengers: Endgame": 5, "Joker": 5, "Parasite": 4, "KGF": 4, "Vikram": 4, "Baahubali": 5
    },
    "Sneha": {
        "Amelie": 5, "Little Women": 5, "The Notebook": 5, "La La Land": 5, "Your Name": 5,
        "Weathering With You": 5, "Pride and Prejudice": 5, "Hidden Figures": 5, "The Pursuit of Happyness": 5,
        "The Theory of Everything": 5, "Interstellar": 4, "Parasite": 4, "The Prestige": 5, "Arrival": 5,
        "Spirited Away": 5, "Ponyo": 5
    },
    "Vikas": {
        "KGF": 5, "Baahubali": 5, "RRR": 5, "Vikram": 5, "Master": 4,
        "Asuran": 4, "Jai Bhim": 5, "Kantara": 5, "Drishyam": 5, "Lucifer": 5,
        "Vikram Vedha": 5, "Pushpa": 5, "Agent Sai Srinivasa Athreya": 5, "Eega": 5,
        "Inception": 5, "The Dark Knight": 5, "John Wick": 5
    },
    "Neha": {
        "Little Women": 5, "The Notebook": 5, "Pride and Prejudice": 5, "Amelie": 5,
        "Your Name": 5, "Weathering With You": 5, "La La Land": 5, "Hidden Figures": 5,
        "The Pursuit of Happyness": 5, "Interstellar": 5, "Parasite": 5, "Arrival": 5,
        "The Theory of Everything": 5, "Spirited Away": 5, "Ponyo": 5, "The Farewell": 5
    },
    "Arjun": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "The Dark Knight": 5, "Fight Club": 5,
        "John Wick": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5, "Avatar": 5, "Avengers: Endgame": 5,
        "Parasite": 4, "Joker": 5, "Tenet": 5, "KGF": 5, "RRR": 5, "Baahubali": 5
    },
    "Divya": {
        "Your Name": 5, "Weathering With You": 5, "Spirited Away": 5, "Ponyo": 5, "Amelie": 5,
        "The Notebook": 5, "Pride and Prejudice": 5, "Little Women": 5, "La La Land": 5, "Hidden Figures": 5,
        "The Pursuit of Happyness": 5, "The Farewell": 5, "The Theory of Everything": 5,
        "Arrival": 5, "Parasite": 5, "The Prestige": 5
    },
    "Ravi": {
        "Inception": 5, "Interstellar": 5, "The Dark Knight": 5, "The Matrix": 5, "Avatar": 5,
        "John Wick": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5, "Fight Club": 5, "Tenet": 5,
        "Joker": 5, "Parasite": 5, "RRR": 5, "KGF": 5, "Vikram": 5, "Master": 5
    },
    "Pooja": {
        "Your Name": 5, "Weathering With You": 5, "Spirited Away": 5, "Ponyo": 5,
        "Amelie": 5, "The Notebook": 5, "La La Land": 5, "Pride and Prejudice": 5,
        "Little Women": 5, "Hidden Figures": 5, "The Pursuit of Happyness": 5, "Arrival": 5,
        "Parasite": 5, "The Farewell": 5, "The Theory of Everything": 5, "Coco": 5
    },
    "Karan": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "The Dark Knight": 5,
        "Fight Club": 5, "John Wick": 5, "Mad Max: Fury Road": 5, "Avatar": 5,
        "Avengers: Endgame": 5, "Parasite": 5, "Tenet": 5, "Joker": 5, "KGF": 5,
        "Baahubali": 5, "RRR": 5, "Vikram": 5, "Pushpa": 5
    },
    "Simran": {
        "Coco": 5, "Inside Out": 5, "Soul": 5, "Your Name": 5, "Weathering With You": 5,
        "Spirited Away": 5, "Ponyo": 4, "La La Land": 5, "Little Women": 5, "Amelie": 5,
        "Hidden Figures": 5, "The Pursuit of Happyness": 5, "The Theory of Everything": 5,
        "The Farewell": 5, "Arrival": 5, "Parasite": 5, "Titanic": 5, "Pride and Prejudice": 5
    },
    "Manish": {
        "Inception": 5, "The Matrix": 5, "Interstellar": 5, "The Dark Knight": 5,
        "Fight Club": 5, "John Wick": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5,
        "Tenet": 5, "Joker": 5, "Avatar": 5, "Avengers: Endgame": 5, "Gladiator": 5,
        "The Godfather": 5, "Parasite": 5, "Vikram": 5, "RRR": 5, "KGF": 5
    },
    "Anjali": {
        "Amelie": 5, "La La Land": 5, "The Notebook": 5, "Little Women": 5,
        "Your Name": 5, "Weathering With You": 5, "Spirited Away": 5, "Ponyo": 5,
        "Hidden Figures": 5, "The Farewell": 5, "Arrival": 5, "The Theory of Everything": 5,
        "Pride and Prejudice": 5, "Coco": 5, "Inside Out": 5, "Soul": 5, "Titanic": 5
    },
    "Raj": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "The Dark Knight": 5,
        "Fight Club": 5, "John Wick": 5, "Tenet": 5, "Avatar": 5, "Avengers: Endgame": 5,
        "Joker": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5, "Gladiator": 5, "The Godfather": 5,
        "Parasite": 5, "Vikram": 5, "RRR": 5, "Baahubali": 5, "KGF": 5
    },
    "Isha": {
        "Little Women": 5, "La La Land": 5, "The Notebook": 5, "Amelie": 5,
        "Your Name": 5, "Weathering With You": 5, "Spirited Away": 5, "Ponyo": 5,
        "Hidden Figures": 5, "The Pursuit of Happyness": 5, "The Farewell": 5, "Arrival": 5,
        "The Theory of Everything": 5, "Titanic": 5, "Coco": 5, "Inside Out": 5, "Soul": 5
    },
    "Saurabh": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "The Dark Knight": 5,
        "Fight Club": 5, "John Wick": 5, "Tenet": 5, "Avatar": 5, "Avengers: Endgame": 5,
        "Joker": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5, "Gladiator": 5, "The Godfather": 5,
        "Parasite": 5, "RRR": 5, "KGF": 5, "Baahubali": 5, "Vikram": 5
    },
    "Khushi": {
        "Your Name": 5, "Weathering With You": 5, "Spirited Away": 5, "Ponyo": 5,
        "Amelie": 5, "La La Land": 5, "The Notebook": 5, "Little Women": 5,
        "Hidden Figures": 5, "The Pursuit of Happyness": 5, "The Theory of Everything": 5,
        "Arrival": 5, "The Farewell": 5, "Coco": 5, "Inside Out": 5, "Soul": 5,
        "Titanic": 5, "Pride and Prejudice": 5
    },
    "Nikhil": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "The Dark Knight": 5,
        "Fight Club": 5, "John Wick": 5, "Tenet": 5, "Avatar": 5, "Avengers: Endgame": 5,
        "Joker": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5, "Gladiator": 5, "The Godfather": 5,
        "Parasite": 5, "RRR": 5, "KGF": 5, "Baahubali": 5, "Vikram": 5
    },
    "Tanya": {
        "Your Name": 5, "Weathering With You": 5, "Spirited Away": 5, "Ponyo": 5,
        "Amelie": 5, "La La Land": 5, "The Notebook": 5, "Little Women": 5,
        "Hidden Figures": 5, "The Pursuit of Happyness": 5, "The Theory of Everything": 5,
        "Arrival": 5, "The Farewell": 5, "Coco": 5, "Inside Out": 5, "Soul": 5,
        "Titanic": 5, "Pride and Prejudice": 5
    },
    "Meera": {
        "Inception": 5, "Interstellar": 5, "The Matrix": 5, "The Dark Knight": 5,
        "Fight Club": 5, "John Wick": 5, "Tenet": 5, "Avatar": 5, "Avengers: Endgame": 5,
        "Joker": 5, "Mad Max: Fury Road": 5, "Pulp Fiction": 5, "Gladiator": 5, "The Godfather": 5,
        "Parasite": 5, "RRR": 5, "KGF": 5, "Vikram": 5, "Baahubali": 5
    }
}


current_user = None

def show_frame(frame):
    for f in (login_frame, signup_frame, app_frame):
        f.pack_forget()
    frame.pack(fill=tk.BOTH, expand=True)

# Sign Up
def signup():
    entry_new_user.delete(0, tk.END)
    entry_new_pass.delete(0, tk.END)
    text_movies.delete("1.0", tk.END)
    show_frame(signup_frame)

def submit_signup():
    new_user = entry_new_user.get().strip()
    new_pass = entry_new_pass.get().strip()
    if not new_user or not new_pass:
        messagebox.showerror("Error", "Please enter both username and password.")
        return
    if new_user in user_credentials:
        messagebox.showerror("Error", "Username already exists.")
        return

    movie_entries = text_movies.get("1.0", tk.END).strip().split("\n")
    user_movies = {}
    for line in movie_entries:
        if not line.strip():
            continue
        try:
            movie, rating = line.split(":")
            user_movies[movie.strip()] = int(rating.strip())
        except:
            messagebox.showerror("Error", f"Invalid format: {line}\nUse Movie: Rating")
            return

    user_credentials[new_user] = new_pass
    users[new_user] = user_movies
    messagebox.showinfo("Success", "✅ Account created successfully! Please log in.")
    show_frame(login_frame)

# Login
def login():
    global current_user
    user_name = entry_user.get().strip()
    password = entry_pass.get().strip()

    if user_name in user_credentials and user_credentials[user_name] == password:
        current_user = user_name
        label_welcome.config(text=f"🎉 Welcome, {current_user}!")
        recommendations_text.delete("1.0", tk.END)
        show_frame(app_frame)
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Logout
def logout():
    global current_user
    current_user = None
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    show_frame(login_frame)

# Add watched movies for existing user
def add_watched_movies():
    movie_entries = simpledialog.askstring(
        "Add Watched Movies",
        "Enter movies in 'Movie: Rating' format, separated by new lines:"
    )
    if not movie_entries:
        return
    lines = movie_entries.strip().split("\n")
    for line in lines:
        try:
            movie, rating = line.split(":")
            users[current_user][movie.strip()] = int(rating.strip())
        except:
            messagebox.showerror("Error", f"Invalid format in: {line}\nUse: Movie: Rating")
            return
    messagebox.showinfo("Success", "✅ Movies added successfully!")

# Recommendation logic
def recommend_movies_collaborative():
    recommendations_text.delete("1.0", tk.END)
    recommendations_text.insert(tk.END, f"🎬 Recommendations for {current_user}:\n\n")
    user_ratings = users.get(current_user, {})
    scores = {}

    for other_user, other_ratings in users.items():
        if other_user == current_user:
            continue
        for movie, rating in other_ratings.items():
            if movie not in user_ratings:
                scores[movie] = scores.get(movie, 0) + rating

    if scores:
        recommended_movies = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:7]
        for movie, score in recommended_movies:
            recommendations_text.insert(tk.END, f"✅ {movie} (Score: {score})\n")
    else:
        recommendations_text.insert(tk.END, "😕 No new recommendations found.")

# UI setup
root = tk.Tk()
root.title("🎥 Movie Recommender")
root.geometry("650x600")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# Login Frame
login_frame = tk.Frame(root, bg="#f0f4f7")
tk.Label(login_frame, text="🎥 Movie Recommender", font=("Helvetica", 22, "bold"), bg="#f0f4f7").pack(pady=20)
frame_login_entries = tk.Frame(login_frame, bg="#f0f4f7")
frame_login_entries.pack()
tk.Label(frame_login_entries, text="Username:", font=("Arial", 14), bg="#f0f4f7").grid(row=0, column=0, pady=10, padx=5)
entry_user = tk.Entry(frame_login_entries, font=("Arial", 14))
entry_user.grid(row=0, column=1, pady=10, padx=5)
tk.Label(frame_login_entries, text="Password:", font=("Arial", 14), bg="#f0f4f7").grid(row=1, column=0, pady=10, padx=5)
entry_pass = tk.Entry(frame_login_entries, font=("Arial", 14), show="*")
entry_pass.grid(row=1, column=1, pady=10, padx=5)
tk.Button(login_frame, text="🔐 Login", font=("Arial", 14), bg="#007acc", fg="white", width=20, command=login).pack(pady=10)
tk.Button(login_frame, text="🆕 Sign Up", font=("Arial", 14), bg="#28a745", fg="white", width=20, command=signup).pack()

# Signup Frame
signup_frame = tk.Frame(root, bg="#f0f4f7")
tk.Label(signup_frame, text="🆕 Create Account", font=("Helvetica", 20, "bold"), bg="#f0f4f7").pack(pady=20)
frame_signup_entries = tk.Frame(signup_frame, bg="#f0f4f7")
frame_signup_entries.pack()
tk.Label(frame_signup_entries, text="New Username:", font=("Arial", 14), bg="#f0f4f7").grid(row=0, column=0, pady=5, padx=5)
entry_new_user = tk.Entry(frame_signup_entries, font=("Arial", 14))
entry_new_user.grid(row=0, column=1, pady=5, padx=5)
tk.Label(frame_signup_entries, text="New Password:", font=("Arial", 14), bg="#f0f4f7").grid(row=1, column=0, pady=5, padx=5)
entry_new_pass = tk.Entry(frame_signup_entries, font=("Arial", 14), show="*")
entry_new_pass.grid(row=1, column=1, pady=5, padx=5)
tk.Label(signup_frame, text="Enter watched movies (Movie: Rating) each on a new line:", bg="#f0f4f7", font=("Arial", 12)).pack(pady=5)
text_movies = tk.Text(signup_frame, font=("Arial", 12), height=8, width=50)
text_movies.pack()
tk.Button(signup_frame, text="✅ Submit", font=("Arial", 14), bg="#007acc", fg="white", width=20, command=submit_signup).pack(pady=10)
tk.Button(signup_frame, text="🔙 Back to Login", font=("Arial", 14), bg="#dc3545", fg="white", width=20, command=lambda: show_frame(login_frame)).pack()

# App Frame
app_frame = tk.Frame(root, bg="#f0f4f7")
label_welcome = tk.Label(app_frame, text="", font=("Helvetica", 20, "bold"), bg="#f0f4f7")
label_welcome.pack(pady=20)
recommendations_text = tk.Text(app_frame, font=("Arial", 12), height=18, wrap=tk.WORD, bg="white")
recommendations_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
tk.Button(app_frame, text="🎯 Generate Recommendations", font=("Arial", 14), bg="#28a745", fg="white", width=25, command=recommend_movies_collaborative).pack(pady=5)
tk.Button(app_frame, text="📽️ Add Watched Movies", font=("Arial", 14), bg="#17a2b8", fg="white", width=25, command=add_watched_movies).pack(pady=5)
tk.Button(app_frame, text="🚪 Logout", font=("Arial", 14), bg="#dc3545", fg="white", width=25, command=logout).pack(pady=5)

# Start on Login Frame
show_frame(login_frame)
root.mainloop()