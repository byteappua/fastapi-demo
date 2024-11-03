from contextlib import asynccontextmanager
from typing import Union
import asyncio

from fastapi import FastAPI, Depends


@asynccontextmanager
async def lifespan(app: FastAPI):
	# 在启动时创建单例对象
	app.state.singleton = MySingleton()
	print(app.state)
	yield
	# Clean up the ML models and release resources
	# ml_models.clear()
	print("stop", app.state.singleton.get_value())


app = FastAPI(lifespan=lifespan)


class MySingleton:
	def __init__(self):
		self.value = "Initial value"

	def get_value(self):
		return self.value


@app.get("/")
def read_root():
	return {"Hello": "World"}


@app.get("/test")
async def root(singleton: MySingleton = Depends(lambda: app.state.singleton)):
	return {"value": singleton.get_value()}


@app.get("/helo")
async def root():
	# 使用 asyncio.sleep 模拟异步操作
	await asyncio.sleep(1)
	return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="0.0.0.0", port=10001)
