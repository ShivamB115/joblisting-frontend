import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector

class JobsSpider(scrapy.Spider):
    name = "jobs"

    def __init__(self, *args, **kwargs):
        super(JobsSpider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # Use the correct path to the new ChromeDriver
        self.driver = webdriver.Chrome(service=Service('C:/Users/ST/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'), options=chrome_options)

    def start_requests(self):
        url = "https://www.dice.com/jobs"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.driver.get(response.url)
        selenium_response = Selector(text=self.driver.page_source)

        # Use correct CSS selectors based on the provided HTML structure
        job_containers = selenium_response.css('div.card.search-card')

        if not job_containers:
            self.log("No job containers found. Check the response body to verify the content.")

        for job in job_containers:
            title = job.css('a.card-title-link::text').get()
            company = job.css('a[data-cy="search-result-company-name"]::text').get()
            location = job.css('span.search-result-location::text').get()
            employment_type = job.css('span[data-cy="search-result-employment-type"]::text').get()
            description = job.css('div[data-cy="card-summary"]::text').get()

            self.log(f"Job Title: {title}")
            self.log(f"Company: {company}")
            self.log(f"Location: {location}")
            self.log(f"Employment Type: {employment_type}")
            self.log(f"Description: {description}")

            job_item = {
                "title": title.strip() if title else "Unknown",
                "company": company.strip() if company else "Unknown Company",
                "location": location.strip() if location else "Unknown Location",
                "employment_type": employment_type.strip() if employment_type else "Unknown",
                "posted_date": "2024-12-21T00:00:00Z",  # Example value; update as needed
                "description": description.strip() if description else "Job description placeholder"
            }

            yield job_item

    def closed(self, reason):
        self.driver.quit()
