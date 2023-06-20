import os

from icrawler.builtin import GoogleImageCrawler

keyword = input('Enter keyword: \n')
max_num = int(input('Enter max num downloading photo: \n'))
path_download = os.path.join('C:', 'Users', os.getlogin(), 'Downloads')


def download_image():
    # todo: This statement will be to create folder if she was not created
    if not os.path.exists(f'{path_download}/{keyword}'):
        os.mkdir(f'{path_download}/{keyword}')

    google_crawler = GoogleImageCrawler(storage={'root_dir': f'{path_download}/{keyword}'})
    google_crawler.crawl(keyword=keyword, max_num=max_num)

    if os.path.exists(keyword):
        os.listdir(keyword)


def main():
    download_image()


if __name__ == '__main__':
    main()
