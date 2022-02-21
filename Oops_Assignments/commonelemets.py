from stringclass import obj
from pairspossible import obj_2


class SearchCommonElements():

    def get_list_of_common_elements(self, obj, second_string):

        first_string = obj.Mainstring

        dict_for_elements = {}
        for i in first_string:
            if i in dict_for_elements:
                dict_for_elements[i] += 1
            else:
                dict_for_elements[i] = 1
        result_list = []
        for j in second_string:
            if j in dict_for_elements and dict_for_elements[j] > 0:
                result_list.append(j)
                dict_for_elements[j] -= 1
        return result_list


obj_3 = SearchCommonElements()
answer_one = obj_3.get_list_of_common_elements(obj, "12345679")
answer_two = obj_3.get_list_of_common_elements(obj_2.obj_1, "12345679")

print(answer_one)
print(answer_two)