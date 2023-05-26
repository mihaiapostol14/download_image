from icrawler.builtin import GoogleImageCrawler
import os
from PIL import Image

dir_name = input('Enter dir name: \n')
keyword = input('Enter keyword: \n')
max_num = int(input('Enter max num downloading photo: \n'))

def download_image():
    # todo: This statement will be to create folder if she was not created
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    google_crawler = GoogleImageCrawler(storage={'root_dir': f'{dir_name}'})
    google_crawler.crawl(keyword=keyword, max_num=max_num)

    if os.path.exists(dir_name):
        os.listdir(dir_name)

def main():
    download_image()

if __name__ == '__main__':
    main()