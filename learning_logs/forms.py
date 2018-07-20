#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        #不生成标签，标签为空
        labels = {'text':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        #小部件：文本框，表格区域宽度设置为80列
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
