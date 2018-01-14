# Natural Language Processing
Teaching computer word meanings with Harry Potter

## Semantic Vectors 

In this simple demo we teach the computer word semantics using context vectors. This means that for each word we compose a vector which contains the words this word most often appears with in the given text. After this the similarity of two words can be calculated as the cosine distances of their corresponding vectors.

To clarify this, let's walk through a simple example.
In this example the words `apple` and `computer` are more similar to each other than `apple` and `cat`.
This is because in our example text, the words `apple` and `computer` often appear with `coding`, `screen` and `keyboard`,
but rarely with `cute` or `flurry`, which can be seen in the example context vectors:

```
apple : { coding : 10, screen: 9, keyboard: 7}
computer : { coding : 11, screen: 10, keyboard: 4, laptop: 5}
cat : { cute: 9, furry: 4, miau: 4}
```

Now, let's build the context vectors using the first Harry Potter book (Philosopher's stone). Here is the list of most similar word pairs. As some quality control I marked the words I find similar with `Y` and the ones I don't with `X`.

```
X (('switch', 'theory'), 0.9578236803139749)
Y (('strawberries', 'treacle'), 0.9551548868707481)
X (('nonexplodable', 'pack'), 0.9516444766248942)
Y (('boiled', 'roast'), 0.9508984333140903)
Y (('tarts', 'treacle'), 0.9452211725035092)
Y (('boiled', 'potatoes'), 0.944347475811051)
Y (('doughnuts', 'treacle'), 0.9442109346492937)
X (('chf', 'sore'), 0.9438930558992281)
Y (('boogers', 'trolls'), 0.9425075480809878)
X (('dreadlocks', 'lifted'), 0.9423677943275823)
Y (('alchemist', 'flamel'), 0.9420199987755068)
Y (('eclairs', 'treacle'), 0.941165198530256)
Y (('beans', 'flavor'), 0.9406034066543112)
Y (('eclairs', 'jam'), 0.9404016757569477)
X (('balloons', 'grow'), 0.9383840333653314)
Y (('buttered', 'peas'), 0.9364399817198383)
X (('downpour', 'theyve'), 0.9361052983381168)
Y (('doughnuts', 'jam'), 0.9359445681745813)
X (('curry', 'grass'), 0.9341959681519371)
X (('strawberries', 'trifle'), 0.9341500558879627)
X (('commit', 'unicorn'), 0.9340019241005072)
X (('brew', 'teach'), 0.9337100426740735)
X (('forgets', 'pasty'), 0.9330761202808986)
X (('panicking', 'unbroken'), 0.9329257614227181)
Y (('apple', 'flavor'), 0.9325704865633547)
Y (('bertie', 'botts'), 0.9323265584758273)
Y (('pies', 'treacle'), 0.9320562646263212)
Y (('jell', 'treacle'), 0.9314715622087658)
X (('gain', 'unicorn'), 0.930614878058716)
Y (('acid', 'smoke'), 0.9302585809379584)
X (('draconis', 'portrait'), 0.9299793791668642)
Y (('lamb', 'roast'), 0.9290077092193909)
Y (('rice', 'treacle'), 0.9282944969545182)
X (('de', 'nicholas'), 0.9280626435903457)
Y (('james', 'lily'), 0.9275564243864461)
X (('dearly', 'turn'), 0.9269025891381522)
X (('stopper', 'teach'), 0.9260593618420201)
X (('balloons', 'luminous'), 0.9254512348727435)
Y (('pork', 'roast'), 0.9252807964075049)
Y (('showers', 'weather'), 0.92495648260602)
X (('fuller', 'waffle'), 0.9243021462289298)
Y (('dress', 'woman'), 0.924133897409459)
X (('flitting', 'shelves'), 0.9241052211509477)

```
