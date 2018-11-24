import urllib.request

class HtmlDownloader():

    def download(self, url):
        if url is None:
            return
        # 这里的下载形式有多种，自行选用
        response = urllib.request.urlopen(url)

        # 获取状态码 200为正常
        if response.getcode() != 200:
            return None
        # 返回读取的文件
        return response.read()
