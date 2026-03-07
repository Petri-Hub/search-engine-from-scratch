from types import Page


class Crawler:
    seeds: list[str]
    frontier: set[str] = set()
    visited: set[str] = set()
    crawled: list[Page] = []
    max_pages: int

    def __init__(self, seeds, max_pages):
        self.seeds = seeds
        self.max_pages = max_pages

    def crawl(self):
        while self.should_continue_crawling():
            print("Crawling...")

    def should_continue_crawling(self) -> bool:
        return self.frontier and self.did_visit_max_pages_amount()

    def did_visit_max_pages_amount(self) -> bool:
        return self.get_visited_pages_amount() >= self.get_max_pages_amount()

    def get_seeds(self) -> list[str]:
        return self.seeds

    def get_visited_pages_amount(self) -> int:
        return len(self.visited)

    def get_max_pages_amount(self) -> int:
        return self.max_pages
