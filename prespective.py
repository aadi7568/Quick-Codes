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

"""
args = sys.argv[1:]

def main():

  compose(args[0],args[1])

  

if __name__== "__main__":

  main()
  """
