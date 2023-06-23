def avg(scores):
    total=scores['tamil']['marks']+scores['english']['marks'] \
          +scores['maths']['marks']+scores['science']['marks'] \
          +scores['social']['marks']

    return total/5.0


def grade(mark):
    if(mark>=90):
        return 'A'
    elif(mark>=80):
        return 'B'
    elif(mark>=70):
        return 'C'
    elif(mark>=60):
        return 'D'
    else:
        return 'E'


#Initialize dictionary
scores={}
scores['tamil']={'marks':0,'grade':''}
scores['english']={'marks':0,'grade':''}
scores['maths']={'marks':0,'grade':''}
scores['science']={'marks':0,'grade':''}
scores['social']={'marks':0,'grade':''}

#Updating marks
scores['tamil']['marks']=int(input("Enter Tamil marks : "))
scores['english']['marks']=int(input("Enter English marks : "))
scores['maths']['marks']=int(input("Enter Maths marks : "))
scores['science']['marks']=int(input("Enter Science marks : "))
scores['social']['marks']=int(input("Enter Social marks : "))

#Updating grade
scores['tamil']['grade']=grade(scores['tamil']['marks'])
scores['english']['grade']=grade(scores['english']['marks'])
scores['maths']['grade']=grade(scores['maths']['marks'])
scores['science']['grade']=grade(scores['science']['marks'])
scores['social']['grade']=grade(scores['social']['marks'])

#Display output
print("------------------------------------")
print("Subject           Marks        Grade")
print("------------------------------------")
print("%-15s  %4d          %3c"%("Tamil",scores['tamil']['marks'],scores['tamil']['grade']))
print("%-15s  %4d          %3c"%("English",scores['english']['marks'],scores['english']['grade']))
print("%-15s  %4d          %3c"%("Maths",scores['maths']['marks'],scores['maths']['grade']))
print("%-15s  %4d          %3c"%("Science",scores['science']['marks'],scores['science']['grade']))
print("%-15s  %4d          %3c"%("Social",scores['social']['marks'],scores['social']['grade']))
print("------------------------------------")
print("Average marks : %.2f"%avg(scores))
print("------------------------------------")


