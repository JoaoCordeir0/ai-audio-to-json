
class PromptUtil:

    @staticmethod
    def get_prompt_product_register() -> str:
        prompt = """Você receberá um texto que contém informações sobre agronegócio. Extraia as seguintes informações:
        - Nome do produto;
        - Nome comercial do produto;
        - Variedade do produto;
        - Descrição do produto;

        Encontre essas informações e responda no formato JSON a seguir:
        {
            "name": "Nome do produto",
            "comercial_name": "Nome comercial do produto",
            "variety": "Variedade do produto",
            "description": "Descrição do produto"
        }"""
        return prompt