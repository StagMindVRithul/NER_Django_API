from django.shortcuts import redirect, render
from .forms import RegisterForm, MedicalForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Medical
from rest_framework import generics, status,  permissions
from .serializers import RegisterSerializer,LoginSerializer, MedicalSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import spacy
import json

nlp = spacy.load('/Users/vrithul/Desktop/src/website/NER_Model')

@login_required(login_url="/login")
def home(request):
    posts = Medical.objects.all()
    if request.method =="POST":
        post_id = request.POST.get("post-id")
        post = Medical.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request,'main/home.html',{'posts':posts})


@login_required(login_url="/login")
def create_medical(request):
    if request.method == "POST":
        form = MedicalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            
            text = form.cleaned_data['text']
            doc = nlp(text)
            entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
            post.entities = json.dumps(entities)  
            
            post.save()
            return redirect('/home')
    else:
        form = MedicalForm()
    
    return render(request, 'main/create_medical.html', {'form': form})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request,'main/registration/sign_up.html',{'form':form})

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user":RegisterSerializer(user,context=self.get_serializer_context()).data,
            "token":token.key
        })
        

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user":RegisterSerializer(user,context=self.get_serializer_context()).data,
            "token":token.key
        })

class CreateMedicalView(generics.CreateAPIView):
    queryset = Medical.objects.all()
    serializer_class = MedicalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)