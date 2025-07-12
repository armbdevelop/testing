import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tasks import router as tasks_router


app = FastAPI()

app.include_router(tasks_router)


#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, env_file='.env')
