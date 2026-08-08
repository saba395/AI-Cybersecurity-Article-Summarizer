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
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

```
paragraphs = soup.find_all("p")

article_text = ""

for p in paragraphs:
    article_text += p.get_text() + "\n"

return article_text
```

# CISA Article

cisa_url = "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a"

cisa_text = extract_article(cisa_url)

cisa_summary = summarizer(
cisa_text[:3000],
max_length=180,
min_length=80,
do_sample=False
)

print("\n===== CISA ARTICLE SUMMARY =====\n")
print(cisa_summary[0]["summary_text"])

# Microsoft Article

microsoft_url = "https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/"

microsoft_text = extract_article(microsoft_url)

microsoft_summary = summarizer(
microsoft_text[:3000],
max_length=180,
min_length=80,
do_sample=False
)

print("\n===== MICROSOFT ARTICLE SUMMARY =====\n")
print(microsoft_summary[0]["summary_text"])

# Cisco Article

cisco_url = "https://blogs.cisco.com/security/inside-the-soc-ai-powered-dns-defense-against-ransomware"

cisco_text = extract_article(cisco_url)

cisco_summary = summarizer(
cisco_text[:3000],
max_length=180,
min_length=80,
do_sample=False
)

print("\n===== CISCO ARTICLE SUMMARY =====\n")
print(cisco_summary[0]["summary_text"])

# Simple summarization example

text = """
Cybersecurity is the practice of protecting systems, networks, and programs
from digital attacks. These cyberattacks usually aim to access, change, or
destroy sensitive information, extort money from users, or interrupt normal
business processes. Organizations use firewalls, encryption, multi-factor
authentication, and employee awareness training to reduce cyber risks.
"""

summary = summarizer(
text,
max_length=50,
min_length=20,
do_sample=False
)

print("\n===== EXAMPLE SUMMARY =====\n")
print("Original Text:")
print(text)

print("\nSummary:")
print(summary[0]["summary_text"])
