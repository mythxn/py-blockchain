import uvicorn
from fastapi import FastAPI, Request

from chain_utils import ChainUtils

app = FastAPI()
node = None


class NodeAPI:

    @staticmethod
    def start(api_port):
        uvicorn.run("node_api:app", port=api_port)

    @staticmethod
    def inject_node(injected_node):
        global node
        node = injected_node

    @app.get("/blockchain")
    async def blockchain():
        return node.blockchain.to_json()

    @app.get("/transaction_pool")
    async def transaction_pool():
        return {ctr: transaction.to_json() for ctr, transaction in enumerate(node.transaction_pool.transactions)}

    @app.post("/transaction")
    async def transaction(self: Request):
        request_body = await self.json()
        if 'transaction' not in request_body:
            return {'message': 'No transaction in request'}
        transaction = ChainUtils.decode(request_body['transaction'])
        node.handle_transaction(transaction)
        return {'message': 'Transaction added to pool'}