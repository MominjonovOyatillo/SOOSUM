from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['POST'])
def post_order(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    Order.objects.create(name=name, number=number)
    order = Order.objects.last()
    data = OrderSerializer(order).data
    return Response(data)


@api_view(['GET'])
def get_Info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info).data
    return Response(ser)


@api_view(['GET'])
def get_order(request):
    order = Order.objects.last()
    ser = OrderSerializer(order).data
    return Response(ser)


@api_view(['GET'])
def get_product(request):
    product = Product.objects.last()
    ser = ProductSerializer(product).data
    return Response(ser)



@api_view(['GET'])
def get_productinfo(request):
    product_info = Productinfo.objects.all()
    ser = ProductinfoSerializer(product_info, many=True).data
    return Response(ser)



@api_view(['GET'])
def get_fakt(request):
    facts = Fakt.objects.all()
    ser = FaktSerializer(facts, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_aboutus(request):
    about = Aboutus.objects.last()
    ser = AboutusSerializer(about).data
    return Response(ser)


@api_view(['GET'])
def get_productfaq(request):
    productfaq = Productfaq.objects.last()
    ser = ProductfaqSerializer(productfaq).data
    return Response(ser)


@api_view(['GET'])
def get_header(request):
    header = Header.objects.last()
    ser = HeaderSerializer(header).data
    return Response(ser)


@api_view(['GET'])
def get_faq(request):
    faq = Faq.objects.all()
    ser = FaqSerializer(faq, many=True)
    return Response(ser)


@api_view(['GET'])
def get_advice(request):
    advice = Advice.objects.all()
    ser = AdviceSerializer(advice, many=True)
    return Response(ser)


@api_view(['GET'])
def get_abouttea(request):
    aboutt = Abouttea.objects.all()
    ser = AboutteaSerializer(aboutt, many=True)
    return Response(ser)


@api_view(['GET'])
def get_ijtimoiy(request):
    ijtimoiy = Ijtimoiy.objects.all()
    ser = IjtimoiySerializer(ijtimoiy, many=True)
    return Response(ser)

    
@api_view(["GET"])
def get_discount(request):
    discount = Discount.objects.last()
    ser = DiscountSerializer(discount).data
    return Response(ser)
