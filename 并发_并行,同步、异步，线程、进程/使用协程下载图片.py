import aiohttp, asyncio
import os
    

async def download_picture(session, url):
    print(f'开始下载:{url}')
    #发送网络请求，获取这张图片，请求发出去后，要等待服务器把数据返回，等的这段时间就是I0等待
    response = await session.get(url)
    #等待数据(图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是I0等待)
    content = await response.read()
    print('下载完毕')
    #保存图片到本地
    with open(url[-10:], 'wb') as file:
        file.write(content)
    #释放连接资源(告诉aiohttp，这个连接我不用了，你可以回收了)
    await response.release()
async def main():
    url_list = [
        'http://e.hiphotos.baidu.com/image/pic/item/a1ec08fa513d2697e542494057fbb2fb4316d81e.jpg',
        'http://c.hiphotos.baidu.com/image/pic/item/30adcbef76094b36de8a2fe5a1cc7cd98d109d99.jpg',
        'http://h.hiphotos.baidu.com/image/pic/item/7c1ed21b0ef41bd5f2c2a9e953da81cb39db3d1d.jpg'
    ]
#创建会话对象(发请求的工具)
    session = aiohttp.ClientSession()
    #创建多个协程对象
    coroutine_list = [download_picture(session, url) for url in url_list]
    #将多个协程对象交给事件循环
    await asyncio.gather(*coroutine_list)
    #关闭会话
    await session.close()

    asyncio.run(main())










