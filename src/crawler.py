import requests
import uuid

from urllib.parse import urljoin
from models import Page
from bs4 import BeautifulSoup

class Crawler:
    frontier: set[str] = set()
    visited: set[str] = set()
    crawled: list[Page] = []
    max_pages: int

    def __init__(self, seeds: set[str], max_pages=5):
        self.frontier = seeds
        self.max_pages = max_pages

    def crawl(self):
        print("[Crawler] Starting crawl process...")

        while self.should_continue_crawling():

            url = self.get_url_to_crawl_from_frontier()
            print(f" [Crawler] Crawling URL: {url}")

            response = self.request_page_source(url)
            print(f"  [Crawler] Received response status: {response.status_code}")

            success = self.is_successfull_status_code(response.status_code)
            print(f"  [Crawler] Was crawl successfull: {success}")

            if not success:
                continue

            soup = self.convert_response_body_into_html_soup(response.content)
            print("  [Crawler] Sucessfully converted HTML into Beatiful Soup")

            title = self.extract_page_title_from_html(soup)
            print(f"  [Crawler] Got title: {title}")

            links = self.extract_page_links_from_html(url, soup)
            print(f"  [Crawler] Extracted {len(links)} links from page")

            page = Page(
                id=uuid.uuid4(),
                url=url,
                title=title,
                contents=response.content,
                links=links,
            )

            self.mark_page_as_visited(page)
            self.add_links_to_be_crawled(page)

    def add_links_to_be_crawled(self, page: Page) -> None:
        for link in page.links:
            if link not in self.visited:
                self.frontier.add(link)

    def extract_page_links_from_html(self, url: str, soup: BeautifulSoup) -> set[str]:
        return {
            urljoin(url, href)
            for href in self.get_all_anchors_urls_from_html(soup)
            if self.is_href_to_another_page(href)
        }

    def is_href_to_another_page(self, href: str) -> bool:
        return href and not href.startswith(("#", "mailto", "javascript"))

    def get_all_anchors_urls_from_html(self, soup: BeautifulSoup):
        return [anchor.get("href") for anchor in soup.find_all("a")]

    def extract_page_title_from_html(self, soup: BeautifulSoup) -> str:
        return soup.title.string

    def convert_response_body_into_html_soup(self, html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")

    def mark_page_as_visited(self, page: Page) -> None:
        self.crawled.append(page)
        self.visited.add(page.url)

    def request_page_source(self, url: str) -> requests.Response:
        return requests.get(
            url,
            headers={
                "User-Agent": "Petri-Hub-Crawler/0.1",
                "Accept": "text/html",
                "Accept-Language": "en-US,en;q=0.9",
            },
        )

    def is_successfull_status_code(self, status_code: int) -> bool:
        return status_code >= 200 and status_code <= 299

    def get_url_to_crawl_from_frontier(self) -> str:
        return self.frontier.pop()

    def should_continue_crawling(self) -> bool:
        return self.has_pages_to_crawl() and not self.did_visit_max_pages_amount()

    def has_pages_to_crawl(self) -> bool:
        return len(self.frontier) > 0

    def did_visit_max_pages_amount(self) -> bool:
        return self.get_visited_pages_amount() >= self.get_max_pages_amount()

    def get_visited_pages_amount(self) -> int:
        return len(self.visited)

    def get_max_pages_amount(self) -> int:
        return self.max_pages

    def get_visited(self) -> set[str]:
        return self.visited

    def get_crawled(self) -> set[Page]:
        return self.crawled
