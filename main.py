import os

from icrawler.builtin import GoogleImageCrawler

class GoogleImageDownloader:
    def __init__(self, search_image='', max_num=0):
        self.search_image = search_image
        self.max_num = max_num

        self.download_image()
        self.count_image()


    def download_image(self):
        # TODO: This statement will be to create folder if she was not created
        if not os.path.exists(f'{self.search_image}'):
            os.mkdir(self.search_image)

        google_crawler = GoogleImageCrawler(storage={'root_dir': f'{self.search_image}'})
        google_crawler.crawl(keyword=self.search_image, max_num=self.max_num)


    def directory_exists(self, directory_name=''):
            try:
                exist = True
                if os.path.exists(directory_name):
                    return exist

            except (FileNotFoundError,FileExistsError):
                exist = False
            return exist

    def count_image(self):
        if self.directory_exists(directory_name=self.search_image):
            print(f'Count image {self.search_image} is {len(os.listdir(self.search_image))}')


    def open_output_directory(self):
        if self.directory_exists(directory_name=self.search_image):
            os.startfile(self.search_image)



def main():
    return GoogleImageDownloader(    
    search_image=input('Enter name search image: \n'),
    max_num=int(input('Enter max number downloading image: \n'))
    )


if __name__ == '__main__':
    main()
