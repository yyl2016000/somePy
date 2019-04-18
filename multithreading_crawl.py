import requests
from lxml import etree
from queue import Queue
import threading
#import time
import json

class thread_crawl(threading.Thread):
    '''''
    抓取线程类
    '''

    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        # q是页面编号的队列
        self.q = q

    def run(self):
        print("抓取网页进程启动" + self.threadID)
        self.qiushi_spider()
        print("抓取网页进程结束", self.threadID)

    def qiushi_spider(self):
        while True:
            if self.q.empty():
                break
            else:
                page = self.q.get()
                print('网页获取线程', self.threadID ,',第', str(page),'页')
                url = 'http://www.qiushibaike.com/hot/page/' + str(page) \
                      + '/'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'}
                # 多次尝试失败结束、防止死循环
                timeout = 4
                while timeout > 0:
                    timeout -= 1
                    try:
                        content = requests.get(url, headers=headers)
                        data_queue.put(content.text)
                        break
                    except Exception as e:
                        print('糗事百科爬虫', e)
                if timeout < 0:
                    print('请求超时', url)

class Thread_Parser(threading.Thread):
    '''''
    页面解析线程类
    '''
    def __init__(self, threadID, queue, lock, f):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.queue = queue
        self.lock = lock
        self.f = f

    def run(self):
        print('解析线程启动：', self.threadID)
        global total, exitFlag_Parser
        while not exitFlag_Parser:
            try:
                ''''' 
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。 
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。 
                如果队列为空且block为False，队列将引发Empty异常。 
                '''
                item = self.queue.get(False)
                if not item:
                    pass
                self.parse_data(item)
                self.queue.task_done()
                print('解析线程：', self.threadID, ',total=', total)
            except:
                pass
        print('线程', self.threadID,'结束')
    def parse_data(self, item):
        '''''
        解析网页函数
        :param item: 网页内容
        :return:
        '''
        global total
        try:
            # 这里的item实际上就是之前抓取每页html代码得到的content.text
            html = etree.HTML(item)
            result = html.xpath('//div[contains(@id,"qiushi_tag")]')
            for site in result:
                try:
                    # 图片地址
                    imgUrl = site.xpath('.//img/@src')[0]
                    # 标题（发布者名字）
                    name = site.xpath('.//h2')[0].text
                    name = name.strip().replace('\n','')
                    # 注意，分享内容中存在<br>标签，用xpath抽取出来是list，
                    # 需要处理一下，合为一个字符串content
                    content = ''
                    content_list = site.xpath\
                        ('.//div[@class="content"]//span/text()')
                    for contents in content_list:
                        contents = contents.strip().replace('\n','')
                        content = content + contents
                    # 好笑数
                    vote = None
                    # 评论数
                    comments = None
                    try:
                        vote = site.xpath('.//i')[0].text
                        comments = site.xpath('.//i')[1].text
                    except:
                        pass
                    result = {
                        'imgUrl': imgUrl,
                        'title': name,
                        'content': content,
                        'vote': vote,
                        'comments': comments,
                    }

                    with self.lock:
                        self.f.write(json.dumps(
                            result, ensure_ascii=False) + "\n")

                except Exception as e:
                    print('获取每页下各条内容错误', e)
        except Exception as e:
            print('解析错误', e)
        with self.lock:
            total += 1


data_queue = Queue()
exitFlag_Parser = False
lock = threading.Lock()
total = 0


def main():
    # 生成一个json文件用来存储所爬取得数据
    output = open('糗事百科.json', 'a',encoding='utf-8')

    # 初始化网页页码page从1-10个页面
    # （你也可以爬更多页面，不过这个网址也没多少页）
    pageQueue = Queue(50)
    for page in range(1, 11):
        pageQueue.put(page)

    # 初始化采集线程（抓取每页内容的线程初始化为三个）
    crawlthreads = []
    crawlList = ["1", "2", "3"]

    for threadID in crawlList:
        thread = thread_crawl(threadID, pageQueue)
        thread.start()
        crawlthreads.append(thread)

    # 初始化解析线程parserList，解析线程也为三个
    parserthreads = []
    parserList = ["parser-1", "parser-2", "parser-3"]
    # 分别启动parserList
    for threadID in parserList:
        thread = Thread_Parser(threadID, data_queue, lock, output)
        thread.start()
        parserthreads.append(thread)

    # 等待队列清空
    while not pageQueue.empty():
        pass

    # 等待所有线程完成
    for t in crawlthreads:
        t.join()

    while not data_queue.empty():
        pass

    # 通知线程退出
    global exitFlag_Parser
    exitFlag_Parser = True

    for t in parserthreads:
        t.join()
    print("退出主线程")
    with lock:
        output.close()


if __name__ == '__main__':
    main()