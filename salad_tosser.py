import random
import time
from random import randrange

nouns = [
    'channel factory',
    'MuSig',
    'Wasabi',
    'channel factories',
    'ColdCard',
    'PSBT',
    'Schnorr',
    'Schnorr sig aggregation',
    'HTLC',
    'HTLC (without the hash)',
    'single sig',
    'HTLC (with extra hash)',
    'AMP',
    'Quantum Safe',
    'scriptless script',
    'TapRoot',
    'Zerolink pools',
    'Atomic multi path payments #AMP',
    '# liquid L-BTC private key',
    'multisig',
    'taproot pubkey',
    'Scrit',
]

product = [
    '@nodl_it',
    'Wasabi',
    'OpenDime',
    'ColdCard',
    'Billfodl',
]

clients = [
    'bitcoind',
    'Knots',
    'libbitcoin',
    'TRB',
]

quantity = [
    '1',
    '6',
    '144',
    '2016',
    '210000',
]

entity = [
    'federation',
    'Zerolink pool',
    'Wasabi',
    'cloud',
    'IP',
    'tor onion',
    'TapRoot',
    'scriptless script',
]

value = [
    'BTC',
    'L-BTC',
    'private key',
    'fidelity bond',
]

adjectives = [
    'atomic swap',
    'MuSig',
    'coinjoin',
    'psbt',
    'cross input',
]

verbs = [
    'atomic swap',
    'MuSig',
    'coinjoin',
    'psbt',
    'single sig',
    'obfuscate',
    'hop',
    'rebalance',
    'transmit',
]

locations = [
    'on chain',
    'in the cloud',
    'on L2',
    'on Lightning',
    'on a Liquid sidechain',
    'on Liquid',
    'in Wasabi',
    'on TailsOS',
    'in state',
    'out of state',
    'on a sidechain',
    'in a side channel',
    'on a 2-way peg',
    'in moar and better mixes',
]

hashtags = [
    '#MoarEducation',
    '#stacksats',
    '#twoweeks',
    '#LightningNetwork',
    '#atomic',
    '#Schnorr',
    '#KeepBuilding',
    '#coinjoin',
    '#BitcoinFixesThis',
    '#MoarAndBetterCode',
    '#MoarAndBetterSaladTossing',
    '#MuhNetworkLevelPrivacy',
    '#MuhChainAnalSpies',
    '#MuhTestnetFakeSats',
]

meatspace_value = [
    'diesel',
    'eggs',
    'pork bellies',
    'frozen banana peels',
    'Berlin Wall rubble',
    'Beanie Babies',
    'frozen orange juice',
    'farmers market potatoes',
    'unredeemed plastic bottles',
    'fertilizer',
]

virtual_places = [
    '#TheDarkNet',
    'EBay',
    'MySpace',
    'Second Life',
    'SnapChat',
    'Deliveroo.com',
    'Qntra.net',
]

costs = [
    'for free',
    'for 1 sat/b',
    'for unfairly cheap',
]

accomplishments = [
    'stacked enough sats',
    'mined enough crypto',
    'dumped enough alt bags',
    'written enough BIPs',
    'pulled off enough exit scams',
    'hacked enough exchanges',
    'ponzied enough noobs',
]

ps = [
    'Seriously, you can think faster than I can talk.',
    'Twice the speed, and repeat the spoken words in your mind',
    'Much more attentive and efficient in knowledge accumulation.',
]

ex1 = [
    'UTXO 1 in block 500',
    'signed input off chain',
    'large slow blocks',
]

ex2 = [
    'UTXO 2 in block 550',
    'signed output on chain',
    'fast small blocks',
]

i = randrange(18)

if i == 0:
    print('Wen ' + random.choice(nouns) + ' ' + random.choice(locations) + '? ' + random.choice(hashtags)
          )
elif i == 1:
    print(random.choice(nouns) + ' is a ' + random.choice(adjectives) +
          ' ' + random.choice(nouns) + ' ' + random.choice(locations) +
          ', that looks like a ' + random.choice(nouns) + '.' +
          ' All 10 peers can ' + random.choice(verbs) +
          ' channels between each other ' + random.choice(locations) +
          ', instantly and ' + random.choice(costs) +
          '. Then they can ' + random.choice(verbs) +
          ' through each other to ' + random.choice(nouns) +
          ' outside the ' + random.choice(nouns) +
          '.' +
          ' ' + random.choice(hashtags)
          )
elif i == 2:
    print(random.choice(nouns) + ' obfuscate the actual ' + random.choice(nouns) + '.' +
          ' There can be unlimited ' + random.choice(nouns) + ' with each different values.' +
          ' ' + random.choice(hashtags)
          )
elif i == 3:
    print('with cross input '+ random.choice(nouns) + ' equal value UTXO is ' + random.choice(nouns) +
          ' for #coinswap that opens a ' + random.choice(nouns) + ' channel factory ' + random.choice(nouns) +
          ' routing' + '. ' + random.choice(hashtags)
          )
elif i == 4:
    print('When you hold a ' + random.choice(value) + ', then you can prove a claim on ' + random.choice(nouns) +
          ' locked up in a ' + random.choice(nouns) + ' not controlled by you but by a ' + random.choice(entity) +
          '. ' + random.choice(hashtags)
          )
elif i == 5:
    print(random.choice(nouns) + ' look like ' + random.choice(nouns) +
          ' but are actually ' + random.choice(nouns) + ' and thus you can do ' + random.choice(nouns) +
          ' either ' + random.choice(locations) + ' or ' + random.choice(locations) + '.' +
          ' So you ' + random.choice(verbs) + ' ' + random.choice(ex1) + ', with ' + random.choice(ex2) +
          '. ' + random.choice(hashtags)
          )
elif i == 6:
    print('moar ' + random.choice(hashtags[1:]) + ' = moar better.' +
          ' with the ' + random.choice(nouns) + ' RPC server you can run the ' + random.choice(
        nouns) + ' daemon 2016 blocks of every difficulty adjustment.' +
                 ' ' + random.choice(hashtags)
          )
elif i == 7:
    p0 = random.choice(product)
    while(p0 == 'Wasabi'):
        p0 = random.choice(product)

    s0 = random.choice(entity)
    s1 = random.choice(entity)
    while(s0 == s1 or s1 == 'Wasabi'):
        s1 = random.choice(entity)

    print('Yup, I use my ' + p0 + ' with Wasabi since ' + random.choice(quantity) +
          ' blocks ago, no additional ' + random.choice(nouns) + ' needed. ' +
          'If ' + random.choice(clients) + ' is on the same ' + random.choice(product) + ', then it does it automatically, ' +
          'if your node is on a separate hardware, set the ' + s0 + ' or ' + s1 +' in the Wasabi settings.' +
          ' ' + random.choice(hashtags)
          )
elif i == 8:
    s0 = random.choice(nouns)
    s1 = random.choice(nouns)
    while(s0 == s1):
        s1 = random.choice(nouns)
    print('Alice has a single pubkey UTXO, sends it to a single ' + random.choice(nouns) + ', which includes a ' + random.choice(nouns) + ' that Bob can spend this coin, only if he reveals a secret by sending his coin to Alice\'s ' + random.choice(nouns) + '. It\'s a ' + random.choice(nouns) + ', but with all spending conditions "hidden" in the pubkey & sigs.' +
          ' ' + random.choice(hashtags)
          )
elif i == 9:
    print(
        'Any merchant who demands that I pay him in fiat shitcoin is not an entrepreneur I want to collaborate with. Either you accept #' + random.choice(
            nouns) + ', or I walk out.' +
        ' ' + random.choice(hashtags)
        )
elif i == 10:
    print(
        'Traveling from Riga to southern Germany: - 7 vehicles - total of 10 hours, layover of 5 hours - harassment by border beurocrats. I cannot wait until an entrepreneur has ' + random.choice(
            accomplishments) + ' to build long distance jetpacks at scale.' + ' ' + random.choice(hashtags)
    )
elif i == 11:
    print(
        'I hold more value in ' + random.choice(meatspace_value) + ' than in fiat.' + ' ' + random.choice(hashtags)
    )
elif i == 12:
    print(
            'Open an issue on ' + random.choice(virtual_places) + ' or code it up yourself.' + ' ' + random.choice(hashtags)
    )
elif i == 13:
    print(
            'Oops... I should toss salad less often and work on my mad privacy skillz. https://twitter.com/HillebrandMax/status/1151400274319290369' + ' ' + random.choice(hashtags)
    )
elif i == 14:
    print(
            'Pay to EndPoint scriptless script atomic swap into a ' + random.choice(virtual_places) + ' ' + random.choice(nouns) + '!! The P2EP solves the unequal value issue!!!' + ' ' + random.choice(hashtags)
    )
elif i == 15:
    print(
            'good to know, but fyi, not optimal for your privacy to tell this in an unencrypted group with bunch of chain anal spies listening - now they might correlate down to a couple of coins which ones are yours :) ' + '#MuhNetworkLevelPrivacy' + ' ' + random.choice(hashtags)

    )
elif i == 16:
    print(
            'even the privacy of my testnet fake sats is too precious for me to use their software...' + ' ' + random.choice(hashtags)
    )
else:
    print('Yup, it is rather taxing on the ' + random.choice(nouns) + ' - ' +
          'and the moar ' + random.choice(nouns) + ' the moar better' +
          ' ' + random.choice(hashtags) +
          '.'
          )
