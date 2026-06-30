import requests
import os
    
def download_picture(url):
    print(f'开始下载{url}')
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join('./并发_并行,同步、异步，线程、进程/pictures', url.split('/')[-1])
        # 确保 pictures 文件夹存在
        if not os.path.exists('./并发_并行,同步、异步，线程、进程/pictures'):
            os.makedirs('./并发_并行,同步、异步，线程、进程/pictures')
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'下载完成{url}')
    else:
        print(f'下载失败{url}')
if __name__ == '__main__':
    urls = [
        'http://e.hiphotos.baidu.com/image/pic/item/a1ec08fa513d2697e542494057fbb2fb4316d81e.jpg',
        'http://c.hiphotos.baidu.com/image/pic/item/30adcbef76094b36de8a2fe5a1cc7cd98d109d99.jpg',
        'http://h.hiphotos.baidu.com/image/pic/item/7c1ed21b0ef41bd5f2c2a9e953da81cb39db3d1d.jpg',
    ]
    for url in urls:
        download_picture(url)
