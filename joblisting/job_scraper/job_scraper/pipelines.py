import mysql.connector
from datetime import datetime
from scrapy.exceptions import DropItem

class MySqlPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="joblisting_db",
            port="3306"
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            # Format the posted_date correctly
            posted_date = item['posted_date']
            formatted_date = datetime.strptime(posted_date, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
            
            # Insert data into api_job table excluding id (auto-increment)
            self.cursor.execute(
                "INSERT INTO api_job (title, company, location, employment_type, posted_date, description) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    item['title'],
                    item['company'],
                    item['location'],
                    item['employment_type'],
                    formatted_date,
                    item['description']
                )
            )
            self.connection.commit()
        except mysql.connector.Error as err:
            spider.log(f"Failed to insert item into database: {err}")
            spider.log(item)
            raise DropItem(f"Failed to insert item into database: {item}")

        return item
