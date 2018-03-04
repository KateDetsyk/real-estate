class Property:
    '''
    Represent the class Property.
    '''
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        '''
        Show the priperty.
        '''
        super().__init__(**kwargs)
        self.square_feet =square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''
        Dislay information about property.
        '''
        print('PROPERTY DETAILS')
        print('================')
        print('square footage: {}'.format(self.square_feet))
        print('bedrooms: {}'.format(self.num_bedrooms))
        print('bathrooms: {}'.format(self.num_baths))
        print()

    def promt_init():
        '''
        Fast initialisation.
        '''
        return dict(square_feet=input('Enter the square feet: '),
                 beds=input('Enter number of bedrooms: '),
                 baths=input('Enter number of baths: '))
    promt_init = staticmethod(promt_init)


class Apartment(Property):
    '''
    Represent apartment.
    '''
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        '''
        Initialise apartment.
        '''
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Display information about apartment.
        '''
        super().display()
        print('APARTEMENT DETAILS')
        print('laundry: %s' % self.laundry)
        print('has balcony: %s' % self.balcony)

    def prompt_init():
        '''
        Fast initialisation.
        '''
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input('What laundry ficilities does'
                     'the property have {{}}'.format(
                     ', '.join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
        balcony = input('Does the property have a balcony? {{}}'.format(
                 ', '.join(Apartment.valid_balconies)))
        parent_init.update({
             'laundry': laundry,
             'balcony': balcony
        })
        return parent_init
        prompt_init = staticmethod(prompt_init)


class House(Property):
    '''
    Represent house.
    '''
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        '''
        Initialisation of class House.
        '''
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        Display the information about house.
        '''
        super().display()
        print('HOUSE DETAILS')
        print('# of stories: {}'.format(self.num_stories))
        print('garage: {}'.format(self.garage))
        print('fenced yard: {}'.format(self.fenced))

    def prompt_init():
        '''
        Fast initialisation. Function returns parent_init.
        '''
        parent_init = Property.prompt_init()
        fanced = get_valid_input('Is the yard fanced?', House.valid_fenced)
        garage = get_valid_input('Is there a garage?', House.valid_garage)
        num_stories = input('How many stories?')

        parent_init.update({
            'fenced': fenced,
            'garage': garage,
            'num_stories': num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase:
    '''
    Represent class Purchase.
    '''
    def __init__(self, price='', taxes='', **kwargs):
        '''
        Initialises class Purchase with price and taxes.
        '''
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Displays the details about purchase.
        '''
        super().display()
        print('PURCHASE DETAILS')
        print('selling price: {}'.format(self.price))
        print('estimated taxes: {}'.format(self.taxes))

    def prompt_init():
        '''
        Function initialise purchase with it's details and return dictionary
        with information.
        '''
        return dict(price=input('What is the selling price?'),
            taxes=input('What are the taxes?'))
    prompt_init = staticmethod(prompt_init)


class Rental:
    '''
    Represent class Rental.
    '''
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        '''
        Initialises class Rental with it's details.
        '''
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Displays the details about rent.
        '''
        super().display()
        print('RENTAL DETAILS')
        print('rent: {}'.format(self.rent))
        print('estimated utilities: {}'.format(self.utilities))
        print('furnished: {}'.format(self.furnished))

    def prompt_init():
        '''
        Function initoalises rent with info about it and returns dict with
        information.
        '''
        return dict(rent=input('What is the monthly rent?'),
            utilities=input('What are the estimated utilities?')
            furnished=get_valid_input('Is the property furnished?',
                ('yes', 'no')))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    '''
    Represent class HouseRental.
    '''
    def prompt_init():
        '''
        Function initoalises house rent with info about it and returns
        dict with information.
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    '''
    Represent class ApartmentRental.
    '''
    def prompt_init():
        '''
        Function initoalises apartment rent with info about it and returns
        dict with information.
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    '''
    Represent class ApartmentPurchase.
    '''
    def prompt_init():
        '''
        Function initoalises apartment purchase with info about it and returns
        dict with information.
        '''
        init = Apartment.prompt_init()
        init.update(Prchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    '''
    Represent class HousePurchase.
    '''
    def prompt_init():
        '''
        Function initoalises house purchase with info about it and returns
        dict with information.
        '''
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    '''
    Represent class Agent.
    '''
    def __init__(self):
        '''
        Initialises agent.
        '''
        self.property_list = []

    def display_properties(self):
        '''
        Function displays properties.
        '''
        for property in self.property_list:
            property.display()
            
