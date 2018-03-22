# -*- coding: utf-8 -*-
import sys
import json
from googleapiclient import discovery
import csv

def compose(text,model=""):

  if model == "S":

    model = "SPAM"

  elif model == "T":

    model = "TOXICITY"

  elif model == "O":

    model = "OBSCENE"

  elif model == "UN":

    model = "UNSUBSTANTIAL"

  elif model == "LTR":

    model = "LIKELY_TO_REJECT"

  elif model == "IN":

    model = "INCOHERENT"

  
  API_KEY='AIzaSyDvSlBOwdeZyTuYEyyuIykdc3DRNBnIeQ4'

  service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

  analyze_request = {

    'comment': { 'text': text },

    'requestedAttributes': {"LIKELY_TO_REJECT": {}}

  }
  try:
    response = service.comments().analyze(body=analyze_request).execute()
    # models = ['SPAM','TOXICITY','OBSCENE','UNSUBSTANTIAL','LIKELY_TO_REJECT','INCOHERENT','INFLAMMATORY']
    #for m in models:
    return response['attributeScores']['LIKELY_TO_REJECT']['summaryScore']['value']*100
  except:
    return 0

f = open('test.csv', 'rt')
reader = csv.reader(f)

#print reader

for r in reader:
  print r[1] + ","
  # score = compose(r[0])
  #print score
  # print str(r[1]) + "," + str(score) + "," + str(r[0])
  
















  #print("%s - %s \n"%(text,score))
  # print json.dumps(response, indent=2)


# revs = ["what a movie_ oh my goodness_ jst awesome and fantastic mind blowing movie_ love u urvashi_ ur acting is awesome … hate story 4 all casting r very good"
# ,"5c6v8v8v9vovov9v9c8cixi,uzucicqixwiwco owcicicixiickvsovalbwovwocwoci,uzuxixifilfokxlfkdkxkckckcclfodidjcpt9gshiwkkspgoxococofofidididixcso6kysusufodif9didodoxixkxiddodidussuixx"
# ,"impressive movie it's so sexy and hoting I really like hate story IV/4 Jovi ho mujha pasand Aya.. kamsa kam hate story 3 Jesa nhi hua wow over ho gya tha  yea thik hai I love you Urvashi main apka bht bht bht bara fan hu ji... I love you",
# "Dont waste your time and money for this f***n*g movie. everything is bakwas in this movie like karan's acting, storyline dialogs delivery . kuch bhi dhang ka nahi hai guys. kyu gaya main ye movie dekhne mood spoil kar diya",
# "Such a waste of time n money!! Fully messed story with lack of proper scripting..So many twist in movie that u can easily forget what was actually going on!!",
# "It's totally waste time and money not recommended until unless you got time to Jerk yourself in few bold shots in songs. Worst direction and story",
# "very boring movie no story money waste the cinematography is quite good but the content the story of the flim is not soo good 1 time watchable movie",
# "The movie starts with an unexceptional start which moves to little past where we come to know how Karan Wahi meets the young and beautiful club dancer played by Urvashi Rautela.",
# "Waste of money. Full faltu. Overacting. No thrills. No story. No suspense. Predictable plot.This type of movies should not be made.0 stars.",
# "Average movie... Story was boaring................repeated story....................................not so adult movie...........................",
# "Giving 3 Star only for the fab performance by Urvashi even karan & vivian also... lots of English dialogues were there which was unnecessary in a hindi film... Story was well written & somehow same like Wajah tum ho... Twist was not so good that audience want & we have seen in Hate story 3... Not so much of bold scenes were there... Overall one tym watch but not in Theatres watch it in pc or phone",
# "well again the same theme with usual twist and turn. well executed but could have been better. 1 time watching film.this film focusses on love, lust, ego, & humanity!",
# "Hate Story ..is a franchise started by Vikram Bhatt and carried ahead by director Vishal Pandya who has directed episodes 2,3 and now 3.Hate Story ( 2012) has Paoli DamHate Story 2 ( 2014) has Surveen Chawla Hate Story 3 (2015-16) had Zareen Khan And now Hate Story 4 has Urwashi Rautela ( Seen earlier in Great Grand Masti)The premise of the film chronicles a woman and her struggle to fight against the man/men that betrayed / harmed  her.If I tell anything more about Hate Story 4 the whole suspense would be revealed.I would say this is the best of the 3 films .(The first I missed ).Go for it expecting some good skin show and few twists and turns.Story revolving around the same old subject of female protagonists revenge, too much of melodrama at places.Personally I enjoyed it.",
# "the movie was cancelled how rubbish how u guys showing  on book my Show if the show was cancelled  den n evn I dint  gt my money  bck very very disappointed",
# "The Story Line Is As Same As The Old Franchise (Now, Revenge For Brother). no So Good Performances,Urvashi Performed The Character Of Tasha Well But Overacted In Few Scenes,Karan Needs To Improve His Acting,Vivan & Ihana Were Ok.",
# "songs are awesome but not the stolen onemovie is n inspiration for youth and game played on poor innocent ppl n police taking briberry should stop",
# "Do not waste money on this shit . Seriously, worst movie ever watched. Waste of time and money. Ohh shit i have wastes my 1 minute to rate this shit.",
# "its was a good movie. but place condition was so much pathetic. there was Lot of Smell, uncomfortable seats and Airconditioner was not properly working.",
# "ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH ONE TINE WATCH",
# "Fuckol movie worse acting poor show poor poor poor poor poor mahapoor nobdy knw how to act accpt gullu bad boy...poor fuckol story bad acting bad screnply only few songs wch u can njoy in d movie all over jst waste of money plz don go bttr download from som mobile site and watch"
# ]

"""
args = sys.argv[1:]

def main():

  compose(args[0],args[1])

  

if __name__== "__main__":

  main()
  """