import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.passwordpolicy.gvpasswordpolicy import PasswordPolicyTag as tags

# ---- Descriptors ----

class PPName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class PPMinLength:
    def __get__(self, instance, owner):
        return instance._min_length
    def __set__(self, instance, value):
        instance._min_length = f"PASSWORD_MIN_LENGTH = {value}"
    def __delete__(self, instance):
        del instance._min_length

class PPMaxLength:
    def __get__(self, instance, owner):
        return instance._max_length
    def __set__(self, instance, value):
        instance._max_length = f"PASSWORD_MAX_LENGTH = {value}"
    def __delete__(self, instance):
        del instance._max_length

class PPMinUpperCase:
    def __get__(self, instance, owner):
        return instance._min_upper
    def __set__(self, instance, value):
        instance._min_upper = f"PASSWORD_MIN_UPPER_CASE_CHARS = {value}"
    def __delete__(self, instance):
        del instance._min_upper

class PPMinLowerCase:
    def __get__(self, instance, owner):
        return instance._min_lower
    def __set__(self, instance, value):
        instance._min_lower = f"PASSWORD_MIN_LOWER_CASE_CHARS = {value}"
    def __delete__(self, instance):
        del instance._min_lower

class PPMInNumeric:
    def __get__(self, instance, owner):
        return instance._min_numeric
    def __set__(self, instance, value):
        instance._min_numeric = f"PASSWORD_MIN_NUMERIC_CHARS = {value}"
    def __delete__(self, instance):
        del instance._min_numeric

class PPMinSpecial:
    def __get__(self, instance, owner):
        return instance._min_special
    def __set__(self, instance, value):
        instance._min_special = f"PASSWORD_MIN_SPECIAL_CHARS = {value}"
    def __delete__(self, instance):
        del instance._min_special

class PPMinAgeDays:
    def __get__(self, instance, owner):
        return instance._min_age
    def __set__(self, instance, value):
        instance._min_age = f"PASSWORD_MIN_AGE_DAYS = {value}"
    def __delete__(self, instance):
        del instance._min_age

class PPMaxAgeDays:
    def __get__(self, instance, owner):
        return instance._max_age
    def __set__(self, instance, value):
        instance._max_age = f"PASSWORD_MAX_AGE_DAYS = {value}"
    def __delete__(self, instance):
        del instance._max_age

class PPMaxRetries:
    def __get__(self, instance, owner):
        return instance._max_retries
    def __set__(self, instance, value):
        instance._max_retries = f"PASSWORD_MAX_RETRIES = {value}"
    def __delete__(self, instance):
        del instance._max_retries

class PPLockoutTime:
    def __get__(self, instance, owner):
        return instance._lockout_time
    def __set__(self, instance, value):
        instance._lockout_time = f"PASSWORD_LOCKOUT_TIME_MINS = {value}"
    def __delete__(self, instance):
        del instance._lockout_time

class PPHistory:
    def __get__(self, instance, owner):
        return instance._history
    def __set__(self, instance, value):
        instance._history = f"PASSWORD_HISTORY = {value}"
    def __delete__(self, instance):
        del instance._history

class PPComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = f"COMMENT = '{value}'"
    def __delete__(self, instance):
        del instance._comment

class PPTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG {clause}"
    def __delete__(self, instance):
        del instance._tag_clause

# ---- Attributes container ----

class PasswordPolicyAttrs:
    name = PPName()
    min_length = PPMinLength()
    max_length = PPMaxLength()
    min_upper = PPMinUpperCase()
    min_lower = PPMinLowerCase()
    min_numeric = PPMInNumeric()
    min_special = PPMinSpecial()
    min_age = PPMinAgeDays()
    max_age = PPMaxAgeDays()
    max_retries = PPMaxRetries()
    lockout_time = PPLockoutTime()
    history = PPHistory()
    comment = PPComment()
    tag_clause = PPTagClause()


class PasswordPolicy(BaseObject):
    def __init__(self, session, user_id):
        super().__init__(session=session,user_id=user_id)
        self.attr = PasswordPolicyAttrs()


    def set_name(self, v): self.attr.name = v
    def set_min_length(self, v): self.attr.min_length = v
    def set_max_length(self, v): self.attr.max_length = v
    def set_min_upper(self, v): self.attr.min_upper = v
    def set_min_lower(self, v): self.attr.min_lower = v
    def set_min_numeric(self, v): self.attr.min_numeric = v
    def set_min_special(self, v): self.attr.min_special = v
    def set_min_age(self, v): self.attr.min_age = v
    def set_max_age(self, v): self.attr.max_age = v
    def set_max_retries(self, v): self.attr.max_retries = v
    def set_lockout_time(self, v): self.attr.lockout_time = v
    def set_history(self, v): self.attr.history = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attr_name):
            self.flag_dic[tag] = 1 if getattr(self.attr, attr_name, None) is not None else 0

        set_flag(tags.PASSWORD_MIN_LENGTH, "min_length")
        set_flag(tags.PASSWORD_MAX_LENGTH, "max_length")
        set_flag(tags.PASSWORD_MIN_UPPER_CASE_CHARS, "min_upper")
        set_flag(tags.PASSWORD_MIN_LOWER_CASE_CHARS, "min_lower")
        set_flag(tags.PASSWORD_MIN_NUMERIC_CHARS, "min_numeric")
        set_flag(tags.PASSWORD_MIN_SPECIAL_CHARS, "min_special")
        set_flag(tags.PASSWORD_MIN_AGE_DAYS, "min_age")
        set_flag(tags.PASSWORD_MAX_AGE_DAYS, "max_age")
        set_flag(tags.PASSWORD_MAX_RETRIES, "max_retries")
        set_flag(tags.PASSWORD_LOCKOUT_TIME_MINS, "lockout_time")
        set_flag(tags.PASSWORD_HISTORY, "history")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, fl in self.flag_dic.items() if fl == 1]

    def set_create_password_policy_qry(self):
        self.qry = f"CREATE PASSWORD POLICY {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            # append each clause to query
            self.qry += f" {getattr(self.attr, prop.lower())}"

    def alter_object(self):
        for prop in self.property_lst:
            # for ALTER, we only do SET or UNSET or COMMENT or TAG
            if prop in (tags.COMMENT, tags.TAG_CLAUSE):
                self.qry = f"ALTER PASSWORD POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
                self.execute_final_query()
            else:
                # for numeric attributes or others
                self.qry = f"ALTER PASSWORD POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
                self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_password_policy_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_min_length(kwargs.get(tags.PASSWORD_MIN_LENGTH))
        self.set_max_length(kwargs.get(tags.PASSWORD_MAX_LENGTH))
        self.set_min_upper(kwargs.get(tags.PASSWORD_MIN_UPPER_CASE_CHARS))
        self.set_min_lower(kwargs.get(tags.PASSWORD_MIN_LOWER_CASE_CHARS))
        self.set_min_numeric(kwargs.get(tags.PASSWORD_MIN_NUMERIC_CHARS))
        self.set_min_special(kwargs.get(tags.PASSWORD_MIN_SPECIAL_CHARS))
        self.set_min_age(kwargs.get(tags.PASSWORD_MIN_AGE_DAYS))
        self.set_max_age(kwargs.get(tags.PASSWORD_MAX_AGE_DAYS))
        self.set_max_retries(kwargs.get(tags.PASSWORD_MAX_RETRIES))
        self.set_lockout_time(kwargs.get(tags.PASSWORD_LOCKOUT_TIME_MINS))
        self.set_history(kwargs.get(tags.PASSWORD_HISTORY))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=PasswordPolicy(session=session,
                         user_id=user_id,
                        )
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set min_length")
        if tags.MIN_LENGTH in kwargs.keys():
            obj_inst.set_min_length(kwargs[tags.PASSWORD_MIN_LENGTH])
        else:
            obj_inst.set_min_length('NONE')

        obj_inst.logger.info("set max_length")
        if tags.MAX_LENGTH in kwargs.keys():
            obj_inst.set_max_length(kwargs[tags.PASSWORD_MAX_LENGTH])
        else:
            obj_inst.set_max_length('NONE')

        obj_inst.logger.info("set min_upper")
        if tags.MIN_UPPER in kwargs.keys():
            obj_inst.set_min_upper(kwargs[tags.PASSWORD_MIN_UPPER_CASE_CHARS])
        else:
            obj_inst.set_min_upper('NONE')

        obj_inst.logger.info("set min_lower")
        if tags.MIN_LOWER in kwargs.keys():
            obj_inst.set_min_lower(kwargs[tags.PASSWORD_MIN_LOWER_CASE_CHARS])
        else:
            obj_inst.set_min_lower('NONE')

        obj_inst.logger.info("set min_numeric")
        if tags.MIN_NUMERIC in kwargs.keys():
            obj_inst.set_min_numeric(kwargs[tags.PASSWORD_MIN_NUMERIC_CHARS])
        else:
            obj_inst.set_min_numeric('NONE')

        obj_inst.logger.info("set min_special")
        if tags.MIN_SPECIAL in kwargs.keys():
            obj_inst.set_min_special(kwargs[tags.PASSWORD_MIN_SPECIAL_CHARS])
        else:
            obj_inst.set_min_special('NONE')

        obj_inst.logger.info("set min_age")
        if tags.MIN_AGE in kwargs.keys():
            obj_inst.set_min_age(kwargs[tags.PASSWORD_MIN_AGE_DAYS])
        else:
            obj_inst.set_min_age('NONE')

        obj_inst.logger.info("set max_age")
        if tags.MAX_AGE in kwargs.keys():
            obj_inst.set_max_age(kwargs[tags.PASSWORD_MAX_AGE_DAYS])
        else:
            obj_inst.set_max_age('NONE')

        obj_inst.logger.info("set max_retries")
        if tags.MAX_RETRIES in kwargs.keys():
            obj_inst.set_max_retries(kwargs[tags.PASSWORD_MAX_RETRIES])
        else:
            obj_inst.set_max_retries('NONE')

        obj_inst.logger.info("set lockout_time")
        if tags.LOCKOUT_TIME in kwargs.keys():
            obj_inst.set_lockout_time(kwargs[tags.PASSWORD_LOCKOUT_TIME_MINS])
        else:
            obj_inst.set_lockout_time('NONE')

        obj_inst.logger.info("set history")
        if tags.HISTORY in kwargs.keys():
            obj_inst.set_history(kwargs[tags.PASSWORD_HISTORY])
        else:
            obj_inst.set_history('NONE')

        obj_inst.logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        obj_inst.logger.info("set tag_clause")
        if tags.TAG_CLAUSE in kwargs.keys():
            obj_inst.set_tag_clause(kwargs[tags.TAG_CLAUSE])
        else:
            obj_inst.set_tag_clause('NONE')


        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

