# Evaluation of Security Article Summaries

## Overview

The summarizer was tested on three cybersecurity articles from CISA, Microsoft Security, and Cisco Security Blog. The BART transformer model (`facebook/bart-large-cnn`) was used to generate abstractive summaries.

## Comparison

| Article   | Main Threat/Topic Preserved | Important Details | Conciseness | Overall Usefulness |
| --------- | --------------------------- | ----------------- | ----------- | ------------------ |
| CISA      | Yes                         | Good              | Good        | High               |
| Microsoft | Yes                         | Good              | Good        | High               |
| Cisco     | Yes                         | Good              | Good        | High               |

## 1. CISA Article

The generated summary correctly identified the red team assessment and explained that the organization was compromised because of insufficient detection and response controls. It preserved the main cybersecurity lesson of the advisory.

**Accuracy:** High
**Usefulness:** High

## 2. Microsoft Article

The generated summary correctly identified Storm-2945, traffic manipulation attacks, adversary-in-the-middle phishing, Microsoft Entra ID, and malware delivery. These are important technical details from the original article.

**Accuracy:** High
**Usefulness:** High

## 3. Cisco Article

The generated summary correctly described Cisco's AI-powered DNS defense platform, Cisco Talos intelligence, DNS security, DGA analysis, malicious-domain detection, and ransomware protection.

**Accuracy:** High
**Usefulness:** High

## Overall Evaluation

The BART model successfully reduced long cybersecurity articles into shorter summaries while preserving their main topics and important security information. The summaries are useful for quickly understanding the purpose and major findings of each article.

However, abstractive summarization can sometimes omit smaller technical details from the original article. For security reports, important indicators such as CVE numbers, IP addresses, domains, and specific mitigation steps should therefore be checked against the original source.

## Conclusion

The results show that transformer-based abstractive summarization can be useful for creating quick security briefs. The system provides concise summaries while retaining the main cybersecurity context across all three tested articles.
