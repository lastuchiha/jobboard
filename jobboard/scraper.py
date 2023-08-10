import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
from datetime import datetime
from typing import List


def jobscraper(total_pages: int = 1) -> List:
    """
    Scraper function that takes the number of pages to scrape as input and returns the scraped results
    """
    results = []

    session = requests.Session()
    for page_num in range(1, total_pages + 1):
        page = {"pageNum": 0, "jobDetails": [], "elapsedTime": "0s"}

        url = "https://www.fresheroffcampus.com/page/{0}/".format(page_num)

        start_time = time.time()
        response = session.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        jobs = soup.find_all("article")

        for job in jobs:
            job_page_url = job.find("a").get("href")
            slug = urlparse(job_page_url).path.strip("/")
            posted_at = job.find("time").text.strip()
            image_url = job.find(
                "img", {"class": "attachment-thumbnail size-thumbnail wp-post-image"}
            ).get("src")
            response = session.get(job_page_url)
            soup = BeautifulSoup(response.text, "html.parser")
            page_title = soup.find("h1", {"class": "page-title"}).text.strip()
            org_url = soup.find("a", {"rel": "noreferrer noopener"}).get("href")
            page["jobDetails"].append(
                {
                    "title": page_title,
                    "slug": slug,
                    "url": org_url,
                    "imageUrl": image_url,
                    "posted_at": datetime.strptime(posted_at, "%B %d, %Y").date(),
                }
            )

        end_time = time.time()
        elapsed_time = end_time - start_time
        page["pageNum"] = page_num
        page["elapsedTime"] = f"{elapsed_time:.5f}s"

        results.append(page)
    return results


if __name__ == "__main__":
    print(scraper(1))
