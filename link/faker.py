from link.models import *
from faker import Faker

# Model:Link:
def runLink():

    '''
        $ python manage.py shell
        > from link.faker import runLink
        > runLink()
        > exit()
    '''

    faker = Faker() # Faker(['tr-TR'])

    for _ in range(10):
        link = Link(link=faker.domain_word(),
                    link_name=faker.domain_word(),
                    description=faker.paragraph())
        link.save()

    print ('Finished')
