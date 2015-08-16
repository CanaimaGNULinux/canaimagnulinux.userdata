# -*- coding: utf-8 -*-

from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """ Making added fields available on the Personal Information form. """

    def get_firstname(self):
        return unicode(self.context.getProperty('firstname', ''), 'utf-8')

    def set_firstname(self, value):
        return unicode(self.context.setMemberProperties({'firstname': value}), 'utf-8')
    firstname = property(get_firstname, set_firstname)

    def get_lastname(self):
        return unicode(self.context.getProperty('lastname', ''), 'utf-8')

    def set_lastname(self, value):
        return unicode(self.context.setMemberProperties({'lastname': value}), 'utf-8')
    lastname = property(get_lastname, set_lastname)

    def get_gender(self):
        return unicode(self.context.getProperty('gender', ''), 'utf-8')

    def set_gender(self, value):
        return unicode(self.context.setMemberProperties({'gender': value}), 'utf-8')
    gender = property(get_gender, set_gender)

    def get_mobile(self):
        return unicode(self.context.getProperty('mobile', ''), 'utf-8')

    def set_mobile(self, value):
        return unicode(self.context.setMemberProperties({'mobile': value}), 'utf-8')
    mobile = property(get_mobile, set_mobile)

    def get_officen(self):
        return unicode(self.context.getProperty('officen', ''), 'utf-8')

    def set_officen(self, value):
        return unicode(self.context.setMemberProperties({'officen': value}), 'utf-8')
    officen = property(get_officen, set_officen)

    def get_irc(self):
        return unicode(self.context.getProperty('irc', ''), 'utf-8')

    def set_irc(self, value):
        return unicode(self.context.setMemberProperties({'irc': value}), 'utf-8')
    irc = property(get_irc, set_irc)


    def get_telegram(self):
        return unicode(self.context.getProperty('telegram', ''), 'utf-8')

    def set_telegram(self, value):
        return unicode(self.context.setMemberProperties({'telegram': value}), 'utf-8')
    telegram = property(get_telegram, set_telegram)

    def get_skype(self):
        return unicode(self.context.getProperty('skype', ''), 'utf-8')

    def set_skype(self, value):
        return unicode(self.context.setMemberProperties({'skype': value}), 'utf-8')
    skype = property(get_skype, set_skype)

    def get_birthdate(self):
        return unicode(self.context.getProperty('birthdate', ''), 'utf-8')

    def set_birthdate(self, value):
        return unicode(self.context.setMemberProperties({'birthdate': value}), 'utf-8')
    birthdate = property(get_birthdate, set_birthdate)

    def get_city(self):
        return unicode(self.context.getProperty('city', ''), 'utf-8')

    def set_city(self, value):
        return unicode(self.context.setMemberProperties({'city': value}), 'utf-8')
    city = property(get_city, set_city)

    def get_country(self):
        return unicode(self.context.getProperty('country', ''), 'utf-8')

    def set_country(self, value):
        return unicode(self.context.setMemberProperties({'country': value}), 'utf-8')
    country = property(get_country, set_country)

    def get_phone(self):
        return unicode(self.context.getProperty('phone', ''), 'utf-8')

    def set_phone(self, value):
        return unicode(self.context.setMemberProperties({'phone': value}), 'utf-8')
    phone = property(get_phone, set_phone)

    def get_institution(self):
        return unicode(self.context.getProperty('institution', ''), 'utf-8')

    def set_institution(self, value):
        return unicode(self.context.setMemberProperties({'institution': value}), 'utf-8')
    institution = property(get_institution, set_institution)

    def get_instadd(self):
        return unicode(self.context.getProperty('instadd', ''), 'utf-8')

    def set_instadd(self, value):
        return unicode(self.context.setMemberProperties({'instadd': value}), 'utf-8')
    instadd = property(get_instadd, set_instadd)

    def get_position(self):
        return unicode(self.context.getProperty('position', ''), 'utf-8')

    def set_position(self, value):
        return unicode(self.context.setMemberProperties({'position': value}), 'utf-8')
    position = property(get_position, set_position)

    def get_profession(self):
        return unicode(self.context.getProperty('profession', ''), 'utf-8')

    def set_profession(self, value):
        return unicode(self.context.setMemberProperties({'profession': value}), 'utf-8')
    profession = property(get_profession, set_profession)

    # def get_newsletter(self):
    #     return unicode(self.context.getProperty('newsletter', ''), 'utf-8')

    # def set_newsletter(self, value):
    #     return unicode(self.context.setMemberProperties({'newsletter': value}), 'utf-8')
    # newsletter = property(get_newsletter, set_newsletter)

    # def get_accept(self):
    #     return unicode(self.context.getProperty('accept', ''), 'utf-8')

    # def set_accept(self, value):
    #     return unicode(self.context.setMemberProperties({'accept': value}), 'utf-8')
    # accept = property(get_accept, set_accept)
