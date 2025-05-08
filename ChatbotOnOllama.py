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
generate_response(query)

the chatbot required the ollama model or I can yes htis is the best can do this off;ien anps we sare peofidinf he socod epserve this with low latency with the network connection 
