from django.shortcuts import render
import google.generativeai as genai
from .models import Zprom
import os

def home2(request):
	return render(request,'home.html',{})

def home(request):
	response = None
	all_entries = Zprom.objects.all()  # Inicializa a variável antes do bloco condicional
    
	if request.method == 'POST':
		#question = request.POST.get('question')
		question = request.POST.get('question').encode('utf-8').decode('utf-8')

		# Código Python que processa a pergunta e retorna uma resposta
		# Este é um exemplo simples, você pode substituir pelo seu código
		
 		# Garante que o valor de 'response' não será nulo
		if not response:
			response = "Response could not be generated7."


		

		genai.configure(api_key='')
		
		# Prepara o histórico de conversas a partir das perguntas e respostas do banco de dados
		history = []
		for entry in all_entries:
			history.append({"role": "user", "parts": entry.question})
			history.append({"role": "model", "parts": entry.response})

		
		try:
            # Adjust the way you interact with the GenerativeModel
			model = genai.GenerativeModel('gemini-1.5-flash')

			chat = model.start_chat(
    			history=history
			)

			result = chat.send_message(question)
			response_text = result.text.encode('utf-8').decode('utf-8')
			#response_text = result.text.encode('utf-8').decode('utf-8')
        
			#result = response_text
			print(result.text)
			
			
			#response = chat.send_message("How many paws are in my house?")
			#print(response.text)







			#result = model.generate_content({"text": question})
			
			#response = result.text if result and hasattr(result, 'text') else "No response generated."

		
		
							#model = genai.GenerativeModel('gemini-1.5-flash')
							#response = f"Você perguntou: {question}. Aqui está a resposta!"
							
							
							
		#response = model.generate_content({question})
							#response = model.generate_content("daniel")
							
							
							
			#response = result.text if result else "No response generated2."


			if result and hasattr(result, 'text') and len(result.text) > 0:
				response = result.text
			

			# Salvar a pergunta e a resposta no banco de dados
			zprom_entry = Zprom(question=question, response=response)
			zprom_entry.save()

			all_entries = Zprom.objects.all()

			if response is None:
				response = "No response was generated3."
			
		except Exception as e:
            # Handle exceptions that may occur during the API call
			response = f"An error occurred: {str(e)}"
							
		
							
		print(response)
		
		
    # Always return a valid HttpResponse object
	return render(request, 'home2.html', {'response': response, 'all_entries': all_entries})
	
		
		
