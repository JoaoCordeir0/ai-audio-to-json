import uvicorn
import logging
import dotenv
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routes import router

# Carrega as variáveis de ambiente
dotenv.load_dotenv(override=True)

# Configuração de logging para apenas warnings em PRD
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR if os.getenv('ENV') == 'development' else logging.WARNING)

if os.getenv('ENV') == 'development':
    handler = logging.FileHandler('errors.log')
    handler.setLevel(logging.ERROR)
else:
    handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Instância da API
app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],     
    allow_methods=['*'], 
    allow_headers=['*']
)

""" NOTE: Middleware para capturar exceções """
@app.middleware('http')
async def log_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception:
        logger.error(f'Error without request: {request.method} {request.url}', exc_info=True)
        return JSONResponse(
            status_code=500,
            content={'detail': 'Internal Server Error'}
        )
    
# Inclui as rotas do arquivo routes.py
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)