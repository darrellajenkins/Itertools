from itertools import batched

flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
unflattened = list(batched(flattened_data, 2))
print(unflattened)


for batch in batched('ABCDEFG', 3):
    print(batch)


names = ['Fluffkins', 'Biscuit', 'Zigzag', 'Wooferson', 'Nacho', 'Gizmo', 'Bubbles', 'Muffin',
         'Ziggy', 'Waffles', 'Nugget', 'Gidget', 'Butterscotch', 'Zigmund', 'Wookiee', 'Noodle',
         'Giggles', 'Buster', 'Munster', 'Zizzy', 'Wrigley', 'Nougat', 'Ginger', 'Butters',
         'Munchkin', 'Zorro', 'Wrinkles', 'Nutmeg', 'Gizmodic', 'Buttercup', 'Muffinhead',
         'Zazu', 'Wrench', 'Nutella', 'Gizmatic', 'Butterfingers', 'Muffintop', 'Zaboo',
         'Wrumples', 'Nutkin', 'Gizmotron', 'Butterstuff', 'Zazzy', 'Wuffles', 'Nutrageous',
         'Gizmonoid', 'Butterworth', 'Muffintush', 'Wugglet', 'Nutster', 'Gizmonica', 'Buttertart',
         'Zbee', 'Wuggles', 'Nutstravaganza', 'Gizbot', 'Butterbear', 'Zeeble', 'Wuggy', 'Nutzoid',
         'Gizmoppet', 'Butterbloop', 'Zeeker', 'Wuglet', 'Nutzzzy', 'Gizmosaurus', 'Butterboom',
         'Zeenie', 'Wugsly', 'Nutzywig', 'Gizmotronic', 'Butterbubble', 'Zeenie', 'Snickerpoo',
         'Fluffernutter', 'Wigglebutt', 'Flufferpup', 'Snickerpup', 'Wigglemutt', 'Fluffertail',
         'Snickerpaws', 'Wigglewagg', 'Flufferspots', 'Snickerspark', 'Fluffershake',
         'Snickersticks', 'Wigglewoof', 'Fluffbunny', 'Snuckerpup', 'Wiggletuft', 'Fluffster',
         'Snugglemutt', 'Wigglewhiskers', 'Fluffernubbin', 'Snickerpibble', 'Wigglewiggle',
         'Flufferfloof', 'Snorkelpup', 'Wigglezag', 'Flufferpuff', 'Snugglehound']

for name in batched(names, 5):
    print(name)