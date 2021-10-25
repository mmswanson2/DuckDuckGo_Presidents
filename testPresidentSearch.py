import pytest
import requests

url_ddg = "https://api.duckduckgo.com"

president_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe",
              "Jackson", "Van Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore",
              "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
              "Garfield", "Arthur", "Harrison", "Cleveland", "McKinley", "Roosevelt",
              "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
              "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan",
              "Bush", "Clinton", "Obama", "Trump"]


def test_president_list():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data['RelatedTopics']

    matches = []

    for president in president_list:
        for topic in related_topics:
            if president in topic['Text']:
                matches.append(president)
                break

    assert len(matches) == 40
