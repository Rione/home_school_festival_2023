# Currently not accessed from anywhere
import g4f

class GptApi():
    """
    A class which wraps the functions of gpt4free. No need to create an instance to use them.
    """
    @classmethod
    def ExtractColor(cls, content: str) -> str:
        g4f.debug.logging = True # enable logging
        g4f.check_version = False # Disable automatic version checking

        response: str =  g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.GptGo,
            messages=[{"role": "user", "content": "Please extract a color name from the following sentence and return it in English. Only return the name and never add any other information: "+content}],
            stream = False,
        )

        return response

