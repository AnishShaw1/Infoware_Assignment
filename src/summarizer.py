from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import sent_tokenize
import numpy as np
from textwrap import shorten
import re

"""def extract_keypoints_and_notes(pages, top_n=8):
    
    #Extracts main ideas from text and builds structured slides.
    #Each slide = title + short note (+ optional bullets)
    
    text = "\n".join(pages)
    sents = [clean_sentence(s) for s in sent_tokenize(text) if len(s.strip()) > 20]

    if not sents:
        return []

    # Compute sentence importance using TF-IDF
    vec = TfidfVectorizer(max_features=2000, stop_words='english')
    X = vec.fit_transform(sents)
    scores = X.sum(axis=1).A1
    idx = np.argsort(scores)[::-1][:top_n]

    slides = []
    for i, k in enumerate(idx):
        main_sent = sents[k]
        headline = shorten_headline(main_sent)
        note = make_summary_line(main_sent)
        bullets = generate_bullets(sents, k)

        slides.append({
            'title': headline,
            'bullets': bullets,
            'note': note
        })

    return slides """


def extract_keypoints_and_notes(pages, top_n=10):
    """
    Extracts topic sections and summaries from a well-structured PDF (like chapters or articles).
    Each slide: section heading + short summary paragraph.
    """
    text = "\n".join(pages)

    # Detect headings like: "1. Introduction", "2. Historical Development", etc.
    sections = re.split(r"\n(?=\d+\.\s+)", text)
    slides = []

    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue

        # Find title (first line, often starts with number + name)
        match = re.match(r"(\d+\.\s*)(.+)", sec)
        if match:
            title = match.group(2).strip()
            # Extract the next few lines or first paragraph
            body = re.split(r"\n", sec, maxsplit=1)
            if len(body) > 1:
                summary_text = body[1].strip()
            else:
                summary_text = ""

            # Clean and trim summary
            summary_text = re.sub(r"\s+", " ", summary_text)
            summary_text = summary_text.split(".")[0] + "."

            slides.append({
                "title": title,
                "note": summary_text,
                "bullets": []  # not used in new design
            })

    # If fewer than desired slides, fallback
    if not slides:
        slides = [{
            "title": "Artificial Intelligence Overview",
            "note": shorten(text, width=250, placeholder="..."),
            "bullets": []
        }]

    # Limit to top_n sections
    return slides[:top_n]

def clean_sentence(s):
    """Remove weird characters and normalize punctuation."""
    s = re.sub(r'\s+', ' ', s)
    s = s.replace('–', '-').replace('—', '-')
    s = s.encode('latin-1', 'ignore').decode('latin-1', 'ignore')
    return s.strip().capitalize()

def shorten_headline(sent, max_words=8):
    words = sent.split()
    headline = " ".join(words[:max_words]).rstrip(",.")
    headline = headline[0].upper() + headline[1:]
    return shorten(headline, width=60, placeholder="...")

def make_summary_line(sent):
    """Creates a short, natural-sounding one-line summary."""
    summary = shorten(sent, width=120, placeholder="...")
    return summary

def generate_bullets(sents, idx, max_bullets=2):
    bullets = []
    for offset in [1, -1, 2, -2]:
        j = idx + offset
        if 0 <= j < len(sents):
            bullets.append(shorten(sents[j], width=100, placeholder="..."))
        if len(bullets) >= max_bullets:
            break
    return bullets
