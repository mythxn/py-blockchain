import uvicorn
from fastapi import FastAPI

app = FastAPI()
node = None


class NodeAPI:

    def start(self, api_port):
        uvicorn.run("node_api:app", port=api_port)

    def inject_node(self, injected_node):
        global node
        node = injected_node

    @app.get("/blockchain")
    async def blockchain():
        return node.blockchain.to_json()

    @app.get("/transaction_pool")
    async def transaction_pool():
        return {ctr: transaction.to_json() for ctr, transaction in enumerate(node.transaction_pool.transactions)}
