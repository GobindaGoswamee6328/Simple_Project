
import random
when = ['Yesterday','After few days','Last night','After a long time','On 16th May']
name = ['Tom', 'Maria','Asonso', 'Ramos', 'Simanta']
residence = ['Spain','Croatia', 'Germany', 'Brazil', 'England']
went = ['University', 'Movie','School', 'Seminar', 'College']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(name) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
