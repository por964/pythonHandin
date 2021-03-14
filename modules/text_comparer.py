import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from urllib.parse import urlparse


class TextComparer():

    def __init__(self, url_list=[]):
        self.url_list = url_list
        self.filenames = []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.filenames):
            self.index += 1
            return self.filenames[self.index]
        else:
            raise StopIteration

    def download(self, url):
        res = requests.get(url)
        bookId = url.split('/')[-1]
        filepath = f'data/{bookId}'
        self.filenames.append(filepath)
        try:
            if res.ok:
                with open(filepath, 'wb') as f:
                    for chunk in res.iter_content(chunk_size=1024):
                        f.write(chunk)
                    print(f'{bookId} downloaded to {filepath}...')
                    return filepath

            elif res.status_code == 404:
                raise FileNotFoundError
        except FileNotFoundError as error:
            print('Error: ' + repr(error))

    def multi_download(self):
        workers = len(self.url_list)
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(self.download, self.url_list)
            self.filenames = list(res)
        print(self.filenames)

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        vowels = set("AEIOUaeiou")
        count = 0
        with open(text, 'r') as file_object:
            content = file_object.read()
            words = content.split()
            no_words = len(words)
            print(no_words)
        for c in content:
            if c in vowels:
                count += 1
        print(count)
        average = "%.2f" % round(count / no_words, 2)
        return (text, float(average))

    def hardest_read(self):
        workers = multiprocessing.cpu_count()
        with ProcessPoolExecutor(workers) as ex:
            results = ex.map(self.avg_vowels, self.filenames)
        return list(results)

    def hardest_read2(self):
        read = multiprocessing(avg_vowels, url_list)
        read.sort(reverse=True)
        return read[0]

    def multiprocess(self, func, args, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(func, args)
        return list(res)

    if __name__ == '__main__':
        url_list = ['https://www.gutenberg.org/files/244/244-0.txt',
                    'https://www.gutenberg.org/files/57775/57775-8.txt',
                    'https://www.gutenberg.org/files/58585/58585-0.txt',
                    'https://www.gutenberg.org/files/2554/2554-0.txt',
                    'https://www.gutenberg.org/files/996/996-0.txt',
                    'https://www.gutenberg.org/files/64777/64777-0.txt',
                    'https://www.gutenberg.org/files/902/902-0.txt',
                    'https://www.gutenberg.org/files/33900/33900-8.txt',
                    'https://www.gutenberg.org/files/829/829-0.txt',
                    'https://www.gutenberg.org/files/64773/64773-0.txt']
