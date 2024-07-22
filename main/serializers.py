from rest_framework import serializers
from .models import Medical
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
import spacy


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self,validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password'],
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    
class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ['id', 'text', 'author', 'entities']
        read_only_fields = ['author', 'entities']

    def create(self, validated_data):
        request = self.context.get('request')
        text = validated_data['text']
        nlp = spacy.load('/Users/vrithul/Desktop/src/website/NER_Model')
        doc = nlp(text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        validated_data['entities'] = json.dumps(entities)
        validated_data['author'] = request.user
        return super().create(validated_data)