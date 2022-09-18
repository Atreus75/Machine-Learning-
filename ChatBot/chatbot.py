from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from  ultilidades import verificar_função


class chatbot():
    
    
    def __init__(self, nome):
        self.nome = nome
        # Cria uma instância do chatbot com os devidos adaptadores lógicos e de memória
        self.bot = ChatBot(
            self.nome,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            #preprocessors=convert_to_ascii,
            logic_adapters = [
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Desculpe, não consegui entender o que você disse.',
                    'maximum_similarity_threshold': 0.99,
                    'statement_comparison_function': LevenshteinDistance
                }
            ],
        )
    
    def treinar(self):
        #Treinando o bot
        trainer_corpus = ChatterBotCorpusTrainer(self.bot)
        trainer_corpus.train(r"C:\Users\Rodrigo\Documents\Estudos\Programação\Python\Hacking\BIT\dialogos_treinamento\linguistic.yml")
        trainer_corpus.train(r"C:\Users\Rodrigo\Documents\Estudos\Programação\Python\Machine Learning\BIT\dialogos_treinamento\greetings.yml")
        trainer_corpus.train(r"C:\Users\Rodrigo\Documents\Estudos\Programação\Python\Machine Learning\BIT\dialogos_treinamento\bye.yml")
        trainer_corpus.train(r"C:\Users\Rodrigo\Documents\Estudos\Programação\Python\Machine Learning\BIT\dialogos_treinamento\feelings.yml")
    
    def responder(self, entrada):
        # Trata a entrada do Usuário
        entrada_str = entrada
        entrada_state = Statement(entrada)
            
        # Gera a resposta inicial do bot
        out = self.bot.generate_response(entrada_state)
            
        # Verifica se uma função de ultilidade pode ser aplicada á conversa
        #out = verificar_função(entrada_str, out)
            
        # Método de aprendizado direto com o usuário
        if str(out) == 'Desculpe, não consegui entender o que você disse.':
            nova_resposta = Statement(str(input('Me ensine uma resposta para isso: ')))
            self.bot.learn_response(nova_resposta, entrada_state)
            print('Resposta adicionada, muito obrigado!')
        
        # Encerrar conversa
        if entrada_str in "Encerrar conversa":
            out = f'{self.bot.name}: Até a próxima conversa! ;)'
            
        # Retorna a resposta da instância do ChatBot
        return f'{self.bot.name}: {out}'
        