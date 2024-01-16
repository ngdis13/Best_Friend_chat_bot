import g4f

class ChatAi:

    def __init__(self):
        pass

    def test_gpt(request):
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": f"{request}"}]
        )
        return response

ai = ChatAi
print(ai.test_gpt('Привет, расскажи сказку про насорога и океан на 5 слов'))
