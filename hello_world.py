# https://docs.iota.org/docs/client-libraries/0.1/how-to-guides/python/send-your-first-bundle

from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

api = Iota('https://nodes.devnet.iota.org:443', testnet=True)

address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'

message = TryteString.from_unicode('Hello world sahin')

tx = ProposedTransaction(
    address=Address(address),
    message=message,
    value=0
)
result = api.send_transfer(transfers=[tx])

print(result['bundle'].tail_transaction.hash)
