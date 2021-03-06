class TransactionPool:
    """
    Store Transactions not yet been added to Blockchain (for miners)
    """
    def __init__(self):
        """
        Initialize TransactionPool with empty pool
        """
        self.transaction_map = {}

    def set_transaction(self, transaction):
        """
        Set Transaction in TransactionPool
        :param transaction: <Transaction> Transaction being added to pool
        :return: None
        """
        self.transaction_map[transaction.id] = transaction

    def existing_transaction(self, address):
        """
        Find Transaction in pool generated by address
        :param address: <str> Address being searched for within pool
        :return: <Transaction / None> Transaction if match found, None if not
        """
        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction

    def transaction_data(self):
        """
        Get list of all Transactions from pool in JSON format
        :return: <list> All Transactions in JSON format
        """
        return list(map(lambda transaction: transaction.to_json(), self.transaction_map.values()))

    def clear_blockchain_transactions(self, blockchain):
        """
        Delete Transactions from pool if already recorded in Blockchain
        :param blockchain: <Blockchain> Blockchain being searched
        :return: None
        """
        for block in blockchain.chain:
            for transaction in block.data:
                try:
                    # Remove from pool if Transaction 'id' found in Blockchain
                    del self.transaction_map[transaction['id']]
                except KeyError:
                    pass
                    