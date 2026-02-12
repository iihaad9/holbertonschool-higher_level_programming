#!/usr/bin/python3
import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    r = requests.get(URL, timeout=10)
    print(f"Status Code: {r.status_code}")
    if r.status_code != 200:
        return

    for post in r.json():
        print(post.get("title", ""))


def fetch_and_save_posts():
    r = requests.get(URL, timeout=10)
    if r.status_code != 200:
        return

    posts = [
        {"id": p.get("id"), "title": p.get("title"), "body": p.get("body")}
        for p in r.json()
    ]

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts)
