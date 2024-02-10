import g4f

class ChatAi:

    def __init__(self):
        pass

    def gpt_chat(request):
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": f"{request}"}]
        )
        return response


