from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fizzbuzz.serializer import FizzBuzzSerializer


class FizzbuzzApiView(APIView):

    def solution(value):
        final_value = []
        string = ''
        for num in range(1, value):
            if num % 3 == 0:
                string = string + "Fizz "
            if num % 5 == 0:
                string = string + "Buzz "
            if num % 5 != 0 and num % 3 != 0:
                string = string + str(num) + " "
            final_value.append(string)
        return string


    def post(self, request):
        serializer = FizzBuzzSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = request.data['count']
            final_value = []
            string = ''
            for num in range(1, data):
                if num % 3 == 0:
                    string = string + "Fizz "
                if num % 5 == 0:
                    string = string + "Buzz "
                if num % 5 != 0 and num % 3 != 0:
                    string = string + str(num) + " "
                final_value.append(string)
            # return string
            result = string
        return Response(result, status=status.HTTP_200_OK)
