from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'home.html')
def c(request):
    return render('c.html')
def cpp(request):
    return render('cpp.html')
def python(request):
    return render('python.html')
def java(request):
    return render('java.html')
def html(request):
    return render('html.html')
def css(request):
    return render('css.html')
def javasctipt(request):
    return render('javasctipt.html')
def django(request):
    return render('django.html')
def mysql(request):
    return render('mysql.html')
def flask(request):
    return render('flask.html')
def restapi(request):
    return render('restapi.html')
def rice(request):
    return HttpResponse("Rice is a rich source of carbohydrates, the body's main fuel source. Carbohydrates can keep you energized and satisfied, and are important for fueling exercise. Brown rice, especially, is an excellent source of many nutrients, including fiber, manganese, selenium, magnesium, and B vitamins")
def pealse(request):
    return HttpResponse("Pulses, also known as grain legumes, are a group of 12 crops that includes dry beans, dry peas, chickpeas, and lentils. They are high in protein, fibre, and various vitamins, provide amino acids, and are hearty crops. They are most popular in developing countries, but are increasingly becoming recognized as an excellent part of a healthy diet throughout the world.")
def pickle(request):
    return HttpResponse("Unique Variety Of Indian Pickles. A Perfect Side Dish. Quality Ingredients. Mango Pickle, Methiya Mango Pickle, Mixed Pickle, Sweet Lemon / Mango Pickle and More. Free shipping above ₹499। COD available। High-quality products। Delivering across India।")
def papad(request):
    return HttpResponse("Papad")
def badi(request):
    return HttpResponse("Yuvraj Food Product Traditional Rajasthani Sundried Moong Badi & Mangodi marwari mungodi Combo Pack of 2 ( 200 Gm X 2) Free kasuri Methi Pouch ")
def  pasta(request):
    return HttpResponse("Macaroni pasta is the most flavorful and you can mix it up with thick cheese sauces, creamy or tomato sauces, and vegetables. Easy Pasta recipes. Spaghetti.")
def sabudana(request):
    return HttpResponse("Sabudana khichdi is an Indian dish made with tapioca pearls, peanuts, potatoes and herbs. It is one of the most common foods eaten during ")
def chana(request):
    return HttpResponse("chana")
def oil(request):
    return HttpResponse("Cooking oil is plant, animal, or synthetic liquid fat used in frying, baking, and other types of cooking. It is also used in food preparation and flavoring")
def sugar(request):
    return HttpResponse("Sugar is the generic name for sweet-tasting, soluble carbohydrates, many of which are used in food. Simple sugars, also called monosaccharides")
def aata(request):
    return HttpResponse("Whole wheat atta flour is a staple food item that is used in every household and in most Indian food recipes, be it chapatis, puris, parathas, or delicious ...")