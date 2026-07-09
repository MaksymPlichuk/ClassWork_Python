import random

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser
#permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from .utils import save_custom_image

from .models import CustomUser
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer

FIRST_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Lee"]
DOMAINS = ["example.com", "test.com", "mail.com"]


def generate_random_users(n=5):
    created_users = []

    for _ in range(n):
        while True:
            username = f"user{random.randint(1000, 9999)}"
            if not CustomUser.objects.filter(username=username).exists():
                break

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(DOMAINS)}"

        user = CustomUser.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        created_users.append(user)

    return created_users


# ViewSet=controller ReadOnlyModelViewSet — дає тільки GET (list/retrieve), без create/update/delete. Це одразу і Controller, і частина роутингу (DRF роутер сам генерує /users/, /users/{id}/ з цього класу).
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes=[MultiPartParser, FormParser] #змінюємо форму

    def get_permissions(self):
        if self.action in ['login', 'register']:
            permission_classes = [AllowAny]
            # або, якщо хочете взагалі заборонити GET списку всім:
            # permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

#@action(...) — це кастомні ендпоінти поверх стандартного CRUD, як окремі [HttpPost("login")] методи в ASP.NET контролері:
    @action(detail=False, methods=['post'])
    def generate(self, request):
        users = generate_random_users(5)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='login', serializer_class=LoginSerializer)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #валідуємо дані з форми з нашим DTO     
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        user = CustomUser.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)   
        
        #вбудова ф-цыя
        refresh = RefreshToken.for_user(user)
        return Response ({
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_200_OK)
        

    @action(detail=False, methods=['post'], url_path='register', serializer_class=RegisterSerializer)
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            if (serializer.validated_data["password"]==serializer.validated_data["confirm_password"]):
                
                user = CustomUser.objects.create_user(
                    username = serializer.validated_data["username"],

                    # якщо serializer.validated_data['email'] то при пустому полі буде помилка
                    email = serializer.validated_data.get('email', ''),
                    first_name = serializer.validated_data.get('first_name', ''),
                    last_name = serializer.validated_data.get('last_name', ''),
                    password = serializer.validated_data["password"],
                )


                #Викликає RegisterSerializer.create() [перевизначений нами метод у serializers.py]
                #user = serializer.save() --непрацює з картинками

                uploaded_image = serializer.validated_data["image"]
                if uploaded_image:
                    user.image_small=save_custom_image(uploaded_image, size=(300,300), folder="small")
                    user.image_medium=save_custom_image(uploaded_image, size=(800,800), folder="medium")
                    user.image_large=save_custom_image(uploaded_image, size=(1200,1200), folder="large")

                user.save() #для збереження картинок
                
                #З rest_framework_simplejwt — генерує пару токенів (refresh + access), "прив'язаних" до конкретного юзера
                refresh = RefreshToken.for_user(user)

                return Response({
                    "user": UserSerializer(user).data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                }, status=status.HTTP_201_CREATED)
            return Response("Паролі не збігаються", staus=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            