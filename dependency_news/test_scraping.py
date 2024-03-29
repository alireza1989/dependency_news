import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def strip_to_max_words(text, num_words):
    words = text.split()
    stripped_text = " ".join(words[:num_words])
    return stripped_text


def generate_summary(text: str) -> str:
    try:
        message = [
            {
                "role": "system",
                "content": "You are a senior software engineer who is in charge of summarizing the release notes of python packages from their github release note page.",
            },
            {
                "role": "user",
                "content": f"This is the text I got from the python package release notes page.  Summerize it with the key information in a nice format. Make sure the version of the release is added at the begining of the summary: \n {text}",
            },
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the GPT-3.5 Turbo model
            messages=message,
            temperature=0.8,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        content = response.choices[0].message.content
        return content

    except Exception as e:
        print(f"An error occurred: {e}")


def generate_md_notes(text: str) -> str:

    md_note_template = """ # Release Notes for [Project Name] [Version]\n\n## Release Date\n[Release Date, 
    e.g., 2024-03-10]\n\n## Overview\nA brief overview of the major highlights in this release and any significant changes or improvements that users should be aware of.\n\n
    ## What's New\nHighlight the new features and updates introduced in this release. Provide a short description for each item.\n\n
    - **Feature 1:** Description of feature 1.\n- **Feature 2:** Description of feature 2.\n- **Feature 3:** Description of feature 3.\n\n
    ## Improvements\nDiscuss the improvements made to existing features, performance enhancements, and other optimizations.\n\n
    - **Improvement 1:** Description of improvement 1.\n- **Improvement 2:** Description of improvement 2.\n- **Improvement 3:** Description of improvement 3.\n\n
    ## Bug Fixes\nList the bugs that have been fixed in this release. Include a brief description of the fix and, if applicable, the issue number.\n\n
    - **Bug 1:** Description of bug fix 1. (Issue #123)\n- **Bug 2:** Description of bug fix 2. (Issue #456)\n"""

    try:
        message = [
            {
                "role": "system",
                "content": f"You are a senior software engineer who is in charge of summarizing the release notes of python packages. You are given the summarized notes an need to put them into a markdown files using this template and if the information does not exists do not add the section in the template to the markdown file \n {md_note_template}",
            },
            {
                "role": "user",
                "content": f"This is the summarized release notes. Put them into markdown file and preseve the URIs: \n {text}",
            },
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the GPT-3.5 Turbo model
            messages=message,
            temperature=0.8,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        content = response.choices[0].message.content
        return content

    except Exception as e:
        print(f"An error occurred: {e}")


def scrape_latest_release_notes(url: str = None):
    """Scrape the latest release notes from a GitHub repository's releases page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the release notes section - GitHub's structure may change, so this might need updates
        # As of now, release notes might be contained in divs with markdown bodies
        version_element = soup.find(
            "h1", class_="d-inline mr-3", attrs={"data-view-component": "true"}
        )

        # Access the text content of the element
        version_content = "Version element does not exist."
        if version_element:
            version_content = version_element.text.strip()
        else:
            print("Element not found")

        notes_section = soup.find("div", class_="markdown-body")
        if notes_section:
            release_notes = (
                f"The version is: {version_content}"
                + notes_section.get_text(strip=True)
            )
            return release_notes
        else:
            return "Release notes not found."

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


data_file_path = os.path.dirname(__file__) + "/repos.json"

with open(data_file_path, "r") as file:
    repos = json.load(file)

MAX_NUM_WORDS = 500
print(repos)
for repo in repos:
    owner = repo["owner"]
    repo = repo["repo"]

    url = f"https://github.com/{owner}/{repo}/releases/latest"

    latest_release_notes = scrape_latest_release_notes(url)
    latest_release_notes = strip_to_max_words(latest_release_notes, MAX_NUM_WORDS)
    summary = generate_summary(latest_release_notes)
    summary = f"Reepository owner: {owner} \n" + f"The repository: {repo} \n" + summary
    md_file_content = generate_md_notes(summary)

    md_file_path = Path(f"dependency_repo/{owner}_{repo}.md")
    absolute_path = md_file_path.resolve()

    with open(md_file_path, "w") as md_file:
        md_file.write(md_file_content)
