
class ValidateSalesforce:
    @staticmethod
    def is_valid_selection_for_columns_to_fetch(columns_list_available,columns_to_pull):
        diff=set(columns_to_pull) - set(columns_list_available)
        if diff:
            raise InvalidColumnToPull()
        else:
            return True