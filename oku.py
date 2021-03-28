# https://docs.iota.org/docs/client-libraries/0.1/how-to-guides/python/read-transactions

from iota import Iota

api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

# tail_transaction_hash = 'ADZRYHNKFQONJTNSRJIWPQTMRPICHONRGLQVOALTYEOWRUVYOBFQOMVCVFRUVMYLSSWYLNOBGXPLID999'
tail_transaction_hash = 'P9I9ZMTTFFFXJZKGBKGRTAOPFKKYRLMILAFAUHGLUAT9YFSHSGPMWDCDTEXNUXDNZZHWRJ9CLQBHWG999'

bundle = api.get_bundles(tail_transaction_hash)

message = bundle['bundles'][0].tail_transaction.signature_message_fragment
print(message.decode())
















