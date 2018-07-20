#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        #�����ɱ�ǩ����ǩΪ��
        labels = {'text':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        #С�������ı��򣬱������������Ϊ80��
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
