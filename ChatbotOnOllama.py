import threading
import ollama
import sys
import time
import requests
def generate_response(query):
  answer = ollama.chat(
    model = 'qwen2.5:1.5b',
    message = [{'role' : 'user','content' : 'query'}]


    
  )
  return answer = ['message']['content']
query = input("enter yout question : "  )
