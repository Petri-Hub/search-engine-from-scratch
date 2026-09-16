<h1 align="center">🔎 search-engine-from-scratch</h1>

<br>

<h3 align="center">A search engine written by hand in Python.<br>The crawler got written, the index never did</h3>

<p align="center">
  <img alt="Top language" src="https://img.shields.io/github/languages/top/Petri-Hub/search-engine-from-scratch" /> <a href="https://github.com/Petri-Hub/search-engine-from-scratch/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/Petri-Hub/search-engine-from-scratch" /></a>
</p>

<br>

## About

> **TL;DR:** I solve ARG puzzles and ciphers for fun, and the tools for them are spread across many sites. The idea was to crawl those sites and search them from one place, writing each stage myself instead of reaching for a crawling or search library. It stopped after the crawler.

## What's inside

```sh
└── src
    ├── crawler.py  # walks pages from a set of seeds, following links it hasn't visited yet
    ├── main.py     # starts a crawl from dcode.fr
    └── models.py   # the page record: id, url, title, contents and links
```

## Technologies

<table align="center">
  <tr>
    <td align="center" width="96"><img src="https://cdn.simpleicons.org/python" width="48" height="48" alt="Python" /><br>Python</td>
  </tr>
</table>
