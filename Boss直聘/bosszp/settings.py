# -*- coding: utf-8 -*-

BOT_NAME = 'bosszp'
SPIDER_MODULES = ['bosszp.spiders']
NEWSPIDER_MODULE = 'bosszp.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2

DEFAULT_REQUEST_HEADERS = {
':authority': 'www.zhipin.com',
':method': 'GET',
':path': '/job_detail/?query=%E5%AE%9E%E4%B9%A0%E7%94%9F&scity=101210100&industry=&position=',
':scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'no-cache',
'cookie': '_uab_collina=155014422431764990135294; sid=sem_pz_bdpc_dasou_title; lastCity=101210100; JSESSIONID=""; __c=1551772176; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY00nqx0KZEgsDG2M4T00000nPijNC00000xgJFi6.THdBULP1doZA80K85yF9pywd0ZnqrHmsPyRLrjTsnj0sPvDYP0Kd5HI7nj7anbDLnHIjnDR3wHI7nYDvPYuKP1ujnbPKPHnd0ADqI1YhUyPGujY1nHbkPjR4PHckFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQMGCpgKGUB4WUvYE5LPGujd1uydxTZGxmhwsmdqbmgPEINqYpgw_ufKWThnqnWbvPHD%26tpl%3Dtpl_11534_18997_15000%26l%3D1510822595%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3191459521_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D177%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26rqlang%3Dcn&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1550836734,1550970840,1551156086,1551772176; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2Fd4f38fdd312ef1051HF42tW1FlM%7E.html; __a=17967891.1550144234.1551156086.1551772176.69.5.7.7; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1551772347',
'pragma': 'no-cache',
'referer': 'https://www.zhipin.com/c101210100/?query=%E5%AE%9E%E4%B9%A0%E7%94%9F&ka=sel-city-101210100',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}




ITEM_PIPELINES = {

   'bosszp.pipelines.YBmysql': 300,

    }
