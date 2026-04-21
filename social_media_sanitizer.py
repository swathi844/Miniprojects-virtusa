


posts = [
    "User123: I hate this bad app http://test.com",
    "User456: This is a good platform",
    "User123: Such a toxic site visit http://example.com",
    "User789: I love this app",
    "User456: bad experience with this http://badlink.com"
]


banned_words = ["bad", "toxic", "hate"]


links_found = []


user_flags = {}


total_posts = len(posts)
cleaned = 0
blocked = 0


for post in posts:

    
    user = post.split(":")[0]
    text = post

    flagged = False

    
    for word in banned_words:
        if word in text:
            text = text.replace(word, "***")
            flagged = True

    
    if flagged:
        cleaned += 1
        blocked += 1
        user_flags[user] = user_flags.get(user, 0) + 1
    else:
        user_flags[user] = user_flags.get(user, 0)

    
    words = text.split()
    for w in words:
        if w.startswith("http"):
            links_found.append(w)

    
    print(text)


with open("links_found.txt", "w") as file:
    for link in links_found:
        file.write(link + "\n")


print(f"\nTotal Posts Screened: {total_posts} | Cleaned: {cleaned} | Blocked: {blocked}")
print("User Flag Summary:", user_flags)