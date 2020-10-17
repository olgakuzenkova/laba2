#!/usr/bin/env python
from __future__ import unicode_literals

import os
import io
from setuptools import setup, find_packages


def gzip_language_data(root, source):
    print("Compressing language data")
    import gzip
    from pathlib import Path

    base = Path(root) / source
    for jsonfile in base.glob("**/*.json"):
        outfile = jsonfile.with_suffix(jsonfile.suffix + ".gz")
        if outfile.is_file() and outfile.stat().st_mtime > jsonfile.stat().st_mtime:
            print("Skipping {}, already compressed".format(jsonfile))
            continue
        with open(str(jsonfile), 'r', encoding="utf-8") as infileh, gzip.open(str(outfile), 'w') as outfileh:
            outfileh.write(infileh.read().encode("utf-8"))
        print("Compressed {}".format(jsonfile))


def setup_package():
    package_name = "spacy_lookups_data"
    root = os.path.abspath(os.path.dirname(__file__))

    about_path = os.path.join(root, package_name, "about.py")
    with io.open(about_path, encoding="utf8") as f:
        about = {}
        exec(f.read(), about)

    if not os.path.exists(os.path.join(root, "PKG-INFO")):
        gzip_language_data(root, "spacy_lookups_data/data")

    setup(name=package_name, version=about["__version__"], packages=find_packages())


if __name__ == "__main__":
    setup_package()

import re
import gensim
from gensim.models import word2vec
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings

warnings.filterwarnings('ignore')

#import spacy



with open ('laba2.txt', encoding='utf-8')as f:
    lines = f.readlines()
    texts=lines[6::7]
    for text in texts:
        text = text.lower()
        text = re.sub(r'[^а-яёА-ЯЁa-zA-Z ]', '', text)
    texts_dict = {}
    for i in texts:
        sim = texts[i].similarity(text[i+1])
        texts_dict.update(sim, [texts[i], texts[i+1]])
    sims = list(text_dict.keys())
    sims = sims.sort()
        

