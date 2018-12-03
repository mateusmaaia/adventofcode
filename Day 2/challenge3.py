# --- Day 2: Inventory Management System ---
# You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

# Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

# "Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

# Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

# To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

# For example, if you see the following box IDs:

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

# What is the checksum for your list of box IDs?

puzzleInputDay2 = ("umdryebvlapkozostecnihjexg","amdryebalapkozfstwcnrhjqxg","umdcyebvlapaozfstwcnihjqgg","ymdryrbvlapkozfstwcuihjqxg","umdrsebvlapkozxstwcnihjqig","umdryibvlapkohfstwcnfhjqxg","umdryebvqapkozfatwcnihjqxs","umzrpebvlapkozfshwcnihjqxg","fmhryebvlapkozfstwckihjqxg","umdryebvlahkozfstwcnizjrxg","qmdryebvlapkozfslwcnihgqxg","umdiyebjlapknzfstwcnihjqxg","umdryebvlapkoqfstwcaihvqxg","cmdryebvlapkpzfstwcnihjvxg","umdryebvlakkozfstwcgihjixg","umdryebvlasjozfstwcnihqqxg","umdryebvladkozfsvwcnifjqxg","umdrlebvlapaozfstwcniwjqxg","umdryebvlhpkozrstwsnihjqxg","umdryebvcapkozfqtwcnihjrxg","ubdrykbvlapkowfstwcnihjqxg","umdryebvldpkozfstwcnihtqsg","umdryebvlapaozyutwcnihjqxg","umdryibvlapkozfstdfnihjqxg","umdryebvlapgozkstwznihjqxg","umdrxebvlapkozfstwcngxjqxg","umdryekvlapkozfstwclchjqxg","nmdryebvlapkozjsewcnihjqxg","umdryebvyapkozfstfcniheqxg","umdfyebvlapkozfstwcnhhjpxg","umdryelylupkozfstwcnihjqxg","smdryebvlqpkozfstwcnihjdxg","umdryebvlapaozfsuwcnihjqxc","umdryebvlrzkozrstwcnihjqxg","umdbycbvlapkojfstwcnihjqxg","umdryebvlapkonfstwpnirjqxg","uecryebvlapkozfstwcnihpqxg","uqdryebvltpkozfstwcnihrqxg","umdryebvlqsknzfstwcnihjqxg","cmdryebvlapkocfstwcvihjqxg","umdrkebvlapkozqsfwcnihjqxg","umdryabveapkoifstwcnihjqxg","ummrnehvlapkozfstwcnihjqxg","umdryebvlxpkozfstwqnihjtxg","umdryebvlagkozastwcnihjqxh","umdryebvlatkozzhtwcnihjqxg","umdryebvlcpkozfstwrnihjqvg","umdryebvlapkozfsnwcnrhjcxg","umdzyebvlypkozfstwcnibjqxg","nmdryebvlvpkozbstwcnihjqxg","uwdryebvlipkozfstwcnihvqxg","umdraebvlavkozfstwcnihjqwg","umdeyebvlspbozfstwcnihjqxg","umdryxlvlapkozfstwcnihjqxu","umdryegvlapkqzfstwcnirjqxg","umdrupbvlapkozfstwcnihjqog","imxryebvlapkxzfstwcnihjqxg","umdrfebvlapkozowtwcnihjqxg","umdreebvlapkozmstwczihjqxg","undryebdlapkozbstwcnihjqxg","umdryebvlapkpzfetwcnihjqxb","ymdnyebvlapkozfstwinihjqxg","umdryebvaapkozfstwcnihyqqg","umdryebvlapkzzwsrwcnihjqxg","umdrkebvlapkmzfskwcnihjqxg","umdrmebvlapkozfsvwcnidjqxg","umdlyehvlapkozfstwcnihjqkg","umnryebvlrpkozfstwjnihjqxg","uqdryebvlapxozfsawcnihjqxg","vmdruebvlapkozfstwcnihjqqg","umdryabviapkozistwcnihjqxg","umdryebvlapkzzfstwfnihkqxg","uvdryebvlapkozfsxwcuihjqxg","umdlhebvlapkozfstwcnvhjqxg","umdreebvlapkopfstjcnihjqxg","umdryebvlazkomfstwynihjqxg","kmdryebulapkoznstwcnihjqxg","umdryebvxakkozfstwinihjqxg","ukdryobvlapkozistwcnihjqxg","umdryebveapkozfstwcnthjqgg","mmdrtebvlapcozfstwcnihjqxg","umdryebvlapkolistwnnihjqxg","umdryebxlapkozfatwcnihjqxx","uxdryebvlapkozfstwhniheqxg","ufdryebvzapkozfstwcnbhjqxg","amdryhbvlapkozfstwcnifjqxg","umqryebvlaphozfstwcnihjqxn","umdryebvlapkosfstfcnihjqxe","gmkryebvlapkozfstwcnihjmxg","umdrnebvlkpkozfstwcnihjnxg","umdryebvrapkozfstmcndhjqxg","umdryebvmapkozfstichihjqxg","umdryesvnapkozestwcnihjqxg","umeryhbvlapkozfstfcnihjqxg","umdryedvbapkozfstwcnihqqxg","umdryebllapzozfstwcnihjvxg","umdcyebvlzdkozfstwcnihjqxg","umdrybbvlapkbvfstwcnihjqxg","umdrytbglapkozfsthcnihjqxg","umdryebvlkpkozfsteclihjqxg","umdntebvlapkmzfstwcnihjqxg","lkdryebveapkozfstwcnihjqxg","ymdryubvlapkozfstwbnihjqxg","tmrryebvlapkozfstwcnqhjqxg","umdryeovlaekonfstwcnihjqxg","umiryeuvlapkozfstwcnihjwxg","umdryebvlspvozwstwcnihjqxg","umdrtebvlapkoznxtwcnihjqxg","umvryebvlaphozfstwcnahjqxg","umdryebvlapkozfstinniajqxg","umdryebqlapkozfctwcnihjqxx","umdryebvlapkbzfptwcnihjqvg","umdryabviapkozistwcnihjqxd","umdryrbvlapkezfstscnihjqxg","umhryebvlapkozfstacnihxqxg","umdxyelvlapkozfitwcnihjqxg","umdryevvuapkozfstwcnihtqxg","uydrypbvxapkozfstwcnihjqxg","umdryebvlapkopfstwcnihzqxo","uedryebvlapkozistwceihjqxg","umdiyebvlapkozfgtwcnihjqxv","ymdryebvlapkozfsticniqjqxg","umbrkebvlapkozfslwcnihjqxg","umdryebliapkozbstwcnihjqxg","umvryebolapkozfstwcnihjqig","umdryeavbackozfstwcnihjqxg","umdryfbvlapsozfstwcnihaqxg","umdqyebvlapkozfjtgcnihjqxg","umdrjebvlaqkozfstwcyihjqxg","umdryebklaqkozrstwcnihjqxg","umdryebvpapkozfstwcpihjqjg","uydryebhlawkozfstwcnihjqxg","umdyyebvlapkozfstwcykhjqxg","umdryebvlapkozfstwcnitjnxh","umdzyebvlapkozfstwcnehyqxg","mmcryebvlapkozfstwinihjqxg","umdryebvlapuozfstwmvihjqxg","umdryfbvlapkozqstwcnihjmxg","umdryebslapsozfhtwcnihjqxg","umdtyemvlapmozfstwcnihjqxg","umdrxevvlapkozfytwcnihjqxg","umdahebvlapjozfstwcnihjqxg","umdryebvlapkozfstacnivjqxb","umdryebvlzpkozfjtwcnihjyxg","umdryebvlaqkozfstwcnisjqxu","umdrydbvlapkozfsuwcnihjlxg","umdryebvlapkomrstwcnihjqkg","umdryebvlapcozfstmcnwhjqxg","umdryebvlahkozfstwcibhjqxg","gmdrzebvlapkozlstwcnihjqxg","umdryebvlapkezfsswcnrhjqxg","umdryebvlapkoqfitwcgihjqxg","umdrnebvlapkozfsiwcninjqxg","umdryebvlapkozfsrwckohjqxg","umdryebtlapkomfstwcnihjexg","umdryxbvlapjozfstwcnihoqxg","umdpyebvlapkosustwcnihjqxg","umdryebvlapkvzfawwcnihjqxg","umhnyebvlaikozfstwcnihjqxg","umdryebvlagkozfstvknihjqxg","uodryebjlapkoxfstwcnihjqxg","umdryefdlapkozfstwcnyhjqxg","umprmebvtapkozfstwcnihjqxg","umdhyebvlapoozfstwcnihjqgg","uddryebvidpkozfstwcnihjqxg","umdryebtlapkozfetwfnihjqxg","umdbyebolapkozfstwcoihjqxg","umdryebvlapkonfstwcnihjpxo","umdryebvlapkohfstwcnihjqwk","umdryebolalkkzfstwcnihjqxg","updryebvxapkozfstwcnshjqxg","umdryebvlapkovfktwcnuhjqxg","umdrqrbvlppkozfstwcnihjqxg","umdrylgvlapkozfstwrnihjqxg","umdryebvlapkozfstxcnihbqig","uvdryeevlappozfstwcnihjqxg","zmdryebvlapkozfstwcnihqqxt","umdryebvlapvozfstwenihiqxg","umdryebvlbpkozfsgwcnihjlxg","umdryhbvlapkozfstwcnihtqxw","umdreecvlapkozwstwcnihjqxg","umwryebvlapkoztsmwcnihjqxg","ukdryebvfapkozrstwcnihjqxg","umdrylbdlamkozfstwcnihjqxg","umdryebvlapoozwsmwcnihjqxg","umdryebvlapkozfqtwcnnzjqxg","umdryekvlapktzfstwcnohjqxg","umdryebvlapkozfstwcnihjwqo","umdrrebflapkogfstwcnihjqxg","umdryevvlapkozfztwctihjqxg","umdrybbvlapkozfstwcnihxaxg","umdryebvlapkozfsowcnphjqag","smdryebvlapbozfitwcnihjqxg","umdryebvtapiozfstwcnihjqxe","umdryebjlakkozfstwccihjqxg","umdryebvlapdozfshwckihjqxg","umnryebvlapiozfstwcnihlqxg","umdrycbvlapkjzfsnwcnihjqxg","umdryebvyaprozjstwcnihjqxg","ucdryebvlapkozfstwomihjqxg","umdryebvlagklzfstwcnihjqyg","umdryebvladkozfstwcnihjqjh","umdrwebvlapkozfstwdnicjqxg","umdryebvlapkmzfstwcniheqxr","umdryebvlapkjzfstwcviheqxg","umdrvebvlapkozfstwcbihjqmg","umdrfebvlapkoffstwcnihsqxg","umdryebvtarkazfstwcnihjqxg","umdryebvlapkozfstwcfihjcng","umdryebvlapkktostwcnihjqxg","uedryeevlapkozfstwcniijqxg","bmdryebylapkozfstwcnihjqog","umdryebvlmpkoztstwcnihjqeg","umdryepvlarkohfstwcnihjqxg","uwdryebvlapklzfstzcnihjqxg","umdryebklapkozfsswcbihjqxg","umdtyeavlapkozfstwsnihjqxg","umdryebvaapkozfhtfcnihjqxg","umdrpebvlapuozfstwvnihjqxg","umdryebvlapkozffmwcniijqxg","uqdpyebvlapkozfstwfnihjqxg","umdryebvlapuozdstwcnihjhxg","tmdryhbvlapkozfptwcnihjqxg","umdryevvmapkozfstwcnihjgxg","umdryeuvlapmozfstwcnihjwxg","umdryebqlzpkozfbtwcnihjqxg","umdryebvsapkozystwcniqjqxg","imdryebvlapkozfscwinihjqxg","umdryebvlzpkozustwcnmhjqxg","umdrypbvlapbozfsnwcnihjqxg","bmdryebvlapqoznstwcnihjqxg","umdrfebvlapaozfstwcnihxqxg","umdiyebvxapkozfstwcnchjqxg","umdrygbvlapkozfstwcnizjqxz","amdryedvlapkozfstwcnihfqxg","umdryebvvapzozfstwcnihjgxg","undryebvlapkzzfstjcnihjqxg","umdryvbvlapgozfrtwcnihjqxg","umdrkebvlapkozfstwcnihihxg","umdryebvrppkozfsowcnihjqxg","umdryebvlapktzfsdwclihjqxg","otdrdebvlapkozfstwcnihjqxg","mmdryebvlazkozfxtwcnihjqxg","umdryebvlapkozfsbwtnihjqxa","imqryebvrapkozfstwcnihjqxg","umdryebvlrpkozfscwcnihjqlg","uedryebvlapkoznsvwcnihjqxg","umdryebvlqpkozfstscnihjqxj","umerycbvlapkozfstwcnihjqxh","umdkykbvlapjozfstwcnihjqxg")

def santaClausChecksum(inputDay2):
    twoCount = threeCount = 0
    for value in inputDay2:
        letters = list(set(value))
        twoOnce = threeOnce =False

        for eachLetter in letters:
            count = value.count(eachLetter)
            if count == 2 and twoOnce == False:
                twoCount += 1
                twoOnce = True
            elif count == 3 and threeOnce == False:
                threeCount += 1
                threeOnce = True

    return(twoCount * threeCount)

print(santaClausChecksum(puzzleInputDay2))