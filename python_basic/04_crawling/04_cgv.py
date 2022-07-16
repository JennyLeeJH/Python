{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5f268649-882d-416f-89e6-d3b0c4f7cdfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import urllib.request\n",
    "from bs4 import BeautifulSoup\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d9dc03d4-46e6-4710-b786-4781ebe4bfa5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "url = 'http://www.cgv.co.kr/movies/'\n",
    "# res = urllib.request.urlopen(url)\n",
    "res = requests.get(url).text\n",
    "soup = BeautifulSoup(res,'lxml')\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "29976edd-9e1d-4dd9-86b9-afada3be4159",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<strong class=\"title\">탑건-매버릭</strong>, <strong class=\"title\">헤어질 결심</strong>, <strong class=\"title\">마녀(魔女) Part2. The Other One</strong>, <strong class=\"title\">범죄도시 2</strong>, <strong class=\"title\">컴온 컴온</strong>, <strong class=\"title\">펄프 픽션</strong>, <strong class=\"title\">비욘드 라이브 더 무비 : 샤이니 월드</strong>, <strong class=\"title\">홀리 모터스 무삭제판</strong>, <strong class=\"title\">고스트랜드</strong>, <strong class=\"title\">호수의 이방인</strong>, <strong class=\"title\">브로커</strong>, <strong class=\"title\">레베카</strong>, <strong class=\"title\">트윈 픽스</strong>, <strong class=\"title\">레드 로켓</strong>, <strong class=\"title\">러브 무삭제판</strong>, <strong class=\"title\">님포매니악 감독판 볼륨1</strong>, <strong class=\"title\">버즈 라이트이어</strong>, <strong class=\"title\">미친 능력</strong>, <strong class=\"title\">애프터 양</strong>]\n"
     ]
    }
   ],
   "source": [
    "result = soup.select('strong.title')\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "25f1d5f3-ec78-4890-b87c-19f274d385f3",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['탑건-매버릭', '헤어질 결심', '마녀(魔女) Part2. The Other One', '범죄도시 2', '컴온 컴온', '펄프 픽션', '비욘드 라이브 더 무비 : 샤이니 월드', '홀리 모터스 무삭제판', '고스트랜드', '호수의 이방인', '브로커', '레베카', '트윈 픽스', '레드 로켓', '러브 무삭제판', '님포매니악 감독판 볼륨1', '버즈 라이트이어', '미친 능력', '애프터 양']\n"
     ]
    }
   ],
   "source": [
    "name = []\n",
    "for item in result:\n",
    "    name.append(item.text)\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7d5b44fa-2265-4472-89c2-b5b1fc1a3659",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://img.cgv.co.kr/Movie/Thumbnail/Poster/000082/82120/82120_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85852/85852_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85871/85871_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85813/85813_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85920/85920_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000082/82616/82616_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86000/86000_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86006/86006_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85785/85785_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000079/79066/79066_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85829/85829_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000080/80957/80957_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000079/79972/79972_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85996/85996_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86004/86004_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86002/86002_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85977/85977_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85881/85881_320.jpg', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85884/85884_320.jpg']\n"
     ]
    }
   ],
   "source": [
    "result = soup.select('span.thumb-image img')\n",
    "#print(result)\n",
    "img = []\n",
    "for item in result:\n",
    "    #print(type(item))\n",
    "    img.append(item['src'])\n",
    "print(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "121a9414-6229-4362-8046-99f4e2f332ae",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('탑건-매버릭', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000082/82120/82120_320.jpg'), ('헤어질 결심', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85852/85852_320.jpg'), ('마녀(魔女) Part2. The Other One', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85871/85871_320.jpg'), ('범죄도시 2', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85813/85813_320.jpg'), ('컴온 컴온', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85920/85920_320.jpg'), ('펄프 픽션', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000082/82616/82616_320.jpg'), ('비욘드 라이브 더 무비 : 샤이니 월드', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86000/86000_320.jpg'), ('홀리 모터스 무삭제판', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86006/86006_320.jpg'), ('고스트랜드', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85785/85785_320.jpg'), ('호수의 이방인', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000079/79066/79066_320.jpg'), ('브로커', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85829/85829_320.jpg'), ('레베카', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000080/80957/80957_320.jpg'), ('트윈 픽스', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000079/79972/79972_320.jpg'), ('레드 로켓', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85996/85996_320.jpg'), ('러브 무삭제판', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86004/86004_320.jpg'), ('님포매니악 감독판 볼륨1', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000086/86002/86002_320.jpg'), ('버즈 라이트이어', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85977/85977_320.jpg'), ('미친 능력', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85881/85881_320.jpg'), ('애프터 양', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85884/85884_320.jpg')]\n"
     ]
    }
   ],
   "source": [
    "print(list(zip(name,img)))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
