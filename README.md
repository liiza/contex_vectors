# Natural Language Processing
Teaching computer word meanings with Harry Potter

## Sematic Vectors 

In this simple demo I'm trying to understand the word semantics using context vectors.
This means each word is build a vector of with which words does the word most often appear with.
After the similar words can be found by calculating the cosine distances of their corresponding vectors.

From this imaginary example we see that words `apple` and `computer` are closer to each other than `apple` and `cat`.
As in our imaginary text we are processing, the words `apple` and `computer` often appear with `coding`, `screen` and `keyboard`,
but rarely with `cute` or `flurry`. 

```
apple : { coding : 10, screen: 9, keyboard: 7}
computer : { coding : 11, screen: 10, keyboard: 4, laptop: 5}
cat : { cute: 9, furry: 4, miau: 4}
```

Note the code is optimized for speed, not for readability!

Enough of the technic here are some results. As you might notice they are not glorius, but seem better to me than random.
In order to train these vectors I used 10000 lines of first Harry Potter book. `X` means no semantic similarity `Y` means
that I see some similarity, even though the words are not exact synonyms.

```
X (('anne', 'path'), 0.9904306610990085)(This is weird as I don't remember there being any character called Anne in the books)
Y (('proudest', 'roars'), 0.9861679722406388)
Y (('mystery', 'unwrap'), 0.9836817278972195)
Y (('muffins', 'toasting'), 0.9749246800834644)
Y (('jk', 'rowling'), 0.9729333067196286)
Y (('sardine', 'strawberry'), 0.9721183387755044)
Y (('lean', 'shrinking'), 0.9717692091180514)
Y (('fan', 'poster'), 0.9691204539907099)
X (('bustling', 'shops'), 0.9688529002880842)
X (('lawns', 'marched'), 0.9685018351227125)
X (('sheer', 'stamps'), 0.9675811808666939)
X (('mended', 'showing'), 0.963118632769093)
X (('punch', 'zooming'), 0.9628733588902264)
X (('sally', 'then'), 0.9578921392414138) (Who is sally?)
X (('cornin', 'easily'), 0.9569731914323597)
X (('dormice', 'terms'), 0.9535339035572303)
X (('perks', 'then'), 0.9532767729894875)
X (('sheer', 'standard'), 0.951306946188738)
X (('mystery', 'video'), 0.9495932281985344)
Y (('grayish', 'porridge'), 0.9480256247484838)
X (('hammer', 'mouthful'), 0.9441731284548319)
X (('direct', 'halfpast'), 0.943459477521926)
X (('frown', 'sleeve'), 0.9427911655411926)
X (('fetch', 'noticing'), 0.9418784274421746)
X (('direct', 'resist'), 0.9417335613762692)
X (('confuse', 'gulpin'), 0.9411039196120318)
Y (('apple', 'chocolate'), 0.9401256165109398)
X (('infusion', 'root'), 0.9400481885911903)
X (('confuse', 'engulfed'), 0.9398366353537789)
X (('confuse', 'finchfletchley'), 0.9398366353537789)
Y (('confuse', 'flute'), 0.9398366353537789) 
X (('confuse', 'marshmallows'), 0.9398366353537789)
X (('confuse', 'trevor'), 0.9398366353537789)
X (('related', 'wear'), 0.9395174460980105)
Y (('fan', 'soccer'), 0.9385149086352418)
X (('stranded', 'wriggled'), 0.9365425847353522)
X (('men', 'throat'), 0.9354295482015642)
X (('granite', 'tuesday'), 0.9354235428893101)
Y (('model', 'shape'), 0.9341291654793635)
X (('direct', 'incredible'), 0.9327196574979102)
X (('destiny', 'sound'), 0.9321327665980406)
X (('bearing', 'purple'), 0.9299809501856848)
X (('bath', 'possible'), 0.9296603991189218)
X (('batteredlooking', 'yew'), 0.9291948564042827)
Y (('instruments', 'telescopes'), 0.928821206887703)
X (('bundled', 'stands'), 0.9285056618125319)
X (('sailed', 'tick'), 0.9280821044512537)
X (('discovery', 'uses'), 0.9254926927032705)
X (('discovery', 'towering'), 0.9235907629204513)
X (('fascinated', 'pence'), 0.9235062780453448)
Y (('hooting', 'voice'), 0.9231440874613833)
X (('tryin', 'yehd'), 0.9227775245840028)
X (('nosie', 'ronnie'), 0.9221883380859608)
X (('druidess', 'scratching'), 0.9218389804564373)
X (('forever', 'show'), 0.9215297731378567)
X (('cutting', 'prophet'), 0.9202169607777512)
X (('toilets', 'wonder'), 0.9191428092642567)
X (('prickle', 'youknow'), 0.9178812002507757)
X (('delicately', 'faces'), 0.9178549423796394)
X (('confuse', 'leading'), 0.9175798186936084)
X (('monstrous', 'wounded'), 0.9175065083842026)
X (('boardedup', 'wrenched'), 0.916747554318271)
X (('fifth', 'gryffindors'), 0.9164857639432858)
Y (('curtain', 'hid'), 0.9152015998670289)
X (('currently', 'order'), 0.9144308727394419)
X (('dinnertime', 'georg'), 0.9144231617762363)
X (('dinnertime', 'player'), 0.9144231617762363)
X (('dinnertime', 'e\\'), 0.9144231617762362)
X (('atta', 'less'), 0.9139002952792921)
X (('goggle', 'nasty'), 0.9138576171239867)
X (('positions', 'string'), 0.9137088212291963)
X (('atta', 'less'), 0.9139002952792921)
X (('goggle', 'nasty'), 0.9138576171239867)
X (('positions', 'string'), 0.9137088212291963)
X (('drafts', 'fungi'), 0.913427018524212)
X (('hoggy', 'hogwarts'), 0.9133144908215072)
X (('fluff', 'pelt'), 0.9112289697577366)
X (('nitwit', 'thank'), 0.911188758368588)
X (('exchanged', 'eyebrows'), 0.910990431813295)
Y (('grinding', 'tongue'), 0.9095501883688343)
X (('aaah', 'has'), 0.9095208384645818)
X (('confed', 'warlock'), 0.9094360235546426)
X (('awe', 'stern'), 0.9088425486611695)
Y (('monstrous', 'threeheaded'), 0.9085082215916175)
X (('monstrous', 'neighbors'), 0.9085082215916174)
X (('village', 'walled'), 0.908384756270393)
X (('village', 'wit'), 0.908384756270393)
X (('seizing', 'sharp'), 0.9076621275672881)
X (('phials', 'set'), 0.907613854414568)
X (('rub', 'taste'), 0.9075222556525648)
Y (('raged', 'ragged'), 0.907515936002454)
X (('prodding', 'west'), 0.9071650063592546)
X (('panting', 'teh'), 0.9070677878098894)
X (('panting', 'wriggles'), 0.9070677878098894)
X (('bravo', 'oh'), 0.906943889151794)
X (('board', 'clock'), 0.9063563052572118)
Y (('limping', 'wing'), 0.9060272072760799)
X (('overhearing', 'trusting'), 0.9058704843963539)
X (('sigh', 'wildlooking'), 0.9057263373135075)
X (('overtook', 'remembering'), 0.9056310506482719)
X (('tackling', 'twelvefoot'), 0.9056129006477551)
X (('destiny', 'puffing'), 0.9052551186090101)
X (('jeans', 'tape'), 0.9046322339579813)
Y (('brandnew', 'wore'), 0.904275963782606)
X (('destiny', 'prefects'), 0.9039150407811526)
X (('positions', 'puff'), 0.903458876714911)
X (('bowling', 'music'), 0.9033172223719995)
X (('considered', 'greatest'), 0.9031228098762938)

```
