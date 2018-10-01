#FWI Test
#Test Written by Min Choi and Nicholas Eickhoff
#Developed by Min Choi, Ashmita Sarma, Nicholas Eickhoff, Lokesh Nasaka

alphabet=['A','B','C','D','E','F','G','H','I']

class Test:
    def __init__(self):
        self.__QuestionArray=[] #array of questions
        self.__Tumblr=0
        self.__Instagram=0
        self.__Reddit=0
        self.__QuestionNumber=1
        self.__NoOfQuestions=0
    def addQuestion(self,adding):
        self.__QuestionArray.append(adding)
        self.__NoOfQuestions+=1
    def getNoOfQuestions(self):
        return self.__NoOfQuestions
    def nextQuestion(self):
        self.__QuestionNumber+=1
    def getQuestionNumber(self):
        return self.__QuestionNumber
    def askQuestion(self):
        print("")
        print("Question #"+str(self.__QuestionNumber))
        pointsDict= {"Answered": False}
        while (pointsDict["Answered"]==False):
            pointsDict = Question.ask(self.__QuestionArray[Test.getQuestionNumber(self)])
            if pointsDict["Answered"]==False:
                print("Not a valid answer. Try Again.")
                print("")
        self.__Tumblr+=pointsDict["Tumblr"]
        self.__Instagram+=pointsDict["Instagram"]
        self.__Reddit+=pointsDict["Reddit"]
        Test.nextQuestion(self)
    def getResults(self):
        total=self.__Tumblr+self.__Instagram+self.__Reddit
        tp=self.__Tumblr/70
        ip=self.__Instagram/53
        rp=self.__Reddit/83
        myScore=tp-rp
        print("")
        if (tp>rp and tp>ip):
            print("Party: Tumblr")
        elif (rp>ip):
            print("Party: Reddit")
        else:
            print("Party: Instagram")
        ip=ip/10
        if (myScore>0):
            myScore=myScore-ip
            myScore*=100
            myScore=round(myScore)
            print("You are "+str(myScore)+" points to the left.")
        elif (myScore<0):
            myScore*=-1
            myScore=myScore-ip
            myScore*=100
            myScore=round(myScore)
            print("You are "+str(myScore)+" points to the right.")
        else:
            print("You are exactly in the middle of the FWI spectrum.")


class Question:
    def __init__(self, content):
        self.__content=content
        self.__answers=[]
        self.__answered=False
        self.__NoOfAnswers=0
    def ask(self): #return dictionary object
        BigBuckHD={
        "Tumblr": 0,
        "Reddit": 0,
        "Instagram": 0,
        "Answered": False
        }
        print(self.__content)
        choice=0
        for m in self.__answers:
            print(alphabet[choice]+") "+Answer.getContent(m))
            choice+=1
        answer=str(input("Enter Choice: "))
        answer=answer.upper()
        try: #fourth value in dictionary sets boolean of whether question was answered
            ooferGang=alphabet.index(answer) #alphabet index
            if ooferGang<self.__NoOfAnswers:
                BigBuckHD["Answered"]=True
                DabberGang=Answer.getBigBuckEl_BurritoLoco(self.__answers[ooferGang])
                BigBuckHD["Tumblr"]=DabberGang["Tumblr"]
                BigBuckHD["Reddit"]=DabberGang["Reddit"]
                BigBuckHD["Instagram"]=DabberGang["Instagram"]
            return BigBuckHD
        except:
            return BigBuckHD
        return
    def addAnswer(self,answerc):
        self.__answers.append(answerc)
        self.__NoOfAnswers+=1

class Answer:
    def __init__(self,content, T, I, R):
        self.__content=content
        self.__T=T
        self.__I=I
        self.__R=R
    def getBigBuckEl_BurritoLoco(self):
        jukerGang = {
        "Tumblr": self.__T,
        "Reddit": self.__R,
        "Instagram": self.__T
        }
        return jukerGang
    def getContent(self):
        return self.__content

def takeFWI():
    RTI=Test()
    q2=Question("What is your favorite social networking site?")
    a10=Answer("Facebook or Twitter", 0, 1, 0)
    Question.addAnswer(q2, a10)
    a11=Answer("Tumblr", 2, 0, 0)
    Question.addAnswer(q2, a11)
    a12=Answer("Reddit", 0, 0, 2)
    Question.addAnswer(q2, a12)
    a13=Answer("Instagram", 0, 2, 0)
    Question.addAnswer(q2, a13)
    a14=Answer("4chan or 8chan", 0, 0, 3)
    Question.addAnswer(q2, a14)
    a15=Answer("Snapchat", 0, 2, 0)
    Question.addAnswer(q2, a15)
    a16=Answer("Other", 0, 0, 0)
    Question.addAnswer(q2, a16)
    Test.addQuestion(RTI, q2)
    q3=Question("Do you use Snapchat on a regular basis?")
    a17=Answer("Yes", 0, 2, 0)
    Question.addAnswer(q3, a17)
    a18=Answer("No", 0, 0, 1)
    Question.addAnswer(q3, a18)
    Test.addQuestion(RTI, q3)
    q4=Question("Do you use Tumblr on a regular basis?")
    a19=Answer("Yes", 2, 0, 0)
    Question.addAnswer(q4, a19)
    a20=Answer("No", 0, 0, 0)
    Question.addAnswer(q4, a20)
    Test.addQuestion(RTI, q4)
    q5=Question("Do you use Pinterest on a regular basis?")
    a21=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q5, a21)
    a22=Answer("No", 0, 0, 0)
    Question.addAnswer(q5, a22)
    Test.addQuestion(RTI, q5)
    q6=Question("Do you use Instagram on a regular basis?")
    a23=Answer("Yes", 0, 2, 0)
    Question.addAnswer(q6, a23)
    a24=Answer("No", 0, 0, 1)
    Question.addAnswer(q6, a24)
    Test.addQuestion(RTI, q6)
    q7=Question("Do you frequently read and leave ratings for YouTube comments?")
    a25=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q7, a25)
    a26=Answer("No", 0, 1, 0)
    Question.addAnswer(q7, a26)
    Test.addQuestion(RTI, q7)
    q8=Question("Do you use Reddit on a regular basis?")
    a27=Answer("Yes", 0, 0, 2)
    Question.addAnswer(q8, a27)
    a28=Answer("No", 0, 0, 0)
    Question.addAnswer(q8, a28)
    Test.addQuestion(RTI, q8)
    q9=Question("Do you use 4chan or other anonymous forums on a regular basis?")
    a29=Answer("Yes", 0, 0, 3)
    Question.addAnswer(q9, a29)
    a30=Answer("No", 0, 0, 0)
    Question.addAnswer(q9, a30)
    Test.addQuestion(RTI, q9)
    q10=Question("Do you identify with most people in your generation?")
    a31=Answer("Yes", 0, 2, 0)
    Question.addAnswer(q10, a31)
    a32=Answer("No", 1, 0, 1)
    Question.addAnswer(q10, a32)
    Test.addQuestion(RTI, q10)
    q11=Question("Do you use, watch or read Buzzfeed on a regular basis?")
    a33=Answer("Yes", 1, 1, 0)
    Question.addAnswer(q11, a33)
    a34=Answer("No", 0, 0, 1)
    Question.addAnswer(q11, a34)
    Test.addQuestion(RTI, q11)
    q12=Question("Are people these days too sensitive and easily offened?")
    a35=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q12, a35)
    a36=Answer("No", 1, 0, 0)
    Question.addAnswer(q12, a36)
    Test.addQuestion(RTI, q12)
    q13=Question("What is your stance on the Black Lives Matter Movement?")
    a37=Answer("Full-Support their ideas and methods of purpose", 2, 0, 0)
    Question.addAnswer(q13, a37)
    a38=Answer("Support, but not all their methods of protest", 0, 1, 0)
    Question.addAnswer(q13, a38)
    a39=Answer("Neutral/Unfamiliar", 0, 0, 1)
    Question.addAnswer(q13, a39)
    a40=Answer("Against, All Lives Matter", 0, 0, 2)
    Question.addAnswer(q13, a40)
    a41=Answer("Against, what the movement stands for is wrong", 0, 0, 2)
    Question.addAnswer(q13, a41)
    Test.addQuestion(RTI, q13)
    q14=Question(" Is changing the race of existing characters in fiction wrong?")
    a42=Answer("Yes, always", 0, 1, 0)
    Question.addAnswer(q14, a42)
    a43=Answer("Yes, but only when it's whitewashing", 2, 0, 0)
    Question.addAnswer(q14, a43)
    a44=Answer("Yes, but only when it's done for the sake of diversity", 0, 0, 2)
    Question.addAnswer(q14, a44)
    a45=Answer("No", 0, 1, 0)
    Question.addAnswer(q14, a45)
    Test.addQuestion(RTI, q14)
    q15=Question("Do you believe you are smarter than the general public?")
    a46=Answer("Yes", 1, 0, 1)
    Question.addAnswer(q15, a46)
    a47=Answer("No", 0, 2, 0)
    Question.addAnswer(q15, a47)
    Test.addQuestion(RTI, q15)
    q16=Question("Is Reverse Racism (racism against whites) real?")
    a48=Answer("Yes, this is an overlooked and important issue", 0, 0, 2)
    Question.addAnswer(q16, a48)
    a49=Answer("Yes, but it is not as significant as racism against non-whites", 0, 1, 0)
    Question.addAnswer(q16, a49)
    a50=Answer("No", 2, 0, 0)
    Question.addAnswer(q16, a50)
    Test.addQuestion(RTI, q16)
    q17=Question("Is it racist to have low numbers of non-whites in a workplace?")
    a51=Answer("Yes, exclusion is inherently racist", 2, 0, 0)
    Question.addAnswer(q17, a51)
    a52=Answer("Yes, but only for some jobs", 0, 1, 0)
    Question.addAnswer(q17, a52)
    a53=Answer("No, the best workers must get each position. Race does not matter", 0, 0, 2)
    Question.addAnswer(q17, a53)
    Test.addQuestion(RTI, q17)
    q18=Question("Do you support affirmative action (specifically for race)?")
    a54=Answer("Yes, this helps the underprivileged", 1, 0, 0)
    Question.addAnswer(q18, a54)
    a55=Answer("No, this is unfair", 0, 0, 1)
    Question.addAnswer(q18, a55)
    Test.addQuestion(RTI, q18)
    q19=Question("What brand is your phone? Why?")
    a56=Answer("Android Phone (Samsung, Google Pixel, LG, Moto, etc), because it's superior to iPhones", 0, 0, 1)
    Question.addAnswer(q19, a56)
    a57=Answer("Android Phone, but no particular preference", 0, 1, 0)
    Question.addAnswer(q19, a57)
    a58=Answer("iPhone, but no particular preference", 0, 1, 0)
    Question.addAnswer(q19, a58)
    a59=Answer("iPhone because it's superior to Android", 1, 0, 0)
    Question.addAnswer(q19, a59)
    a60=Answer("Other", 0, 0, 0)
    Question.addAnswer(q19, a60)
    Test.addQuestion(RTI, q19)
    q20=Question("What is Gamergate?")
    a61=Answer("A horrible event that resulted in the attack of female gamers and gaming developers", 3, 0, 0)
    Question.addAnswer(q20, a61)
    a62=Answer("An overreaction between two sides over something that wasn't a big deal", 0, 0, 1)
    Question.addAnswer(q20, a62)
    a63=Answer("An issue on corruption among journalists in the gaming industry", 0, 0, 2)
    Question.addAnswer(q20, a63)
    a64=Answer("Feminists twisting an issue to pursue their own agenda", 0, 0, 2)
    Question.addAnswer(q20, a64)
    a65=Answer("I have no idea", 0, 2, 0)
    Question.addAnswer(q20, a65)
    Test.addQuestion(RTI, q20)
    q21=Question('Is Candy Crush a "real" video game?')
    a66=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q21, a66)
    a67=Answer("No", 0, 0, 1)
    Question.addAnswer(q21, a67)
    a68=Answer("I'm not familiar with Candy Crush", 0, 0, 0)
    Question.addAnswer(q21, a68)
    Test.addQuestion(RTI, q21)
    q22=Question("Do you use Twitch on a regular basis?")
    a69=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q22, a69)
    a70=Answer("No, I don't like Twitch", 1, 0, 0)
    Question.addAnswer(q22, a70)
    a71=Answer("I don't know what Twitch is", 0, 2, 0)
    Question.addAnswer(q22, a71)
    Test.addQuestion(RTI, q22)
    q23=Question("How many genders are there?")
    a72=Answer("0 or 1", 0, 0, 0)
    Question.addAnswer(q23, a72)
    a73=Answer("2", 0, 0, 2)
    Question.addAnswer(q23, a73)
    a74=Answer("3-26", 2, 0, 0)
    Question.addAnswer(q23, a74)
    a75=Answer("27+", 3, 0, 0)
    Question.addAnswer(q23, a75)
    Test.addQuestion(RTI, q23)
    q24=Question("Is gender just a social construct?")
    a76=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q24, a76)
    a77=Answer("No ", 0, 0, 1)
    Question.addAnswer(q24, a77)
    a78=Answer("Partially", 0, 1, 0)
    Question.addAnswer(q24, a78)
    Test.addQuestion(RTI, q24)
    q25=Question("Should someone that has female genitalia, and is born as the sex female be able to use male (he/him/his) pronouns?")
    a79=Answer("Yes, sex and genitalia are an innaccurate way of defining gender", 2, 0, 0)
    Question.addAnswer(q25, a79)
    a80=Answer("No", 0, 0, 2)
    Question.addAnswer(q25, a80)
    a81=Answer("Yes, I do not agree with this, but people are free to do what they want", 0, 2, 0)
    Question.addAnswer(q25, a81)
    Test.addQuestion(RTI, q25)
    q26=Question("Should producers and writers include more gay characters in their works?")
    a82=Answer("Yes, representation must be improved", 1, 0, 0)
    Question.addAnswer(q26, a82)
    a83=Answer("Yes, gay characters are better than straight characters", 2, 0, 0)
    Question.addAnswer(q26, a83)
    a84=Answer("No, representation is important, but the current amount is good", 0, 1, 0)
    Question.addAnswer(q26, a84)
    a85=Answer("No, do not include gay characters for the sake of diversity", 0, 0, 2)
    Question.addAnswer(q26, a85)
    a86=Answer("No, being gay is wrong", 0, 0, 0)
    Question.addAnswer(q26, a86)
    Test.addQuestion(RTI, q26)
    q27=Question("Is Modern Feminism out of control and is no longer necessary as women have already achieved equality?")
    a87=Answer("Yes, women have achieved equality and now feminists are trying to obtain an advantage over men", 0, 0, 2)
    Question.addAnswer(q27, a87)
    a88=Answer("Yes, women and men are equal", 0, 0, 1)
    Question.addAnswer(q27, a88)
    a89=Answer("No, but feminists frequently overreact", 0, 1, 0)
    Question.addAnswer(q27, a89)
    a90=Answer("No, but we are close to equality", 0, 1, 0)
    Question.addAnswer(q27, a90)
    a91=Answer("No, women face injustice and disadvantages in our society", 2, 0, 0)
    Question.addAnswer(q27, a91)
    Test.addQuestion(RTI, q27)
    q28=Question("How many cents do women make for every $1 (100 cents) that men make in the workplace?")
    a92=Answer("80 or less", 2, 0, 0)
    Question.addAnswer(q28, a92)
    a93=Answer("80-90", 0, 0, 0)
    Question.addAnswer(q28, a93)
    a94=Answer("91-100", 0, 0, 2)
    Question.addAnswer(q28, a94)
    a95=Answer("101+", 0, 0, 3)
    Question.addAnswer(q28, a95)
    a96=Answer("I don't know", 0, 1, 0)
    Question.addAnswer(q28, a96)
    Test.addQuestion(RTI, q28)
    q29=Question("There are proven statistics that women are paid less than men on average, but why is this the case?")
    a97=Answer("Sexism", 1, 0, 0)
    Question.addAnswer(q29, a97)
    a98=Answer("I don't know", 0, 1, 0)
    Question.addAnswer(q29, a98)
    a99=Answer("Women get pregnant", 0, 0, 2)
    Question.addAnswer(q29, a99)
    a100=Answer("Women work less dangerous jobs", 0, 0, 2)
    Question.addAnswer(q29, a100)
    a101=Answer("Women just have worse jobs than men which justifies this gap", 0, 0, 2)
    Question.addAnswer(q29, a101)
    a102=Answer("Systemic Oppression", 3, 0, 0)
    Question.addAnswer(q29, a102)
    a103=Answer("There aren't proven statistics", 0, 0, 2)
    Question.addAnswer(q29, a103)
    a104=Answer("Other", 0, 1, 0)
    Question.addAnswer(q29, a104)
    Test.addQuestion(RTI, q29)
    q30=Question("What is your assessment of the effects of the #MeToo movement?")
    a105=Answer("Empowerment towards victims and a positive change in our culture", 2, 0, 0)
    Question.addAnswer(q30, a105)
    a106=Answer("Exposes perpetrators of sexual assault/harassment", 1, 1, 0)
    Question.addAnswer(q30, a106)
    a107=Answer("Benefits for victims, but with harmful sideful effects", 0, 1, 1)
    Question.addAnswer(q30, a107)
    a108=Answer("It created a dangerous precedent that will ruin lives without due process", 0, 0, 2)
    Question.addAnswer(q30, a108)
    a109=Answer("I don't know what #MeToo is", 0, 1, 0)
    Question.addAnswer(q30, a109)
    Test.addQuestion(RTI, q30)
    q31=Question("Did you actively participate in the Women's March and other protests with similar intentions?")
    a110=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q31, a110)
    a111=Answer("No", 0, 0, 0)
    Question.addAnswer(q31, a111)
    a112=Answer("Partially (No you didn't)", 0, 1, 0)
    Question.addAnswer(q31, a112)
    Test.addQuestion(RTI, q31)
    q32=Question("What is your opinion on people who ask for more awareness of female abusers, female rapists, and male victims on posts/videos/stories about female victims?")
    a113=Answer("This is an important and underlooked issue", 0, 0, 2)
    Question.addAnswer(q32, a113)
    a114=Answer("They should make their own posts", 2, 0, 0)
    Question.addAnswer(q32, a114)
    a115=Answer("They do not care about victims, and only want to undermine other important causes", 2, 0, 0)
    Question.addAnswer(q32, a115)
    a116=Answer("I agree with what they stand for, as long as they remain sensitive", 0, 1, 0)
    Question.addAnswer(q32, a116)
    Test.addQuestion(RTI, q32)
    q33=Question("Is white male privilege real?")
    a117=Answer("Yes", 2, 0, 0)
    Question.addAnswer(q33, a117)
    a118=Answer("No", 0, 0, 2)
    Question.addAnswer(q33, a118)
    Test.addQuestion(RTI, q33)
    q34=Question('Do "Black" and "Muslim" culture contain sexist ideas that modern American feminists should criticize more? ')
    a119=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q34, a119)
    a120=Answer("No", 1, 0, 0)
    Question.addAnswer(q34, a120)
    Test.addQuestion(RTI, q34)
    q35=Question("Are Batman and Superman boring characters?")
    a121=Answer("They are both interesting", 0, 2, 0)
    Question.addAnswer(q35, a121)
    a122=Answer("They are both boring", 2, 0, 0)
    Question.addAnswer(q35, a122)
    a123=Answer("Only Batman is boring", 0, 1, 0)
    Question.addAnswer(q35, a123)
    a124=Answer("Only Superman is boring", 0, 0, 2)
    Question.addAnswer(q35, a124)
    a125=Answer("I'm not familiar with these characters", 0, 0, 0)
    Question.addAnswer(q35, a125)
    Test.addQuestion(RTI, q35)
    q36=Question("What is your opinion on Rick and Morty fans?")
    a126=Answer("Most of them are good, except a few cringey people who give it a bad image", 0, 0, 2)
    Question.addAnswer(q36, a126)
    a127=Answer("I have no opinion", 0, 2, 0)
    Question.addAnswer(q36, a127)
    a128=Answer("They are a good fanbase that enjoy a show that is better than most other shows", 1, 0, 1)
    Question.addAnswer(q36, a128)
    a129=Answer("They're annoying", 0, 0, 0)
    Question.addAnswer(q36, a129)
    Test.addQuestion(RTI, q36)
    q37=Question("Which of the following movies is the best?")
    a130=Answer("Frozen", 0, 2, 0)
    Question.addAnswer(q37, a130)
    a131=Answer("Big Hero 6", 0, 0, 2)
    Question.addAnswer(q37, a131)
    a132=Answer("Brave", 2, 0, 0)
    Question.addAnswer(q37, a132)
    a133=Answer("Tangled", 1, 1, 0)
    Question.addAnswer(q37, a133)
    Test.addQuestion(RTI, q37)
    q38=Question("Which of the following movies is the best?")
    a134=Answer("Black Panther", 2, 0, 0)
    Question.addAnswer(q38, a134)
    a135=Answer("Wonder Woman", 1, 0, 0)
    Question.addAnswer(q38, a135)
    a136=Answer("Thor: Ragnarok", 0, 2, 0)
    Question.addAnswer(q38, a136)
    a137=Answer("Spiderman: Homecoming", 0, 1, 1)
    Question.addAnswer(q38, a137)
    a138=Answer("Guardians of the Galaxy Vol 2", 0, 0, 1)
    Question.addAnswer(q38, a138)
    a139=Answer("The Dark Knight", 0, 0, 2)
    Question.addAnswer(q38, a139)
    Test.addQuestion(RTI, q38)
    q39=Question("Is Rey from Star Wars a good character?")
    a140=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q39, a140)
    a141=Answer("Neutral", 0, 1, 0)
    Question.addAnswer(q39, a141)
    a142=Answer("No, because she's a Mary Sue", 0, 0, 2)
    Question.addAnswer(q39, a142)
    a143=Answer("I'm not familiar", 0, 1, 0)
    Question.addAnswer(q39, a143)
    a144=Answer("No, because she's boring", 0, 0, 2)
    Question.addAnswer(q39, a144)
    Test.addQuestion(RTI, q39)
    q40=Question("What is your opinion on remaking old male-driven movies with female casts?")
    a145=Answer("It's a good thing, promotes inclusion", 2, 0, 0)
    Question.addAnswer(q40, a145)
    a146=Answer("It's a bad thing, they should come up with original ideas for women", 0, 0, 2)
    Question.addAnswer(q40, a146)
    Test.addQuestion(RTI, q40)
    q41=Question("Were you ever a fan of BTS, Justin Bieber, One Direction, EXO, Taylor Swift, or Ariana Grande?")
    a147=Answer("Yes", 0, 3, 0)
    Question.addAnswer(q41, a147)
    a148=Answer("No", 1, 0, 1)
    Question.addAnswer(q41, a148)
    Test.addQuestion(RTI, q41)
    q42=Question("What is your opinion on The Big Bang Theory?")
    a149=Answer("It's a good show", 0, 2, 0)
    Question.addAnswer(q42, a149)
    a150=Answer("It's bad", 2, 0, 2)
    Question.addAnswer(q42, a150)
    a151=Answer("No Opinion", 0, 0, 0)
    Question.addAnswer(q42, a151)
    Test.addQuestion(RTI, q42)
    q43=Question("Select the best music artist from these options")
    a152=Answer("Pink Floyd", 0, 0, 2)
    Question.addAnswer(q43, a152)
    a153=Answer("Dua Lipa", 0, 2, 0)
    Question.addAnswer(q43, a153)
    a154=Answer("Janelle Monae", 2, 0, 0)
    Question.addAnswer(q43, a154)
    a155=Answer("Shawn Mendes", 0, 2, 0)
    Question.addAnswer(q43, a155)
    a156=Answer("Camila Cabello", 0, 2, 0)
    Question.addAnswer(q43, a156)
    Test.addQuestion(RTI, q43)
    q44=Question("What is your favorite genre of music?")
    a157=Answer("Pop", 0, 2, 0)
    Question.addAnswer(q44, a157)
    a158=Answer("R&B", 0, 2, 0)
    Question.addAnswer(q44, a158)
    a159=Answer("Rap", 0, 0, 0)
    Question.addAnswer(q44, a159)
    a160=Answer("Country", 0, 1, 1)
    Question.addAnswer(q44, a160)
    a161=Answer("Rock", 0, 0, 2)
    Question.addAnswer(q44, a161)
    a162=Answer("EDM", 0, 0, 2)
    Question.addAnswer(q44, a162)
    a163=Answer("Alternative", 1, 0, 0)
    Question.addAnswer(q44, a163)
    a164=Answer("Alternative Rock", 0, 0, 1)
    Question.addAnswer(q44, a164)
    a165=Answer("Other", 1, 0, 1)
    Question.addAnswer(q44, a165)
    Test.addQuestion(RTI, q44)
    q45=Question("Which of the following is the best video game?")
    a166=Answer("Fallout New Vegas", 0, 0, 2)
    Question.addAnswer(q45, a166)
    a167=Answer("Call of Duty: Black Ops 3", 0, 1, 0)
    Question.addAnswer(q45, a167)
    a168=Answer("Civilization V", 0, 0, 2)
    Question.addAnswer(q45, a168)
    a169=Answer("Battlefront II (The one with Rey)", 2, 0, 0)
    Question.addAnswer(q45, a169)
    a170=Answer("The Sims", 0, 2, 0)
    Question.addAnswer(q45, a170)
    Test.addQuestion(RTI, q45)
    q46=Question("Is Nickelback a terrible band?")
    a171=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q46, a171)
    a172=Answer("No", 0, 1, 0)
    Question.addAnswer(q46, a172)
    a173=Answer("I've never listened to Nickelback", 0, 0, 0)
    Question.addAnswer(q46, a173)
    Test.addQuestion(RTI, q46)
    q47=Question('Was it wrong for Lexa from "The 100" to be killed off considering she is a lesbian character? ')
    a174=Answer("Yes, this is damaging for inclusion of LGBTQ+ characters", 3, 0, 0)
    Question.addAnswer(q47, a174)
    a175=Answer("No, characters die all the time in the series. Her sexual orientation isn't relevant", 0, 0, 0)
    Question.addAnswer(q47, a175)
    a176=Answer("I am not familiar with the 100", 0, 0, 0)
    Question.addAnswer(q47, a176)
    Test.addQuestion(RTI, q47)
    q48=Question("Is Doctor Who casting a woman as The Doctor for the first time a good thing?")
    a177=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q48, a177)
    a178=Answer("No, if they want to promote diversity they should create original characters", 0, 0, 1)
    Question.addAnswer(q48, a178)
    a179=Answer("I am not familiar with Doctor Who", 0, 2, 0)
    Question.addAnswer(q48, a179)
    Test.addQuestion(RTI, q48)
    q49=Question("What is your opinion on the Bechdel Test?")
    a180=Answer("It's a good test to determine if women are well represented", 1, 0, 0)
    Question.addAnswer(q49,a180)
    a181=Answer("Its requirements are not sufficient enough for proper representation of women", 2, 0, 0)
    Question.addAnswer(q49,a181)
    a182=Answer("The test is not sufficient because it only covers two genders", 3, 0, 0)
    Question.addAnswer(q49,a182)
    a183=Answer("The test is flawed, just because something fails it doesn't mean it failed to represent women well", 0, 0, 1)
    Question.addAnswer(q49,a183)
    a184=Answer("I don't know what the Bechdel Test is", 0, 2, 0)
    Question.addAnswer(q49,a184)
    Test.addQuestion(RTI,q49)
    Go2ItGang=1
    while Go2ItGang<Test.getNoOfQuestions(RTI):
        Test.askQuestion(RTI)
        Go2ItGang+=1
    Test.getResults(RTI)

takeFWI()
