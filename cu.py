import datetime
import hmac
import hashlib
import os
import time
import requests
import json
import urllib.request
import secrets
from urllib.parse import urlencode
from wordpress_xmlrpc import Client
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods import posts

class cupangMgr:
    DOMAIN = "https://api-gateway.coupang.com"
# HMAC 인증정보 생성
    def generateHmac(self, method, url, secretKey, accessKey):
        path, *query = url.split("?")
        os.environ["TZ"] = "GMT+0"
        datetime = time.strftime('%y%m%d') + 'T' + time.strftime('%H%M%S') + 'Z'
        message = datetime + method + path + (query[0] if query else "")
        signature = hmac.new(bytes(secretKey, "utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(accessKey,datetime,signature)

    def get_productsdata(self, request_method, authorization, keyword, limit):
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(
            keyword) + "&limit=" + str(limit)
        url = "{}{}".format(self.DOMAIN, URL)
        response = requests.request(method=request_method, url=url, headers={"Authorization": authorization,
                                                                            "Content-Type": "application/json;charset=UTF-8"})
        retdata = json.dumps(response.json(), indent=4).encode('utf-8')
        jsondata = json.loads(retdata)
        data = jsondata['data']
        productdata = data['productData']
        return productdata

if __name__ == '__main__':
    method = 'GET'      # 정보를 얻는것이기 때문에 GET
    keyword = '제습기'      # 검색할 키워드, 쿠팡에서 검색하는거랑 결과가 동일합니다.
    limit =10               # 몇개의 정보를 가져올지 설정. 상위부터 가져옵니다.
    access_key = '0c3d2d4f-e9a4-4b0d-b11d-b6f1aee1de02'    # API access key
    secret_key = 'c6ab8cc040a56f26fcb871d9710faa97665a8a57'    # API secret key
    URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(keyword) + "&limit=" + str(limit)

    test = cupangMgr()
    authorization = test.generateHmac(method, URL, secret_key, access_key)  # HMAC 생성
    productdata = test.get_productsdata(method, authorization, keyword, limit)  # API 호출
    productCount = len(productdata)
    i = 0
    while i < productCount:
        print(productdata[i]['productId'])
        print(productdata[i]['productName'])
        print(productdata[i]['productPrice'])
        print(productdata[i]['productImage'])
        print(productdata[i]['productUrl'])
        print(productdata[i]['keyword'])
        print(productdata[i]['rank'])
        print(productdata[i]['isRocket'])
        print(productdata[i]['isFreeShipping'])
        print(datetime.datetime.now())
        strProductId = str((productdata[i]['productId']))
        strProductName = (productdata[i]['productName'])
        strProductPrice = str((productdata[i]['productPrice']))
        strProductImage = (productdata[i]['productImage'])
        strProductUrl = (productdata[i]['productUrl'])
        strKeyword = (productdata[i]['keyword'])
        strRank = str((productdata[i]['rank']))
        strIsRocket = bool(productdata[i]['isRocket'])
        strIsFreeShipping = bool(productdata[i]['isFreeShipping'])
        if strIsRocket == True:
            strIFRocket = '로켓배송 가능 상품이라 로켓배송 지역이면, 로켓배송으로 빠르게 배송 받아보실 수 있습니다.'
        else:
            strIFRocket = '로켓배송 가능한지는 아래 배송도착일 확인 링크에서 확인 가능합니다.'

        if strIsFreeShipping == True:
            strIFFreeship = '배송비는 무료이며,'
        else:
            strIFFreeship = '배송비는 아래 배송도착일 확인 링크에서 확인 가능하며,'

        client = Client("http://colorpen.kr/xmlrpc.php", "admin", "wjdcjf!!05")
        postx = WordPressPost()
        postx.title = strProductName
        postx.slug = strProductName
        postx.content = '''<p><span style="font-family: Helvetica;">오늘 소개해드릴 상품은 '''+strProductName+''' 입니다.</span></p>
<p><span style="font-family: Helvetica;">이 상품은 쿠팡에서 '''+strKeyword+''' 조회시 추천 순위 '''+strRank+'''위 입니다.</span></p>
<p><span style="font-family: Helvetica;">'''+strKeyword+''' 인기순위, '''+strKeyword+''' 가격정보는 아래 본문에서 확인 가능합니다.</span></p>
<p><span style="font-family: Helvetica; color: rgb(40, 50, 78);">(업데이트 날짜 : '''+time.strftime('%y-%m-%d')+''')</span></p>
<p><span style="font-family: Helvetica;">상품별 추천순위, 판매가격, 배송비, 로켓배송 가능여부, 상품사진을 확인 하실 수 있습니다.</span></p>
<p><span style="font-family: Helvetica;"><br></span></p>
<h1><span style="font-family: Helvetica; font-size: 19px; color: rgb(209, 72, 65);">'''+strProductName+'''</span></h1>
<p><span style="font-family: Helvetica;"><br></span></p>
<h2><span style="font-family: Helvetica; font-size: 19px; color: rgb(243, 121, 52);">▶ 판매가격</span></h2>
<p><span style="font-family: Helvetica;">가격은 <span style="color: rgb(44, 130, 201);">'''+strProductPrice+'''원</span> 입니다.</span></p>
<p><span style="font-family: Helvetica;">(아래 링크에서 현재 가격을 확인 하세요.)</span></p>
<p><a href="'''+strProductUrl+'''" rel="noopener noreferrer" target="_blank"><span style="font-family: Helvetica;"><strong>★ 현재가격 보기 ★</strong></span></a></p>
<p><span style="font-family: Helvetica;"><br></span></p>
<h2><span style="font-family: Helvetica; font-size: 19px; color: rgb(243, 121, 52);">▶ 배송비, 로켓배송</span></h2>
<p><span style="font-family: Helvetica;">'''+strIFFreeship+''',</span></p>
<p><span style="font-family: Helvetica;">'''+strIFRocket+'''</span></p>
<p><span style="font-family: Helvetica;">(배송비, 로켓배송 가능 여부가 변동될 수 있으니 아래 링크에서 확인하세요.)</span></p>
<p><a href="'''+strProductUrl+'''" rel="noopener noreferrer" target="_blank"><span style="font-family: Helvetica;"><strong>★ 배송비, 로켓배송 보기 ★</strong></span></a></p>
<p><span style="font-family: Helvetica;"><br></span></p>
<h2><span style="font-family: Helvetica; font-size: 19px; color: rgb(243, 121, 52);">▶ 상품 상세정보, 구매후기</span></h2>
<p><span style="font-family: Helvetica;">추가적인 상품정보, 상품사진 및 구매후기는 아래 상품정보 상세보기에서 확인 가능합니다.</span></p>
<p><a href="'''+strProductUrl+'''" rel="noopener noreferrer" target="_blank"><span style="font-family: Helvetica;"><strong>★ 상품정보 상세보기 ★</strong></span></a></p>
<p><span style="font-family: Helvetica;"><br></span></p>
<h2><span style="font-family: Helvetica; font-size: 19px; color: rgb(243, 121, 52);">▶ 상품사진</span></h2>
<p><img src="'''+strProductImage+'''"></p>
<p><br></p>'''
        postx.terms_names = {
            'post_tag': [strKeyword+' 추천',strKeyword+' 순위',strKeyword+' 비교',strKeyword+' 가격비교'],
            'category': ['Coupangs']
        }
        postx.post_status = 'publish'
        client.call(posts.NewPost(postx))
        time.sleep(10)
        i = i + 1