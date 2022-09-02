import math
import statistics

### Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = min(sorted_ages)
max_age = max(sorted_ages)
print(sorted_ages)
print("min_age, max_age=",min_age,",",max_age)
# Add the min age and the max age again to the list
sorted_ages.extend((min_age, max_age))
print(sorted_ages)

# Median of Ages
sorted_ages = sorted(sorted_ages)
len_ages = len(sorted_ages)

median_age = statistics.median(sorted_ages)
print("median_age=",median_age)
# Average of Ages
avg_age = sum(sorted_ages)/len(sorted_ages)
print("avg_age=",avg_age)
# Range of Ages
range_age = max_age - min_age
print("range_age=",range_age)
print("break1")
### Question 2

dog = dict()
dog['name'] = 'shadow'
dog['color'] = 'black'
dog['breed'] = 'rotwiller'
dog['legs'] = 4
dog['age'] = 4

student = {
    "first_name": "dhheeraj",
    "last_name": "boleenenni",
    "gender": "male",
    "age": 23,
    "marital status": "single",
    "skills": ["python", "java","sql"],
    "country": "United States",
    "city": "lees summit",
    "address": "1104 Innovation Campus"
}

len_student = len(student)
print("length of student dic",len_student)
skills = student['skills']
print("skills=",skills)
type_of_skills = type(skills)
print("type of skills=",type_of_skills)
student['skills'].extend(["ML"])
print("update skills=",student['skills'])
#student.update()

keys_student = list(student.keys())
print("student keys=",keys_student)
values_student = list(student.values())
print("student values=",values_student)
print("break2")
### Question 3
brothers = ("prem","harish")
sisters =  ("mounica","manu")

siblings = brothers + sisters
len_siblings = len(siblings)
print("length of sibilings=",len_siblings)
family_members = siblings + ("narssing rao","lavanya")
print("family members=",family_members)
print("break3")
### Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

len_it_companies = len(it_companies)
print("len_companies=",len_it_companies)
it_companies.add("Twitter")
it_companies.discard("Oracle")
print("remove vs discard=remove deletes the element from the list if not present it returns Key error discard deleted "
      "the element from the list otherwise return None")

join_AB = A.union(B)
intersection_AB = A.intersection(B)
print("intersection=",intersection_AB)
isSubset_AB = A.issubset(B)

A.isdisjoint(B)
A.union(B)
B.union(A)
A.difference(B)
A.clear()
B.clear()

set_ages = set(age)
print("set ages length = ",len(set_ages) , "list ages length :",len(age))
print("break4")
### Question 5
# The radius of a circle is 30 meters.
r = 30
pi = 3.14
_area_of_circle_ =  pi * r * r
_circum_of_circle_ = 2 * pi * r
print("area of circle=",_area_of_circle_," ,circumference of a circle=",_circum_of_circle_)
r = float(input("Enter radius of circle : "))
area_of_circle = pi * r * r
print("area of circle as per unit=",area_of_circle)
print("break5")
### Question 6

sent = """I am a teacher and I love to inspire and teach people"""
split_sent = sent.split()
unique_words = set(split_sent)
print("unique words=",unique_words)
print("break6")
### Question 7

# Use a tab escape sequence to get the following lines.
data = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(data)
print("break7")
### Question 8
radius = 10
area = 3.14 * radius ** 2
sent = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(sent)
print("break8")
### Question 9

#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]

N = int(input("Enter No. of students : "))
lbs_to_kg_convert = 0.4536
lbs_weights = []
kg_weights = []
for i in range(0,N):
    lbs_weights.append(int(input("Enter student Weight(lbs) : ")))

for weight in lbs_weights:
    kg_weights.append(round(weight * lbs_to_kg_convert,2))

print(kg_weights)
print("break9")

