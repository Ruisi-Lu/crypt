RSA 檔案加密
=============

檔案結構
-------------
| crypt.py  
| decrypt.py  
| rename.py  
| RSAgenerator.py  
| readme.md  

運行環境
-------------
python3.7  
Cryptodome3.8.1

RSA 金鑰產生
-------------
RSAgenerator.py 使用Cryptodome 產生 RSA KEY 公鑰與私鑰

檔案加密
-------------
使用混合加密方式 PKCS#1 OAEP  對檔案內容進行非對稱加密填充
產生一組16字Session key並使用 RSA 公鑰 對 Session key 進行加密
將檔案內容以AES進行加密並將 nonce, 內容及驗證碼寫原文件
並對檔案名稱進行base 64 進行編碼進行倒序混淆後重新命名檔案
![](https://d1dwq032kyr03c.cloudfront.net/upload/images/20170106/20103434cTJ19UZgTu.jpg)  
圖片引用https://ithelp.ithome.com.tw/articles/10188528  

檔案解密
-------------
導入RSA 私鑰, Session key, nonce, 訊息驗證碼, 加密後的檔案內容後
重建出AES密鑰對檔案數據進行解密
即可解出原檔案
解出後將其檔名倒序並以base 64 解碼回原檔名即完成解密程序
![](https://d1dwq032kyr03c.cloudfront.net/upload/images/20170106/20103434tEe0Y1MwCN.jpg)  
圖片引用https://ithelp.ithome.com.tw/articles/10188528  

應用
-------------
如導入 os.walk 對磁碟機進行遊走
可以成為磁碟加密軟體或隨身碟加密軟體
當繼續加入提示畫面或更換桌布等惡意行為
此軟體將變為風流一時的勒索軟體wannaCry的簡易版

參考資料
-------------
https://pycryptodome.readthedocs.io  
https://maoao530.github.io/2016/11/20/python-rsa/  
https://zh.wikipedia.org/wiki/Base64  
https://zh.wikipedia.org/wiki/WannaCry  
https://ithelp.ithome.com.tw/articles/10188528
