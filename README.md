# AI Cybersecurity Article Summarizer

**Internship Task 1 — AI/ML Track**

## Project Overview

This project is an AI-powered cybersecurity article summarizer developed using Python and Hugging Face Transformers.

The system takes cybersecurity articles from trusted security sources and uses a transformer-based AI model to generate concise summaries of the original articles.

## Objectives

* Collect cybersecurity articles from trusted cybersecurity sources.
* Extract and process article text using Python.
* Use an AI summarization model to generate concise summaries.
* Compare original articles with generated summaries.
* Demonstrate the use of Natural Language Processing (NLP) for cybersecurity content.

## Technologies Used

* Python
* Google Colab
* Hugging Face Transformers
* PyTorch
* BeautifulSoup
* Requests

## AI Model

The project uses:

**Model:** `facebook/bart-large-cnn`

BART is a transformer-based sequence-to-sequence model that can be used for abstractive text summarization.

## Articles Used

### 1. CISA

**Title:** Enhancing Cyber Resilience: Insights from CISA Red Team Assessment of a US Critical Infrastructure Sector Organization

**Source:** Cybersecurity and Infrastructure Security Agency (CISA)

**Article:** https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-326a

**Generated Summary:**

The Cybersecurity and Infrastructure Security Agency (CISA) conducted a red team assessment at the request of a critical infrastructure organization. The red team was able to compromise the organization's domain and sensitive business systems because of insufficient controls to detect and respond to malicious activities. The findings provide lessons for network defenders and software manufacturers to reduce cybersecurity risks.

---

### 2. Microsoft Security Blog

**Title:** CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft

**Source:** Microsoft Security Blog

**Date:** July 31, 2026

**Article:** https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/

**Generated Summary:**

Microsoft has observed Storm-2945, a sub-cluster of Midnight Blizzard, conducting widespread but targeted traffic manipulation attacks involving hospitality sector networks. A portion of this activity uses doppelganger domains that mimic Microsoft online services for adversary-in-the-middle phishing attacks and abuse the Microsoft Entra ID device code authentication flow. Microsoft also identified traffic manipulation attacks leading to malware delivery on affected systems.

---

### 3. Cisco Security Blog

**Title:** Inside the SOC: AI-powered DNS defense against ransomware

**Source:** Cisco Security Blog

**Article:** https://blogs.cisco.com/security/inside-the-soc-ai-powered-dns-defense-against-ransomware

**Generated Summary:**

Cisco introduced an AI-powered DNS defense platform integrated with Cisco Secure Access and powered by Cisco Talos intelligence. Talos DNS Security detects obfuscated data in DNS packets, while AI-driven detection and Domain Generation Algorithm (DGA) analysis help identify and predict malicious domains. The technology provides proactive protection against ransomware and reduces security alert noise for SOC analysts.

## Example

### Original Text

Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These attacks may attempt to access, change, or destroy sensitive information.

### Generated Summary

Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These cyberattacks usually aim to access, change, or destroy sensitive information.

## How It Works

1. The user provides cybersecurity article text.
2. The article text is processed using Python.
3. The text is passed to the BART summarization model.
4. The model identifies the important information and generates a shorter summary.
5. The original article and generated summary can be compared to evaluate the result.

## Output

The system successfully generates concise summaries from cybersecurity articles while preserving the main security-related information.

## Project Structure

```text
AI-Cybersecurity-Article-Summarizer/
│
├── README.md
├── summarizer.py
└── articles/
```

## How to Run

The project can be run easily in Google Colab.

Install the required libraries:

```python
!pip install transformers torch beautifulsoup4 requests
```

Load the summarization model:

```python
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
```

Then provide the article text and generate the summary.

## Conclusion

This project demonstrates how AI and Natural Language Processing can be applied to cybersecurity information. Using the BART transformer model, long cybersecurity articles can be converted into shorter and easier-to-understand summaries while retaining their key information.

## Future Improvements

* Add automatic article extraction from URLs.
* Add support for more cybersecurity sources.
* Compare multiple summarization models.
* Add a simple web interface.
* Evaluate summaries using ROUGE scores.


