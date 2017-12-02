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

Here are some results. As you might notice they are not glorious, but seem better to me than random.
In order to train these vectors I used the first Harry Potter book (Philosopher's stone). `X` means no semantic similarity `Y` means that I see some similarity, even though the words are not exact synonyms.

```
X ((‘rabbitin', 'shoutin'), 0.9954854671625583)
Y ((‘mystery', 'unwrap'), 0.9897653928943894)
Y ((‘grinding', 'gritted'), 0.9877401049113139)
Y ((‘proudest', 'roars'), 0.9849799224637618)
X ((‘leader', 'resting'), 0.9839651974209115)
Y ((‘jk', 'rowling'), 0.9822048780315338)
Y ((‘muffins', 'toasting'), 0.9782025246444235)
X ((‘lawns', 'marched'), 0.977305634366506)
X ((‘smashed', 'square'), 0.9763058400726282)
X ((‘proudest', 'struggle'), 0.9762467087608058)
Y ((‘sardine', 'strawberry'), 0.9757154166477865)
X ((‘puffed', 'tricky'), 0.9748745239699392)
X ((‘bustling', 'shops'), 0.9740049270372261)
X ((‘sheer', 'stamps'), 0.9739588677550911)
Y ((‘fan', 'poster'), 0.9732650003347938)
X ((‘lean', 'propped'), 0.969255044610288)
Y ((‘lean', 'shrinking'), 0.969255044610288)
X ((‘lean', 'tennis'), 0.969255044610288)
Y ((‘rub', 'wipe'), 0.9685783093482921)
X ((‘frown', 'tartan'), 0.9658941624123855)
X ((‘fanatic', 'wilder'), 0.9621755066273454)
X ((‘fanatic', 'unbearable'), 0.9608970959678637)
Y ((‘mended', 'nurse'), 0.9601008053536392)
X ((‘mystery', 'video'), 0.9597125188033816)
X ((‘dormice', 'terms'), 0.9596687249151236)
Y ((‘mended', 'wax'), 0.958810123628371)
X ((‘punch', 'zooming'), 0.9575525633756854)
X ((‘forgetfulness', 'sleeping'), 0.9574607229167622)
X ((‘sheer', 'standard'), 0.9572760546436241)
X ((‘mended', 'relax'), 0.9568233087983712)
X ((‘hammer', 'mouthful'), 0.9555775928891512)
X ((‘downfall', 'everyones'), 0.9552478356934911)
X ((‘ghoulie', 'wee'), 0.9497754153491135)
X ((‘infusion', 'root'), 0.9489456135541766)
Y ((‘apple', 'chocolate'), 0.9477783608868775)
X ((‘meantime', 'tears'), 0.9475349436695042)
X ((‘confuse', 'gulpin'), 0.9473748763557878)
X ((‘confuse', 'engulfed'), 0.9473226368369153)
X ((‘confuse', 'finchfletchley'), 0.9473226368369153)
X ((‘confuse', 'harryl'), 0.9473226368369153)
X ((‘confuse', 'marshmallows'), 0.9473226368369153)
X ((‘confuse', 'tickling'), 0.9473226368369153)
X ((‘confuse', 'wellknown'), 0.9473226368369153)
X ((‘confuse', 'whatve'), 0.9473226368369153)
Y ((‘fiftyeight', 'sixtyfifth'), 0.9457694677843625)
Y ((‘fiftyeight', 'sixtyfive'), 0.9457694677843625)
Y ((‘fan', 'soccer'), 0.9456884301028985)
X ((‘granite', 'tuesday'), 0.9452541950932258)
X ((‘ghoulie', 'student'), 0.9451821742622841)
X ((‘flock', 'lock'), 0.9448757136734677)
X ((‘stranded', 'wriggled'), 0.9446513412372332)
X ((‘shelling', 'yorkshire'), 0.9445775369516817)
X ((‘related', 'wear'), 0.9442364713682097)
X ((‘exchanged', 'stunned'), 0.943468211957755)
Y ((‘pprofessor', 'suspect'), 0.9426431377373033) Interesting
X ((‘anne', 'path'), 0.9425220252830029)
X ((‘abysmal', 'magical'), 0.9415985014982612)
X ((‘shifty', 'squeaky'), 0.9411131036447853)
X ((‘grandfathers', 'sank'), 0.9409583537052726)
Y ((‘carriages', 'trunks'), 0.939339830945129)
Y ((‘hearing', 'sneaking'), 0.9382557625562312)
X ((‘lover', 'noted'), 0.9380061248324352)
X ((‘nosie', 'ronnie'), 0.9373912338638553)
X ((‘bodies', 'unraveled'), 0.9352203547870149)
X ((‘fiftyeight', 'perenelle'), 0.9345800403669805)
Y ((‘instruments', 'telescopes'), 0.934160821186669)
X ((‘druidess', 'scratching'), 0.933938970720373)
X ((‘dinnertime', 'georg'), 0.9334115078045534)
X ((‘dinnertime', 'player'), 0.9334115078045533)
X ((‘dinnertime', 'e\\'), 0.9334115078045532)
X ((‘shelling', 'tureens'), 0.933155406898148)
Y ((‘lean', 'slumped'), 0.9330132779753737)
X ((‘stain', 'tunnel'), 0.932430086123716)
X ((‘grownup', 'leathercovered'), 0.9323738271544109)
X ((‘stain', 'tunnels'), 0.9323513169994001)
X ((‘stain', 'unused'), 0.9323513169994001)
X ((‘batteredlooking', 'yew'), 0.9320146872861094)
X ((‘panting', 'teh'), 0.9301681680433297)
X ((‘panting', 'wriggles'), 0.9301681680433297)
X ((‘overtook', 'remembering'), 0.9300661544008998)
X ((‘bites', 'ways'), 0.9299751847937484)
X ((‘bearing', 'purple'), 0.9296470062533946)


```

Edit:

Run this again with the entire book, this time without stopwords and with the word window of seven words.
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