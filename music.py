import os
from tkinter import *
from selenium import webdriver
from urllib.request import urlretrieve

class music():

    def xz(self):
        root = Tk()

        root.title("音乐下载器")

        root.geometry("500x500")

        label = Label(root, text="请输入下载歌曲:")

        label.grid()

        self.entry = Entry(root)

        self.entry.grid(row=0, column=1)

        self.text = Text(root, width=70, heigh=34)

        self.text.grid(row=1, columnspan=2)

        botton = Button(root, text="下载歌曲", command=self.get_music)

        botton.grid(row=2, column=0, sticky=W)

        botton2 = Button(root, text="退出程序", command=sys.exit)

        botton2.grid(row=2, column=0, sticky=E)

        root.mainloop()  # 显示输入框


    def cbk(self,a, b, c):
        '''''回调函数
        @a:已经下载的数据块
        @b:数据块的大小
        @c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100

        percentage = ('%.2f%%\n' % per)

        print(percentage)

        self.text.insert(END, percentage)
        self.text.see((END))
        self.text.update()

    def music_download(self,song_id, music_name):
        download_url = ("http://music.163.com/song/media/outer/url?id=%s.mp3" % (song_id))

        # 存储至本地文件夹
        os.makedirs("music", exist_ok="true")

        path = ("music/%s.mp3" % (music_name))

        urlretrieve(download_url, path, self.cbk)



    # selenium获取音乐ID
    def get_music(self):
        music_name = self.entry.get()

        print(music_name)

        url = ("https://music.163.com/#/search/m/?s=%s&type=1" % (music_name))

        option = webdriver.ChromeOptions()

        option.add_argument("headless")

        driver = webdriver.Chrome(options=option)

        driver.get(url)

        driver.switch_to.frame('g_iframe')

        req = driver.find_element_by_id('m-search')

        a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")

        song_id = (a_id.split("=")[-1])

        self.music_download(song_id, music_name)


music().xz()




