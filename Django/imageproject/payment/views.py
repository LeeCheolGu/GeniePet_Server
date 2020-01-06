from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseRedirect, request
import requests
import json
from django.core import serializers

@api_view(['POST'])
def kakaoPay(request):
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "your number",
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        'cid': "TC0ONETIME",    #가맹점 코드
        'partner_order_id': '1001', #가맹점 주문 번호 임의의 값 
        'partner_user_id': 'GeniePet',  #가맹점 회원 id 임의의 값
        'item_name': '사료',  #상품명
        'quantity': 1,  #상품 수량
        'total_amount': 1000,  #상품 총액
        'vat_amount': 200,  #상품 부가세
        'tax_free_amount': 0,   #상품 비과세
        'approval_url': 'http://127.0.0.1:8000/success/', #결제 성공시
        'fail_url': 'http://127.0.0.1:8000/',    #결제 실패시
        'cancel_url': 'http://127.0.0.1:8000/',    #결제 취소시
    }
    response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
    response = json.loads(response.text)
    global TID
    TID = response['tid']
    return HttpResponseRedirect(response["next_redirect_mobile_url"])

def success(request):
    global pg
    pg = request.GET['pg_token']
    info = payapporve(pg)
    print(info)
    return Response('success.html')

def payapporve(pg):
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "your number",
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        'cid' : "TC0ONETIME",
        'tid' : TID,
        'partner_order_id': "1001",
        'partner_user_id' : 'GeniePet',
        'pg_token' : pg,
    }
    response = requests.post(url+"/v1/payment/approve", params=params, headers=headers)
    response = json.loads(response.text)
    return response


def pay(requests):
    return render(requests, 'pay.html')
