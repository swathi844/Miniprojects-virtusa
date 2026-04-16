import re

posts = [
    "User123: I hate this bad app http://test.com",
    "User456: This is a good platform",
    "User123: Such a toxic site visit http://example.com",
    "User789: I love this app",
    "User456: bad experience with this http://badlink.com"
]

banned_words = ["bad", "toxic", "hate"]
LINKS_FILE = "links_found.txt"

def mask_banned_words(text, banned):
    pattern = re.compile(r"\b(" + "|".join(re.escape(word) for word in banned) + r")\b", re.IGNORECASE)
    return pattern.sub("***", text)


def extract_links(text):
    return re.findall(r"https?://\S+", text)


def sanitize_post(post):
    username, message = post.split(":", 1)
    username = username.strip()
    message = message.strip()
    cleaned_message = mask_banned_words(message, banned_words)
    links = extract_links(cleaned_message)
    flagged = cleaned_message != message
    return username, cleaned_message, links, flagged


def save_links(links, filename=LINKS_FILE):
    with open(filename, "w", encoding="utf-8") as output:
        output.write("\n".join(links))


def main():
    links_found = []
    user_flags = {}
    cleaned_count = 0
    blocked_count = 0

    for post in posts:
        user, cleaned_message, links, flagged = sanitize_post(post)
        links_found.extend(links)

        if flagged:
            cleaned_count += 1
            blocked_count += 1
            user_flags[user] = user_flags.get(user, 0) + 1
        else:
            user_flags.setdefault(user, 0)

        print(f"{user}: {cleaned_message}")

    save_links(links_found)

    print(f"\nTotal posts processed: {len(posts)} | Cleaned: {cleaned_count} | Blocked: {blocked_count}")
    print("User flag summary:", user_flags)


if __name__ == "__main__":
    main()
