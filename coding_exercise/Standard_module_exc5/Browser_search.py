import webbrowser

search = input("Enter search content: ").replace(" ", "+")
url = f"https://www.google.com/search?q={search}"
webbrowser.open(url)