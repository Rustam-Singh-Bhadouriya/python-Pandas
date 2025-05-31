import wikipediaapi

# Wikipedia API का object बनाते समय user-agent और language सेट करें
wiki_wiki = wikipediaapi.Wikipedia(
    language='en', 
    user_agent="MyCustomUserAgent/1.0 (https://mywebsite.com)"
)

# Article का नाम
article_name = "Machine learning"

# Article fetch करना
page = wiki_wiki.page(article_name)

# Check if the page exists
if page.exists():
    print(f"Article Title: {page.title}")
    print(f"Article Summary: {page.summary[:]}...") 
else:
    print(f"The article '{article_name}' does not exist on Wikipedia.")

f = open('timestamp.txt', 'a')
f.write(page.summary[:])
