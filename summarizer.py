import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Load summarization model

summarizer = pipeline(
"summarization",
model="facebook/bart-large-cnn"
)

print("Summarizer loaded successfully!")

# Function to extract article text

def extract_article(url):
response = requests.get(url, timeout=20)
response.raise_for_status()

```
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

article_text = ""

for paragraph in paragraphs:
    article_text += paragraph.get_text(strip=True) + "\n"

return article_text
```

# Function to summarize an article

def summarize_article(text):
return summarizer(
text[:3000],
max_length=180,
min_length=80,
do_sample=False
)[0]["summary_text"]

# CISA Article

cisa_url = "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a"

cisa_text = extract_article(cisa_url)
cisa_summary = summarize_article(cisa_text)

print("\n===== CISA ARTICLE SUMMARY =====\n")
print(cisa_summary)

# Microsoft Article

microsoft_url = "https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/"

microsoft_text = extract_article(microsoft_url)
microsoft_summary = summarize_article(microsoft_text)

print("\n===== MICROSOFT ARTICLE SUMMARY =====\n")
print(microsoft_summary)

# Cisco Article

cisco_url = "https://blogs.cisco.com/security/inside-the-soc-ai-powered-dns-defense-against-ransomware"

cisco_text = extract_article(cisco_url)
cisco_summary = summarize_article(cisco_text)

print("\n===== CISCO ARTICLE SUMMARY =====\n")
print(cisco_summary)

