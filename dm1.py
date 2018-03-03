import string
import json
import pickle
import datetime

#Task 1: Test Python Environment
def task1 ():
    print ("hello world")
if __name__== ' main ':
    task1 ()

#Task 2: Dene Object
items = [1,2,3,4,5]
def task2():
    items = [1,2,3,4,5]
    print ("objects in list:",items)
task2()

#Task 3: File Reading
def task3():
    list1 = []
    list2 = []
    f = open("task3.data", 'w+')
    f.write('12345678910')
    for first in range(1, 6):
            list1.append(first)
    for second in range(6, 11):
            list2.append(second)
    print('objects in items1:', list1)
    print('objects in items2:', list2)

task3()

#Task 4: Data Structure
data = {'school': 'UAlbany', 'address': '1400 Washington Ave, Albany, NY 12222', 'phone': '(518) 442-3300'}
for key, value in data.items() :
    print (key+":", value)

#Task 5: Data Serialization
json_string = json.dumps(data)
print(json_string)
jsonToPython = json.loads(json_string)
print(jsonToPython)

#Task 6: Data Serialization
def task6():
    with open("task6.data","wb") as handle:
        pickle.dump((items,data), handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open("task6.data", "rb") as handle:
        task6 = pickle.load(handle)
    print ("\n",task6)
task6()

#Task 7: Data Preprocessing

with open("CrimeReport.txt", "r") as f2:
    for line in f2:
        #line = f2.readlines()
        tweet = json.loads(line)
        for id in tweet:
            print("tweet_id:",tweet['id'])

#Task 8: Data Preprocessing: tweets iltering
tweets = []
for line in open("CrimeReport.txt").readlines():
    tweet = json.loads(line)
    tweets.append(tweet)
    print(tweets[])
sorted_tweets = sorted (tweets , key = lambda item :
datetime.datetime.strptime (item ["created_at"], '%a %b %d %H:%M:%S +0000 %Y' ) )
# s o r t ed twe e t s based on time .
f = open ('task8.data',"w")
for tweets in sorted_tweets [-5:]:
    f.write (json.dumps(tweets ))
    print(tweets)
f.close()
