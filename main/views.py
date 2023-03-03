from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['POST'])
def post_order(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    Order.objects.create(name=name, number=number)
    return Response('Success')


@api_view(['GET'])
def get_Info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)
    return Response(ser.data)


@api_view(['GET'])
def get_order(request):
    order = Order.objects.all()
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_productinfo(request):
    product_info = Productinfo.objects.all()
    ser = ProductinfoSerializer(product_info, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_fakt(request):
    facts = Fakt.objects.all()
    ser = FaktSerializer(facts, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_aboutus(request):
    about = Aboutus.objects.all()
    ser = AboutusSerializer(about, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_productfaq(request):
    productfaq = Productfaq.objects.all()
    ser = ProductfaqSerializer(productfaq, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_header(request):
    header = Header.objects.all()
    ser = HeaderSerializer(header, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_faq(request):
    faq = Faq.objects.all()
    ser = FaqSerializer(faq, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_advice(request):
    advice = Advice.objects.all()
    ser = AdviceSerializer(advice, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_abouttea(request):
    aboutt = Abouttea.objects.all()
    ser = AboutteaSerializer(aboutt, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_ijtimoiy(request):
    ijtimoiy = Ijtimoiy.objects.all()
    ser = IjtimoiySerializer(ijtimoiy, many=True)
    return Response(ser.data)
