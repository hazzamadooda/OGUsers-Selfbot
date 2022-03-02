from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc
import time, random, os

connected = False
#Values to input
#How many messages
total_messages = 1
i = 0
#Username
username = ""
#password
password = ""
#Website reply (MUST ONLY REPLY TO THE MAIN POST)
reply_link = ""
#Full Message (Message has been successfully sent as:" sparkle oval laugh "! The program has been running for 20 itterations! Only 0 left!) = True ||||||| OR ||||||| (5 itterations left) = False
full_message = False
list_of_random_words = ["swanky","berry","gifted","water","painful","anger","rapid","instinctive","manage","breezy","moldy","curvy","hop","unarmed","pickle","middle","stupid","idiotic","gaping","friend","pancake","launch","puzzling","soothe","awful","tasteful","sore","overflow","linen","steel","curved","abrupt","explain","rabbit","hard-to-find","stuff","chivalrous","ethereal","buzz","highfalutin","moor","cynical","flock","doubt","vulgar","typical","rustic","appear","feeble","squeamish","sip","hall","care","chance","donkey","chilly","thank","absorbed","improve","grain","scrape","separate","reminiscent","zip","jar","disastrous","hand","contain","bruise","subtract","wet","cooperative","thumb","bumpy","easy","discovery","threatening","chew","straw","tumble","cry","maniacal","gusty","icy","cheese","settle","tame","toothsome","guarantee","waves","list","regular","harsh","purple","upset","stay","dramatic","tough","sleet","surprise","unable","fasten","permit","strip","burn","kitty","second","rejoice","substance","increase","alike","judicious","actor","marvelous","chase","wander","shoes","tacky","cross","beautiful","transport","happy","capricious","pushy","repulsive","furniture","habitual","file","boiling","excellent","sink","unruly","closed","subsequent","grieving","keen","pot","harmony","divergent","zippy","sound","reject","street","stranger","day","guttural","puny","pastoral","grade","spiritual","sand","mice","towering","unadvised","shiver","worthless","industry","tired","acoustics","belong","fear","alive","adaptable","ill-fated","sparkle","hideous","ink","cheap","temper","duck","bed","own","bury","home","ice","brown","party","current","snakes","sky","snotty","control","barbarous","placid","texture","nutty","badge","flame","harmonious","vacuous","purring","garrulous","daughter","lean","diligent","null","decisive","thrill","bump","near","elastic","super","cake","jittery","painstaking","attract","plastic","kind","stormy","learned","thick","electric","zipper","division","brief","true","sweater","poison","nonchalant","good","difficult","art","fertile","first","ashamed","incredible","telephone","long-term","multiply","trap","idea","call","fixed","ceaseless","rinse","public","gainful","excuse","horse","daffy","obese","degree","sweltering","drain","fluttering","meddle","slope","odd","breath","relation","spotty","consider","intelligent","groovy","bored","lettuce","store","action","sulky","skirt","silk","necessary","accidental","lucky","rub","skillful","knot","grey","connection","languid","impress","used","park","try","irate","dolls","apparatus","punch","angle","pet","needle","worm","crayon","frighten","teeth","chief","measly","copper","x-ray","sofa","half","territory","hurt","utopian","scary","press","zealous","fair","clear","adventurous","advertisement","smash","wakeful","force","wicked","perform","delirious","disgusting","downtown","unpack","fry","curl","magic","low","dance","careless","thoughtful","goofy","grass","string","preserve","men","waiting","glossy","harm","oceanic","drink","fit","doctor","change","overt","crawl","spoil","synonymous","capable","secretary","nostalgic","kick","freezing","dynamic","faint","aboriginal","float","hover","pencil","mammoth","wooden","adjoining","monkey","shop","flippant","shivering","drab","somber","compare","well-off","sheep","horses","tiger","teeny","hammer","muscle","hobbies","round","spill","homely","tall","long","bottle","tiresome","lacking","important","plant","box","spurious","repeat","welcome","brainy","knife","guitar","show","selection","blind","discreet","anxious","macho","disappear","name","knit","evasive","perfect","tart","sable","grab","found","hateful","boring","defiant","far","grate","eminent","frequent","dizzy","bustling","cars","elderly","lick","uppity","suspend","precious","laugh","valuable","smooth","cellar","delight","different","meek","many","groan","sophisticated","dead","field","invent","lavish","motion","concentrate","excited","value","silent","flimsy","visit","toes","writer","hurry","maid","borrow","tire","base","sour","charming","cooing","abashed","macabre","shock","damaged","hill","reading","annoyed","doubtful","protest","impossible","mist","cheerful","afford","scatter","switch","sneaky","irritating","inject","frame","jam","cream","metal","listen","frightened","weight","quilt","cure","pause","heap","wealth","humorous","forgetful","possess","tangible","enchanted","sponge","actually","reward","introduce","earth","drip","abandoned","ball","irritate","teeny-tiny","rambunctious","dangerous","ship","recess","wing","impartial","nervous","radiate","nasty","certain","wacky","slim","quixotic","chin","paint","achiever","health","bleach","baseball","woman","level","tempt","economic","soup","vagabond","swim","damage","impolite","smile","replace","foot","explode","record","tacit","hands","juggle","meal","shirt","yell","income","nonstop","satisfy","report","deeply","amusement","neighborly","acceptable","knee","scribble","early","combative","outstanding","industrious","bells","coal","deserted","weak","march","animated","examine","zebra","island","amuck","share","sack","deep","insurance","opposite","scrawny","holistic","mix","efficient","slip","white","land","pleasure","education","rule","gigantic","male","burly","travel","waste","exist","yellow","lethal","imagine","smiling","squealing","minute","carpenter","bubble","new","weigh","flight","utter","haircut","office","wound","didactic","tip","rush","stop","lovely","glib","two","fumbling","imminent","comparison","pig","inconclusive","possessive","abiding","flower","heady","lunchroom","consist","measure","sleepy","quack","beg","wipe","cluttered","heavenly","zoo","gabby","vengeful","oval","arithmetic","bit","wine","sordid","wiry","road","town","grease","mug","clover","thought","disarm","cause","ruddy","love","vigorous","short","toothbrush","voyage","standing","plan","absorbing","illegal","quiet","friction","longing","cook","fierce","week","collar","dare","board","befitting","vanish","pies","pine","dull","attack","malicious","high-pitched","nutritious","holiday","rock","wish","airplane","aware","rabbits","thirsty","army","astonishing","payment","heal","attempt","language","awesome","yak","confused","tooth","pointless","bitter","point","succeed","hat","toothpaste","scandalous","helpful","expert","annoy","twist","unequaled","observant","daily","kettle","north","fast","card","unknown","itch","fang","well-groomed","wriggle","historical","instruct","want","bee","start","interfere","hypnotic","excite","knowing","creature","shave","damaging","cultured","loose","scissors","sloppy","clumsy","stiff","dress","iron","club","descriptive","mysterious","fire","great","itchy","shocking","depend","perpetual","jaded","warn","protective","rail","whole","extend","voracious","observation","weary","hollow","houses","lame","rhythm","experience","approve","cobweb","mind","late","extra-large","queen","divide","dashing","condemned","fork","craven","toys","enchanting","night","sense","ski","adhesive","behavior","basket","group","spicy","cherry","wonderful","strap","suspect","bomb","woozy","rely","inexpensive","babies","seal","sweet","scientific","selfish","competition","tramp","melted","royal","stone","selective","popcorn","shallow","desire","detailed","halting","nut","kneel","theory","can","soak","plausible","bent","blink","greasy","pretend","whip","disturbed","medical","crash","team","temporary","ablaze","glamorous","vacation","psychotic","injure","substantial","nebulous","acidic","development","push","talk","belief","victorious","brash","clammy","polish","high","quaint","identify","ignorant","mellow","rhetorical","morning","needless","tedious","ear","woebegone","fish","reduce","class","provide","pleasant","authority","hunt","well-made","yard","unsuitable","scarf","run","nondescript","abortive","workable","noiseless","cute","decay","double","nappy","tour","blow","nifty","rough","structure","crack","squeal","yummy","guard","futuristic","outrageous","tongue","blue-eyed","zinc","large","trot","overconfident","sisters","youthful","curve","defective","whine","relieved","bucket","treatment","famous","puncture","sea","broad","foregoing","earthquake","delicious","analyze","soggy","ban","red","window","accurate","receipt","salty","alert","repair","preach","time","calm","omniscient","blade","fallacious","coast","chunky","lamentable","unhealthy","loud","phone","eager","tight","pipe","false","trite","tomatoes","pizzas","billowy","suppose","neat","range","invention","owe","son","graceful","recognise","angry","paste","stick","caring","head","promise","blue","optimal","legs","roomy","careful","trust","throne","jelly","thankful","playground","gold","military","spot","mushy","humor","purpose","lumpy","argument","shame","growth","amazing","dislike","exuberant","shelf","fruit","regret","suggestion","physical","screw","system","bait","versed","dog","seashore","beginner","subdued","soft","heat","fly","view","shy","car","wreck","fence","elbow","harass","death","fetch","productive","complex","admire","leg","yawn","connect","earthy","activity","resonant","command","dispensable","grateful","price","count","encourage","cherries","tent","solid","attach","auspicious","joke","applaud","sheet","tease","unsightly","naughty","treat","shade","therapeutic","obey","root","cough","wax","cow","undress","untidy","dazzling","laughable","obsequious","scattered","wary"]

def startup_questions():
    global username
    global password
    global reply_link
    global full_message
    global total_messages
    os.system("clear")
    print("""
██╗  ██╗░░██╗░█████╗░███████╗███████╗░█████╗░  ██╗
██║  ██║░░██║██╔══██╗╚════██║╚════██║██╔══██╗  ██║
██║  ███████║███████║░░███╔═╝░░███╔═╝███████║  ██║
╚═╝  ██╔══██║██╔══██║██╔══╝░░██╔══╝░░██╔══██║  ╚═╝
██╗  ██║░░██║██║░░██║███████╗███████╗██║░░██║  ██╗
╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝  ╚═╝
""")
    print("Note: use a key-scramber if you are worried about your account being compromised\n\n\n")
    question_1 = input("Please enter your OGUsers Username: ")
    username = question_1
    question_2 = input("Please enter your OGUsers Password: ")
    password = question_2
    question_3 = input("Please enter the 'Reply to post' URL: ")
    reply_link = question_3
    question_4 = input("Would you like full updates (Y) or short updates (N): ")
    question_4_bool = False
    while question_4_bool == False:
        if question_4 == "y":
            full_message = True
            question_4_bool = True
        elif question_4 == "n":
            question_4_bool = True
            full_message = False
        else:
            question_4 = input("Please only input (y) or (n): ")
    question_5 = input("How many replies do you want (Numbers only): ")
    question_5_bool = False
    while question_5_bool == False:
        if question_5.isdigit():
            question_5_bool = True
            total_messages = question_5
        else:
            question_5 = input("How many replies do you want (NUMBERS ONLY): ")


    os.system("clear")
    print("""
██╗  ██╗░░██╗░█████╗░███████╗███████╗░█████╗░  ██╗
██║  ██║░░██║██╔══██╗╚════██║╚════██║██╔══██╗  ██║
██║  ███████║███████║░░███╔═╝░░███╔═╝███████║  ██║
╚═╝  ██╔══██║██╔══██║██╔══╝░░██╔══╝░░██╔══██║  ╚═╝
██╗  ██║░░██║██║░░██║███████╗███████╗██║░░██║  ██╗
╚═╝  ╚═""")
    loginfunction()





def end_function():
    print("Your message has successfully been sent", str(total_messages), "times!")
    quit()

def loginfunction():
    global driver
    driver = uc.Chrome(use_subprocess=True)
    driver.get('https://ogusers.com/login')
    connected = False
    while not connected:
        time.sleep(5)
        try:
            email_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]')
            email = username
            for letter in email:
                email_input.send_keys(letter)
                wait_time = random.randint(0,100)/1000
                time.sleep(wait_time)
            conncted = True

            password_input = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Password"]')
            for letter in password:
                password_input.send_keys(letter)
                wait_time = random.randint(0,100)/1000
                time.sleep(wait_time)

            driver.find_element(By.CSS_SELECTOR,'button').click()
            connected = True
            replyfunction()
        except:
            time.sleep(5)
            driver.get('https://ogusers.com/login')

def replyfunction():
    global i
    while i != total_messages:
        word_string = []
        driver.get(reply_link)
        if int(i) == int(total_messages):
            end_function()
        try:
            iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
            driver.switch_to.frame(iframe)
            text_box = driver.find_element(By.XPATH, "//html/body/p")
            for b in range(0,random.randint(1,5)):
                word_string.append(list_of_random_words[random.randint(0,1010)])
            message = (' '.join(word_string))
            for letter in message:
                text_box.send_keys(letter)
                wait_time = random.randint(0,250)/1000
                time.sleep(wait_time)
            driver.switch_to.default_content()
            time.sleep(0.5)            
            driver.find_element(By.CSS_SELECTOR,'[value="Post Reply"]').click()
            i += 1
            if full_message == True:
                os.system("clear")
                print("""
██╗  ██╗░░██╗░█████╗░███████╗███████╗░█████╗░  ██╗
██║  ██║░░██║██╔══██╗╚════██║╚════██║██╔══██╗  ██║
██║  ███████║███████║░░███╔═╝░░███╔═╝███████║  ██║
╚═╝  ██╔══██║██╔══██║██╔══╝░░██╔══╝░░██╔══██║  ╚═╝
██╗  ██║░░██║██║░░██║███████╗███████╗██║░░██║  ██╗
╚═╝  ╚═""")
                print("Message has been successfully sent as:\"", message + " \"! The program has been running for", str(i) , "itterations! Only", str(int(total_messages) - int(i)), "left!")
            else:
                os.system("clear")
                print("""
██╗  ██╗░░██╗░█████╗░███████╗███████╗░█████╗░  ██╗
██║  ██║░░██║██╔══██╗╚════██║╚════██║██╔══██╗  ██║
██║  ███████║███████║░░███╔═╝░░███╔═╝███████║  ██║
╚═╝  ██╔══██║██╔══██║██╔══╝░░██╔══╝░░██╔══██║  ╚═╝
██╗  ██║░░██║██║░░██║███████╗███████╗██║░░██║  ██╗
╚═╝  ╚═""")
                print("There are", str(int(total_messages) - int(i)), "itterations left.")
            time.sleep(7)
        except:
            time.sleep(1)
            driver.get(reply_link)


startup_questions()




