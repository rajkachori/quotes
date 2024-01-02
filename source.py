import tkinter as tk
import requests

api = "http://api.quotable.io/quotes/random"
quotes = []
quote_number = 0

def preload_quotes():
    global quotes

    print("***Loading more quotes***")
    try:
        # Fetch 10 quotes in a single request
        random_quotes = requests.get(f"{api}?count=10").json()

        for random_quote in random_quotes:
            content = random_quote.get("content", "")
            author = random_quote.get("author", "")
            quote = content + "\n\n" + "By " + author
            print(content)

            quotes.append(quote)

        print("***Finished loading more quotes!***")
        update_quote_label()
    except Exception as e:
        print(f"Error: {e}. Unable to fetch quotes.")

    # Schedule the next update after a delay (e.g., 10 seconds)
    window.after(10000, preload_quotes)

def update_quote_label():
    global quote_label
    global quotes
    global quote_number

    if quote_number < len(quotes):
        quote_label.configure(text=quotes[quote_number])
        quote_number += 1

# Function to initiate the quote loading
def get_random_quote():
    update_quote_label()

# UI
window = tk.Tk()
window.geometry("900x260")
window.title("quote generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="grey")

quote_label = tk.Label(window, text="Click on a button to generate a random!",
                       height=6,
                       pady=10,
                       wraplength=800,
                       font=("Helvetica", 14))
quote_label.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

button = tk.Button(text="Generate", command=get_random_quote, bg="#0052cc", fg="#ffffff",
                   activebackground="grey", font=("Helvetica", 14))
button.grid(row=1, column=0, sticky="WE", padx=20, pady=10)

# Start loading quotes
if __name__ == "__main__":
    preload_quotes()
    window.mainloop()
